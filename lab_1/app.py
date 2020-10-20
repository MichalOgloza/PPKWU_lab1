from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "This API has a reverse string functionality available at address: /reverse/textToReverse"


@app.route("/reverse/<text>")
def revert(text):
    return text[::-1]


if __name__ == '__main__':
    app.run(debug=True)
