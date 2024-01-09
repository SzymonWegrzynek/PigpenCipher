from flask import Flask
from flask import render_template 


app = Flask(__name__)


enc = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'o', 'ó', 'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż']
dec = ['⁅', '⁆', '<', '>', '⌈', '⌉', '«', '»', '⌊', '⌋', '⟨', '⟩', '⟦', '⟧', '⟪', '⟫', '⟬', '⟭', '‡', '¶', '⁋', '⁕', '‣', '⁌', '⁜', '※', '♪', '✕', '⌀', '⏕', '⏔', '⁒', '‽', '⸘']


def encrypt():
    pass


def decrypt():
    pass


@app.route("/")
def page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run("localhost", 8080, debug=True)
