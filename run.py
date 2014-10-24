#!virtualenv/bin/python
from flask import Flask
from flask import render_template
from tidylib import tidy_document

app = Flask(__name__)

@app.route('/')
def route_index():
    files = {'device': {'full': {'foo': None}, 'bar': None, 'empty': {}}}
    response = render_template("index.html", tree=files)
    response, errors = tidy_document(response)
    return response

if __name__ == "__main__":
    app.run(port=5050, debug=True, host='127.0.0.1')
