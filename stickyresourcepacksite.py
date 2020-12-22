from flask import Flask
import zipfile
import dominate
from bs4 import dammit,BeautifulSoup
from dominate.tags import *
import sys, os

app = Flask(__name__)



def generate_thumbnail(name):
    if not(isinstance(name, str)):
        raise ValueError('name must be of type str')
    title = name.title()
    name = title.replace(' ', '')
    returned_div = div(id=name)
    with returned_div:
        attr(_class='thumbnail')
        img(source=name.replace(' ', '') + '.png')
        br()
        p(title)
    return returned_div


@app.route("/")
def main_page():
    soup = BeautifulSoup(open('static/base.html'))







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
    #app.run(host='0.0.0.0')
    print(generate_thumbnail('test thingy'))