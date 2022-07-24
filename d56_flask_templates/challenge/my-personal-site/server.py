from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/site1")
def site_1():
    return render_template('site1.html')


@app.route("/site2")
def site_2():
    return render_template('site2.html')


if __name__ == '__main__':
    app.run(debug=True)
