from urlparse import urlsplit

from . import TestCase
from flask import Flask, url_for
from flask.ext.imagine import Imagine


class TestCoreMethods(TestCase):
    def test_wrong_adapter_init(self):
        app = Flask(__name__)

        app.config['IMAGINE_ADAPTER'] = 'adapter'

        with self.assertRaises(ValueError):
            Imagine(app)

    def test_wrong_filter_init(self):
        class WrongFilter(object):
            pass

        app = Flask(__name__)

        app.config['IMAGINE_FILTERS'] = {
            'wrong_filter': WrongFilter
        }

        app.config['IMAGINE_FILTER_SETS'] = {
            'wrong_set': {
                'wrong_filter': {}
            }
        }

        with self.assertRaises(ValueError):
            Imagine(app)

    def test_not_exist_filter(self):
        url = url_for('imagine', path='flask.png', filter_name='not_exist', _external=False)

        self.assert404(self.client.get(url))

    def test_not_exist_image(self):
        url = url_for('imagine', path='not_exist.png', filter_name='test_scale', _external=False)

        self.assert404(self.client.get(url))

    def test_build_url(self):
        url = url_for('imagine', path='flask.png', filter_name='test_scale', _external=False)

        parsed_url = urlsplit(url)

        self.assertEqual('/media/cache/resolve/test_scale/flask.png', parsed_url.path)

        response = self.client.get(url)

        self.assert302(response)
        self.assertEqual('http://localhost/static/cache/test_scale/flask.png', response.headers['Location'])
