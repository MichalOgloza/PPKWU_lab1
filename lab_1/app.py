from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"


@app.route("/reverse/<text>")
def revert(text):
    return text


if __name__ == '__main__':
    app.run(debug=True)
