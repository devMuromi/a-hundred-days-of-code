from flask import Flask, render_template, redirect, url_for
import requests


app = Flask(__name__)


@app.route("/")
def home():
    return redirect(url_for("blog"))


@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/8ca3f3b91e6448ef25f1"
    res = requests.get(blog_url)
    data = res.json()

    return render_template("index.html", posts=data)


@app.route("/post/<int:post_id>")
def get_post(post_id):
    blog_url = "https://api.npoint.io/8ca3f3b91e6448ef25f1"
    res = requests.get(blog_url)
    data = res.json()[post_id - 1]
    return render_template("post.html", post=data)


if __name__ == "__main__":
    app.run(debug=True)
