from flask import Flask, html_template

app = Flask(__name__)


@app.route("/")
def root():
    return html_template("index.html")


# ㅇㅅㅇ...
