#!/usr/bin/env python3
""" Setup a basic Flask app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home() -> str:
    """ Home Route """
    return (render_template("0-index.html"))


if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    app.run(host=host, port=port, threaded=True)
