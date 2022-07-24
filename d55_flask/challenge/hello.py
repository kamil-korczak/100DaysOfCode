from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"

    return wrapper


def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"

    return wrapper


@app.route('/')
def hello_world():
    return 'Hello, World!'


# Different routes using the app.route decorator
@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!"


# Creating variable paths and converting the path to specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"


# To run the application you can use lines below or use the flask command or python’s -m switch with Flask.
# Before you can do that you need to tell your terminal the application to work with by exporting
# the FLASK_APP environment variable
# $ export FLASK_APP=hello.py
# $ flask run

if __name__ == '__main__':
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
