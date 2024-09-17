from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 10)
#user_input = int(input('guess the number:'))

@app.route("/")
def game():
    return ('<h1> Guess the number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')


@app.route("/<int:userinput>")
def answer(userinput):
    if userinput > random_number:
        return ('<h1 style="color:red"> Too high! Try again </h1>'
                '<img src= "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')

    if userinput < random_number:
        return ('<h1 style="color:yellow"> Too low ! Try again </h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')

    if userinput == random_number:
        return ('<h1 style="color:purple"> You found me </h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')




if __name__ == "__main__":
    app.run(debug=True)



