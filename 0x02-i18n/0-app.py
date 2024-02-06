#!/usr/bin/env python3
""" Setup a basic Flask app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """ Home Route """
    return (render_templage("0-index.html"))


if __name__ == "__main__":
    app.run()
