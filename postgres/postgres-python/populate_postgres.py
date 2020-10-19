import psycopg2
import random
import string
import time

record_number = 10000

def generate_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    # print("Random string of length", length, "is:", result_str)
    return result_str

def generate_random_genre():
  genreList = ['Drama','Sci-Fi','Comedy','Romance','Action']
  return random.choice(genreList)

def generate_movies_query(id):
  return "insert into movies values ({},'movie-{}','{}','{}','{}')".format(id, generate_random_string(3), id, random.randint(1950,2020), generate_random_genre())

def generate_ratings_query(id):
  return "insert into ratings values ('{}','{}','{}')".format(id, random.randint(0,10), random.randint(0,10))


print('Waiting 10s to Postgres')
time.sleep(10)
print('10 seconds waited. Starting...')

try:
  connection = psycopg2.connect(user = "postgres",
                                password = "postgres",
                                host = "postgres",
                                port = "5432",
                                database = "postgres")

  cursor = connection.cursor()
  print("PostgreSQL connection is opened")

  create_movies_query = '''CREATE TABLE movies 
        (titleid INT PRIMARY KEY NOT NULL,
        title TEXT NOT NULL,
        ratingid INT NOT NULL,
        year INT,
        genre TEXT); '''

  create_ratings_query = '''CREATE TABLE ratings 
        (ratingid INT PRIMARY KEY NOT NULL,
        audio INT,
        video INT); '''
  
  cursor.execute(create_movies_query)
  cursor.execute(create_ratings_query)

  for i in range(record_number):
    cursor.execute(generate_movies_query(i))
    cursor.execute(generate_ratings_query(i))

  connection.commit()
  print("Queries successfully run in PostgreSQL")

except (Exception, psycopg2.DatabaseError) as error :
  print ("Error while creating PostgreSQL table", error)

finally:
  #closing database connection.
    if(connection):
      cursor.close()
      connection.close()
      print("PostgreSQL connection is closed")