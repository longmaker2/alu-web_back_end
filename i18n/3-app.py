#!/usr/bin/env python3
""" Basic Flask App """
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


class Config(object):
    """ Configuration class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Determine the best language for the user """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def root():
    """ Render the index template """
    return render_template('3-index.html',
                           title=_('home_title'),
                           heading=_('home_header'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
