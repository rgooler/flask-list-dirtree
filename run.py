#!virtualenv/bin/python
from flask import Flask
from flask import render_template
from tidylib import tidy_document
import os

import pprint
pp = pprint.PrettyPrinter(indent=2)
pp.__call__ = pp.pprint

app = Flask(__name__)

@app.route('/')
def route_index():
    response = render_template("index.html", tree=list_files('test'))
    response, errors = tidy_document(response)
    return response

def list_files(rootdir):
    """
    Creates a nested dictionary that represents the folder structure of rootdir
    """
    d = {}
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        subdir = {}
        for f in files:
            subdir[f] = path
        parent = reduce(dict.get, folders[:-1], d)
        parent[folders[-1]] = subdir
    return d

if __name__ == "__main__":
    app.run(port=5050, debug=True, host='127.0.0.1')

    #pp(list_files('test'))
