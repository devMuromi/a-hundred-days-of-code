from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template(
        "index.html", random_number=random_number, current_year=current_year
    )


@app.route("/guess/<name>")
def guess(name):
    name = name.capitalize()
    res = requests.get(url="https://api.genderize.io", params={"name": name})
    data = res.json()
    print(data)
    gender = data["gender"]
    res = requests.get(url="https://api.agify.io", params={"name": name})
    data = res.json()
    age = data["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)


@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/8ca3f3b91e6448ef25f1"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
