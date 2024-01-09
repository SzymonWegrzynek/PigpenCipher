from flask import Flask
from flask import render_template 


app = Flask(__name__)


def encrypt():
    pass


def decrypt():
    pass


@app.route("/")
def page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run("localhost", 8080, debug=True)
