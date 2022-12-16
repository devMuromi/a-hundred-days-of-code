from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(0, 9)

# def make_bold(function):
#     def wrapper():
#         return f"<b>{function()}</b>"

#     return wrapper


# def make_emphasis(function):
#     def wrapper():
#         return f"<em>{function()}</em>"

#     return wrapper


# def make_underlined(function):
#     def wrapper():
#         return f"<u>{function()}</u>"

#     return wrapper


def make_h1(function):
    def wrapper(*args, **kwargs):
        return f"<h1>{function(*args, **kwargs)}</h1>"

    return wrapper


@app.route("/")
def hello_world():
    return (
        "Hello World!"
        "<h1>Bye World!</h1>"
        "<h2>Bye World!</h2>"
        "<h3>Bye World!</h3>"
        "<h4>Bye World!</h4>"
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"
    )


@app.route("/bye")
def bye_world():
    return "Bye World!"


@app.route("/<int:number>")
@make_h1
def check_number(number):
    if number == random_number:
        return "You guessed correctly!"
    elif number > random_number:
        return "Too high!, try again"
    else:
        return "Too low!, try again"


if __name__ == "__main__":
    app.run(debug=True)
