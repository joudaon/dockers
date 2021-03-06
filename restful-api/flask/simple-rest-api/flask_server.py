import flask
import os
import logging
from flask import request, jsonify

app = flask.Flask(__name__)
app.logger.setLevel(logging.INFO)

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
      'title': 'A Fire Upon the Deep',
      'author': 'Vernor Vinge',
      'first_sentence': 'The coldsleep itself was dreamless.',
      'year_published': '1992'},
    {'id': 1,
      'title': 'The Ones Who Walk Away From Omelas',
      'author': 'Ursula K. Le Guin',
      'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
      'published': '1973'},
    {'id': 2,
      'title': 'Dhalgren',
      'author': 'Samuel R. Delany',
      'first_sentence': 'to wound the autumnal city.',
      'published': '1975'},
    {'id': 3,
      'title': 'One Up On Wall Street',
      'author': 'Peter Lynch',
      'first_sentence': 'Do you wonder',
      'published': '2000'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

# A route to return all of the available entries in our catalog.
# $> curl http://localhost:5000/api/v1/resources/books/all
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    app.logger.info("Getting all book catalog. Request from: {}".format(request.remote_addr))
    return jsonify(books)

# A route to return one specific book.
# $> curl http://localhost:5000/api/v1/resources/books?id=1
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    app.logger.info("Getting a book from catalog. Request from: {}".format(request.remote_addr))
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

# A route to delete specific book
# $> curl -X DELETE http://localhost:5000/api/v1/resources/books/delete?id=1
@app.route('/api/v1/resources/books/delete', methods=['DELETE'])
def api_id_delete():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
        logging.warning("ID: {}".format(id))
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)
            books.remove(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

# A route to add a new book
# $> curl -d '{"id":4, "title":"One Up On Wall Street", "author":"Peter Lynch", "first_sentence":"Do you wonder", "published": "2000"}' -H "Content-Type: application/json" -X PUT http://localhost:5000/api/v1/resources/books/add
@app.route('/api/v1/resources/books/add', methods=['PUT'])
def api_id_add():
    book = request.get_json()
    books.append(book)
    return jsonify(book)

# app.run()