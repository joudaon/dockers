from flask import Flask, render_template, url_for, request, session
from flask_bootstrap import Bootstrap
import mysql.connector
import os

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
  greeting = 'Hello ' + name
  mycursor.execute("""INSERT INTO user (email, password) VALUES (%s,%s)""",(name,'jonpass'))
  mydb.commit()
  mycursor.close()
  mydb.close()
  return(greeting)

# Route with greeting
@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    form = request.form
    username = form['username']
    email = form['email']
    password = form['password']
    mycursor.execute("""INSERT INTO user (username, email, password) VALUES (%s,%s,%s)""",(username,email,password))
    mydb.commit()
    mycursor.close()
    mydb.close()
    session['username'] = request.form['username']
    return 'Successfully registered'
  return render_template('login.html')

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
