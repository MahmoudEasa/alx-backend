#!/usr/bin/env python3
""" Setup a basic Flask app
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ Class to configure available languages """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home() -> str:
    """ Home Route """
    return (render_template("1-index.html"))


if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    app.run(host=host, port=port, threaded=True)
