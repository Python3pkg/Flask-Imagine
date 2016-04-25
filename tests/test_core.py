from . import TestCase
from flask import Flask, url_for
from flask.ext.imagine import Imagine
from six.moves.urllib.parse import urlsplit


class TestCoreMethods(TestCase):
    def test_wrong_adapter_init(self):
        app = Flask(__name__)

        app.config['IMAGINE_ADAPTER'] = '_adapter'

        with self.assertRaises(ValueError):
            Imagine(app)

    def test_empty_filter_init(self):
        app = Flask(__name__)

        app.config['IMAGINE_FILTER_SETS'] = ''

        with self.assertRaises(ValueError):
            Imagine(app)

    def test_wrong_filter_init(self):
        app = Flask(__name__)

        class WrongFilter(object):
            pass

        app.config['IMAGINE_FILTERS'] = {
            'wrong_filter': WrongFilter
        }

        app.config['IMAGINE_FILTER_SETS'] = {
            'wrong_set': {
                '_filters': {
                    'wrong_filter': {}
                }
            }
        }

        with self.assertRaises(ValueError):
            Imagine(app)

    def test_unknown_filter_init(self):
        app = Flask(__name__)

        app.config['IMAGINE_FILTER_SETS'] = {
            'wrong_set': {
                '_filters': {
                    'wrong_filter': {}
                }
            }
        }

        with self.assertRaises(ValueError):
            Imagine(app)

    def test_wrong_filter_set_init(self):
        app = Flask(__name__)

        app.config['IMAGINE_FILTER_SETS'] = {
            'wrong_set': {}
        }

        with self.assertRaises(ValueError):
            Imagine(app)

    def test_init_without_cached(self):
        app = Flask(__name__)

        app.config['IMAGINE_FILTER_SETS'] = {
            'test_scale': {
                'filters': {
                    'thumbnail': {'size': [100, 100], 'mode': 'inset'}
                }
            }
        }

        imagine = Imagine(app)
        self.assertTrue(isinstance(imagine, Imagine))

    def test_not_exist_filter(self):
        url = url_for('imagine', path='flask.png', filter_name='not_exist', _external=False)

        self.assert404(self.client.get(url))

    def test_not_exist_image(self):
        url = url_for('imagine', path='not_exist.png', filter_name='test_scale_cached', _external=False)

        self.assert404(self.client.get(url))

    def test_build_url(self):
        url = url_for('imagine', path='flask.png', filter_name='test_scale_cached', _external=False)

        parsed_url = urlsplit(url)

        self.assertEqual('/media/cache/resolve/test_scale_cached/flask.png', parsed_url.path)

        response = self.client.get(url)

        self.assert302(response)
        self.assertEqual('http://localhost/static/cache/test_scale_cached/flask.png', response.headers['Location'])

        response = self.client.get(url)

        self.assert302(response)
        self.assertEqual('http://localhost/static/cache/test_scale_cached/flask.png', response.headers['Location'])

    def test_not_cached_filter_set(self):
        url = url_for('imagine', path='flask.png', filter_name='test_scale_dynamic', _external=False)

        parsed_url = urlsplit(url)

        self.assertEqual('/media/cache/resolve/test_scale_dynamic/flask.png', parsed_url.path)

        response = self.client.get(url)

        self.assert200(response)
