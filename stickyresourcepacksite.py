from flask import Flask
import zipfile
import dominate
import bs4
from dominate.tags import *

app = Flask(__name__)


@app.route("/")
def main_page():
    doc = dominate.document(title="DumbDogDiner Resource Pack Builder")
    with doc.head:
        link(rel='stylesheet', href='static/style.css')
        script(type='text/javascript', src='static/test1.js')
    with doc:
        with div(id='header').add(ol()):
            for i in ['home', 'about', 'contact']:
                li(a(i.title(), href='/%s.html' % i))

        with div():
            attr(cls='body')
            p('Lorem ipsum..')
    return str(doc)



@app.route("/mkpack")
def hello():
    with open('static/main.html') as mainhtm:
        contents = mainhtm.read()
    return contents


@app.route("/*.zip")
def dozip():
    print("xp")
    return "derp"

if __name__ == "__main__":
    app.run(host='0.0.0.0')