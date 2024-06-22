#!/usr/bin/env python3
"""Simple flask app setup"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _ as get_translation
app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Class to set defualts for babel"""
    LANGUAGES = ["en", "fr"]
    Babel.default_locale = "en"
    Babel.default_timezone = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Get best langauge for user"""
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Return simple homepage"""
    if g.user:
        login_msg = get_translation('logged_in_as', username=g.user['name'])
    else:
        login_msg = get_translation('not_logged_in')
    return render_template('5-index.html', login_msg=login_msg)


def get_user():
    """get_user returns a user dictionary or None"""
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))

    return None


@app.before_request
def before_request():
    """find a user if any, and set it as a global"""
    g.user = get_user()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
