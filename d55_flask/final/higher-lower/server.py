from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)

IMG_CORRECT = 'https://media2.giphy.com/media/elsol3P5Jt2ASsxLva/giphy.gif'
IMG_TOO_LOW = 'https://media4.giphy.com/media/j3FzUsajPDD3OJKJyb/giphy.gif'
IMG_TOO_HIGH = 'https://media2.giphy.com/media/G2w61fwWbKtAKj3txt/giphy.gif'


@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<div style="width:480px"><iframe allow="fullscreen" frameBorder="0" height="270" src="https://giphy.com/embed/4pqm16XH2rQopZrdFU/video" width="480"></iframe></div>'


@app.route('/<int:number>')
def guess_number(number):
    if number == random_number:
        return '<h1 style="color:green">You found me!</h1>' \
               f'<img src="{IMG_CORRECT}" />'
    elif number < random_number:
        return '<h1 style="color:red">Too low, try again!</h1>' \
               f'<img src="{IMG_TOO_LOW}" />'
    else:
        return '<h1 style="color:purple">Too high, try again!</h1>' \
               f'<img src="{IMG_TOO_HIGH}" />'


if __name__ == '__main__':
    app.run(debug=True)
