#!/usr/bin/env python3
""" Setup a basic Flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ Class to configure available languages """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user() -> Union[Dict, None]:
    """ Returns a user dictionary or None if the ID cannot be found
        or if login_as was not passed
    """
    login_as = request.args.get("login_as", None)

    if not login_as:
        return (None)

    return (users[login_as] or None)


@app.before_request
def before_request():
    """ Set get_user as a global on flask.g.user """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """ Get Locale Function """
    locale = request.args.get("locale", None)
    if locale and locale in Config.LANGUAGES:
        return (locale)

    return (request.accept_languages.best_match(app.config["LANGUAGES"]))

# babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def home() -> str:
    """ Home Route """
    return (render_template("5-index.html", user=g.user))


if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    app.run(host=host, port=port, threaded=True)
