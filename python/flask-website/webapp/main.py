from flask import Flask, render_template
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

# Route with greeting
@app.route('/hello/<name>', methods=['GET'])
def add_name(name):
  greeting = 'Hello ' + name
  mycursor.execute("""INSERT INTO user (email) VALUES (%s)""",(name,))
  mydb.commit()
  mycursor.close()
  mydb.close()
  return(greeting)

# Route with greeting
@app.route('/login', methods=['GET'])
def login():
  return render_template('login.html')

if __name__ == '__main__':
  app.run(debug=True, port=5000)
