from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)


# For that example posts data are downloaded from API during server run,
# so they will be not requested from API on every load of main page and post page.
BLOG_API_URL = 'https://api.npoint.io/2eacbd1891d101c13a09'
blog_response = requests.get(BLOG_API_URL)
posts = blog_response.json()

posts_objects = []
for post in posts:
    posts_objects.append(
        Post(id=post.get('id'), title=post.get('title'), subtitle=post.get('subtitle'), body=post.get('body'), )
    )


@app.route('/')
def home():
    return render_template("index.html", posts=posts_objects)


@app.route('/post/<int:post_id>')
def display_post(post_id):
    post_data = []

    for post_single in posts_objects:
        if post_single.id == post_id:
            post_data = post_single
            break

    return render_template("post.html", post=post_data)


if __name__ == "__main__":
    app.run(debug=True)
