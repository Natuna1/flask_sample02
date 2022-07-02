from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello,World"


@app.route("/member")
def member():
    return "Hello,Member"


if __name__ == "__main__":
    app.run()
