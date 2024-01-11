from flask import Flask
from flask import render_template 


enc = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'o', 'ó', 'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż']
dec = ['⁅', '⁆', '<', '>', '⌈', '⌉', '«', '»', '⌊', '⌋', '⟨', '⟩', '⟦', '⟧', '⟪', '⟫', '⟬', '⟭', '‡', '¶', '⁋', '⁕', '‣', '⁌', '⁜', '※', '♪', '✕', '⌀', '⏕', '⏔', '⁒', '‽', '⸘']


key = int(input())

def encrypt(text):
    text = ""
    key_for_enc = (key // (key * 8))**2 
    for i in text:
        if (ord(i) - key_for_enc < 98):
            text += chr(ord(i) - key_for_enc + key)
        else:
            text += chr(ord(text) - key_for_enc)
    return text


def decrypt():
    pass


app = Flask(__name__)


@app.route("/")
def page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run("localhost", 8080, debug=True)
