# Flask Web Framework

## Table of Contents
- [Introduction](#introduction)
- [Setting up Flask](#setting-up-flask)
- [Routes in Flask](#routes-in-flask)
- [Templates in Flask](#templates-in-flask)
- [Dynamic Templates](#dynamic-templates)
- [Displaying Data from MySQL](#displaying-data-from-mysql)

## Introduction
### What is a Web Framework?
A web framework is a software framework designed to help developers build web applications including web services, web resources, and web APIs. Frameworks provide a standard way to build and deploy web applications, allowing developers to focus on writing the application-specific code, rather than the low-level details of handling requests, responses, etc.

## Setting up Flask
### How to Build a Web Framework with Flask
Flask is a micro web framework written in Python. It is classified as a micro framework because it does not require particular tools or libraries. Here are the steps to set it up:
```bash
pip install Flask
```
Then, in a new Python file:
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()
```

## Routes in Flask
### What is a Route?
A route is a URL pattern that the application uses to decide which view function should handle a request. The view functions in Flask are mapped to one or more route URLs so that Flask knows what logic to execute when a specific route is accessed.

### How to Define Routes in Flask
Using the `@app.route()` decorator in Flask, you can easily define routes. For instance:
```python
@app.route('/hello')
def hello():
    return "Hello Flask!"
```

### How to Handle Variables in a Route
Flask supports variable sections in the route. For instance, if you want to greet the user by their name:
```python
@app.route('/hello/<username>')
def hello_user(username):
    return f"Hello {username}!"
```

## Templates in Flask
### What is a Template?
A template contains variables and/or expressions, which get replaced with values when the template is rendered. Flask uses the Jinja2 template engine.

### How to Create a HTML Response in Flask Using a Template
First, create a new folder named `templates`. Inside this folder, you can store your HTML templates. Here's a simple `hello.html` template:
```html
<html>
    <body>
        <h1>Hello, {{ username }}!</h1>
    </body>
</html>
```
In your Flask app:
```python
from flask import render_template

@app.route('/hello/<username>')
def hello_user(username):
    return render_template('hello.html', username=username)
```

## Dynamic Templates
### How to Create a Dynamic Template (loops, conditions…)
Jinja2 allows loops and conditions in templates. For instance, to loop through a list of users:
```html
<ul>
{% for user in users %}
    <li>{{ user }}</li>
{% endfor %}
</ul>
```
Conditions can be used as:
```html
{% if user_logged_in %}
    <h1>Welcome, {{ username }}!</h1>
{% else %}
    <h1>Welcome, Guest!</h1>
{% endif %}
```

## Displaying Data from MySQL
### How to Display in HTML Data from a MySQL Database
First, set up a MySQL connection using an ORM like SQLAlchemy. Once you've fetched the data, pass it to `render_template`.
```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/dbname'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

@app.route('/users')
def list_users():
    users = User.query.all()
    return render_template('users.html', users=users)
```
Then in `users.html`:
```html
<ul>
{% for user in users %}
    <li>{{ user.username }}</li>
{% endfor %}
</ul>
```
---
