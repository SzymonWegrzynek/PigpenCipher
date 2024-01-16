from flask import Flask
from flask import render_template 


app = Flask(__name__)


@app.route("/")
def page():
    return render_template('index.html')


@app.post("/enc")
elo elo

if __name__ == "__main__":
    app.run("localhost", 8080, debug=True)
