Flask-Imagine
============

[![Author](https://img.shields.io/badge/author-Kronas-blue.svg)](https://github.com/kronas)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/kronas/Flask-Imagine/master/LICENSE)
[![PyPi](https://img.shields.io/badge/pypi-0.3.1-red.svg)](https://pypi.python.org/pypi/Flask-Imagine)
[![Build Status](https://travis-ci.org/FlaskGuys/Flask-Imagine.svg?branch=master)](https://travis-ci.org/FlaskGuys/Flask-Imagine)
[![Dependency Status](https://www.versioneye.com/user/projects/570503e8fcd19a0039f15cc1/badge.svg)](https://www.versioneye.com/user/projects/570503e8fcd19a0039f15cc1)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/FlaskGuys/Flask-Imagine/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/FlaskGuys/Flask-Imagine/?branch=master)
[![Build Status](https://scrutinizer-ci.com/g/FlaskGuys/Flask-Imagine/badges/build.png?b=master)](https://scrutinizer-ci.com/g/FlaskGuys/Flask-Imagine/build-status/master)
[![Code Health](https://landscape.io/github/FlaskGuys/Flask-Imagine/master/landscape.svg)](https://landscape.io/github/FlaskGuys/Flask-Imagine/master)
[![codecov.io](https://codecov.io/github/FlaskGuys/Flask-Imagine/coverage.svg?branch=master)](https://codecov.io/github/FlaskGuys/Flask-Imagine?branch=master)
[![Documentation Status](https://readthedocs.org/projects/flask-imagine/badge/?version=latest)](http://flask-imagine.readthedocs.org/en/latest/?badge=latest)

Extension which provides easy image manipulation support in Flask applications.

Installation
------
```
$ pip install Flask-Imagine
```

Configuration example
------
```
from flask import Flask
from flask.ext.imagine import Imagine

app = Flask(__name__)

app.config['IMAGINE_ADAPTER'] = {
    'name': 'fs',
    'source_folder': 'static',
    'cache_folder': 'cache'
}

app.config['IMAGINE_FILTER_SETS'] = {
    'filter_set_name': {
        'cache': True,
        'filters': {
            # Filters initialization parameters
        }
    }
}
```
