from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# To run the application you can use lines below or use the flask command or python’s -m switch with Flask.
# Before you can do that you need to tell your terminal the application to work with by exporting
# the FLASK_APP environment variable
# $ export FLASK_APP=hello.py
# $ flask run

if __name__ == '__main__':
    app.run()
