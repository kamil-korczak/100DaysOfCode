from flask import Flask, render_template
import datetime
import random
import requests

app = Flask(__name__)

GENDER_API_URL = 'https://api.genderize.io'
AGE_API_URL = 'https://api.agify.io'


def get_gender(name):
    response = requests.get(f"{GENDER_API_URL}?name={name}")
    gender_data = response.json()
    gender = gender_data.get('gender')
    return gender


def get_age_of_the_name(name):
    response = requests.get(f"{AGE_API_URL}?name={name}")
    age_data = response.json()
    age = age_data.get('age')
    return age


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year

    context = {
        'random_number': random_number,
        'current_year': current_year,
    }

    return render_template("index.html", **context)


@app.route('/guess/<name>')
def guess(name):
    gender = get_gender(name)
    age_of_the_name = get_age_of_the_name(name)
    variety_of_year = 'year' if age_of_the_name <= 1 else 'years'

    context = {
        'name': name.capitalize(),
        'gender': gender,
        'age_of_the_name': age_of_the_name,
        'variety_of_year': variety_of_year,
    }
    return render_template("guess.html", **context)


@app.route("/blog")
@app.route("/blog/<int:number>")
def get_blog(number=1):
    blog_api_url = 'https://api.npoint.io/2eacbd1891d101c13a09'
    response = requests.get(blog_api_url)
    posts = response.json()
    return render_template("blog.html", posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
