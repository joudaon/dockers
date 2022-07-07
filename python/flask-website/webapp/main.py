from flask import Flask, render_template, url_for, request, session
from flask_bootstrap import Bootstrap
from flask import request
import mysql.connector
import smtplib
import os
import logging
from logging.handlers import RotatingFileHandler

# Setup logging
logging.basicConfig(
  handlers=[RotatingFileHandler('./app.log', mode='a', maxBytes=10000000, backupCount=10)],
  format='%(asctime)-5s - PID: %(process)d - %(levelname)-8s - In Module: %(module)s and File: %(filename)s [%(pathname)s:%(lineno)d]: %(message)s',
  datefmt='%Y-%m-%d %H:%M:%S',
  level=logging.INFO
)
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.INFO)


# Get Environment Variables
## smtp
smtp_username = os.environ.get('SMTP_USERNAME') if os.environ.get('MYSQL_HOST') else 'test@gmail.com'
smtp_password = os.environ.get('SMTP_PASSWORD') if os.environ.get('MYSQL_HOST') else 'password'
smtp_host = os.environ.get('SMTP_HOST') if os.environ.get('MYSQL_HOST') else 'smtp.gmail.com'
smtp_port = os.environ.get('SMTP_PORT') if os.environ.get('MYSQL_HOST') else '587'

# Create smtp server
smtpconn = smtplib.SMTP(smtp_host, smtp_port)

mydb = mysql.connector.connect(
  host=os.environ.get('MYSQL_HOST') if os.environ.get('MYSQL_HOST') else 'localhost',
  user=os.environ.get('MYSQL_USER') if os.environ.get('MYSQL_USER') else 'root',
  password=os.environ.get('MYSQL_PASSWORD') if os.environ.get('MYSQL_PASSWORD') else 'password',
  database=os.environ.get('MYSQL_DATABASE') if os.environ.get('MYSQL_DATABASE') else 'website'
)

mycursor = mydb.cursor()

app = Flask(__name__)
Bootstrap(app)

# Secret key for sessions
# https://flask.palletsprojects.com/en/2.0.x/quickstart/#sessions
app.secret_key = 'mysecretkey'

# Route with greeting
@app.route('/hello/<name>', methods=['GET'])
def add_name(name):
  logging.info('Accessing from {}.'.format(request.remote_addr))
  greeting = 'Hello ' + name
  return(greeting)

# Route to register
@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    try:
      form = request.form
      username = form['username']
      email = form['email']
      password = form['password']
      mycursor.execute("""INSERT INTO user (username, email, password) VALUES (%s,%s,%s)""",(username,email,password))
      mydb.commit()
      # Send email
      try:
        smtpconn.ehlo()
        smtpconn.starttls()
        smtpconn.login(smtp_username, smtp_password)
        smtpconn.sendmail(smtp_username, email, 'Subject: Welcome to the website!\n\nWelcome to the website {}!'.format(username))
        smtpconn.quit()
        mycursor.close()
      except:
        logging.error('ERROR: Unable to send email')
      logging.info('User {} registered'.format(username))
    except:
      logging.error('ERROR: unable to register user')
      return 'ERROR: unable to register user'
    return 'Successfully registered'
  return render_template('register.html')

# Route to register
@app.route('/login', methods=['GET', 'POST'])
def login():
  # Output message if something goes wrong...
  msg = ''
  # Check if "username" and "password" POST requests exist (user submitted form)
  if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
      # Create variables for easy access
      email = request.form['email']
      password = request.form['password']
      # Check if account exists using MySQL
      mycursor.execute('SELECT id, username FROM user WHERE email = %s AND password = %s', (email, password,))
      # Fetch one record and return result
      account = mycursor.fetchone()
      # If account exists in accounts table in out database
      if account:
        id = account[0]
        username = account[1]
        # Create session data, we can access this data in other routes
        session['loggedin'] = True
        session['id'] = id
        session['username'] = username
        # Redirect to home page
        return 'Logged in successfully {}!'.format(username)
      else:
        # Account doesnt exist or username/password incorrect
        msg = 'Incorrect username/password!'
  return render_template('login.html', msg=msg)

# Test route
@app.route('/test', methods=['GET'])
def test():
  # fruits = ['orange, apple, mango']
  # return render_template('test.html', fruits=fruits)
  if 'username' in session:
    return f'Logged in as {session["username"]}'
  return 'You are not logged in'

if __name__ == '__main__':
  app.run(debug=True, port=5000)
