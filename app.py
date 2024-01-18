from flask import Flask
from flask import request
from flask import render_template
from pigpen_cipher import encrypt
from pigpen_cipher import decrypt


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.post("/enc")
def enc():
    key = int(request.form["key"])
    text = request.form["text"]
    pigpen_text = encrypt(text, key)
    return pigpen_text


@app.post("/dec")
def dec():
    key = int(request.form["key"])
    pigpen_text = request.form["pigpen_text"]
    text = decrypt(pigpen_text, key)
    return text


if __name__ == "__main__":
    app.run("localhost", 8080, debug=True)
