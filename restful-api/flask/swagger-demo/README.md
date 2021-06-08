# flask_demo 🌶
Flask demo project with auto generated Swagger documentation. Refer to the [IC Blog Post](https://www.imaginarycloud.com/blog/flask-python/) to have a detailed explanation of this demo.

![Flask Demo Screen Recording](https://www.imaginarycloud.com/blog/content/images/2021/03/documented_api--1--1.gif)

## Start Application Instructions

Clone the repo to your local machine by running the command:

```sh
git clone https://github.com/pedromartinho/flask_demo
```

You must have python installed in your machine. The code presented will run in python3. If you want to use python2 and/or are following this procedure in a Windows machine please refer to the instructions presented in the [Flask installation guide](https://flask.palletsprojects.com/en/1.1.x/installation/)

After that, go into the folder with the project and create a virtual environment with the following command:

```sh
python3 -m venv venv
```

Active the the respective environment by running:

```sh
. venv/bin/activate
```

**Note:** It might be important to specify the environment you are considering when running this code in your IDE.

Install the project's dependencies with the following command. This will consider the packages detailed in the requirements.txt file. This is done using [pip]
(https://pypi.org/) (Python package installer):

```sh
pip install -r requirements.txt
````

Before running the application set the Flask environment variables:

```sh
export FLASK_APP=main.py
export FLASK_ENV=development
```

Run Flask... RUN!!

```sh
flask run
```

## Relevant endpoints

The application has three different "modules" presented in detail in the [IC Blog Post](https://www.imaginarycloud.com/blog/flask-python/)

### Basic and classic hello world

Basic endpoints for demo purposes:

* https://flask-ic.herokuapp.com/basic_api/hello_world | GET method
* https://flask-ic.herokuapp.com/basic_api/entities | GET and POST methods
* https://flask-ic.herokuapp.com/basic_api/entities/<entity_id> | GET, PUT and DELETE methods

### Jinja

Example of a Jinja template rendering with dynamic content change based on query params **top** and **bottom**. This allows you to create your own **Business Cat** meme:

* https://flask-ic.herokuapp.com/jinja_template?top=cancel%20my%203%20o%27clock&bottom=the%20mouse%20is%20moving

### Documented endpoints

Endpoints created based on the Flask-RESTPlus suggested structure and documentation. All the endpoints previously created are presented with a better structure inside the **blueprints** folder. This is achieved with the usage of [Flask-RESTPlus extension](https://flask-restplus.readthedocs.io/en/stable/) You can check the generated documentation by referring to this link: https://flask-ic.herokuapp.com/documented_api/doc
