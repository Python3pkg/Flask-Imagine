from . import TestCase
from flask import url_for
from flask.ext.imagine.filters import ThumbnailFilter
from six.moves.urllib.parse import urlsplit


class TestAddFilterSet(TestCase):
    def test_wrong_parameters(self):
        with self.assertRaises(TypeError):
            self.imagine.add_filter_set()

        with self.assertRaises(ValueError):
            self.imagine.add_filter_set({}, [])

        with self.assertRaises(ValueError):
            self.imagine.add_filter_set('test_set', '')

        with self.assertRaises(ValueError):
            self.imagine.add_filter_set('test_set', [])

        with self.assertRaises(ValueError):
            self.imagine.add_filter_set('test_set', ['asd'])

        with self.assertRaises(ValueError):
            self.imagine.add_filter_set('test_set', [ThumbnailFilter(size=[100, 100], mode='inset')], '')

    def test_duplicate_filter_name(self):
        thumbnail_filter = ThumbnailFilter(size=[100, 100], mode='inset')
        self.imagine.add_filter_set('test_set', [thumbnail_filter, ])

        with self.assertRaises(ValueError):
            self.imagine.add_filter_set('test_set', [thumbnail_filter, ])

    def test_success_filter_addition_with_cache(self):
        self.imagine.add_filter_set('test_dynamic_set_cached', [ThumbnailFilter(size=[100, 100], mode='inset')])

        url = url_for('imagine', path='flask.png', filter_name='test_dynamic_set_cached', _external=False)

        parsed_url = urlsplit(url)

        self.assertEqual('/media/cache/resolve/test_dynamic_set_cached/flask.png', parsed_url.path)

        response = self.client.get(url)

        self.assert302(response)
        self.assertEqual('http://localhost/static/cache/test_dynamic_set_cached/flask.png', response.headers['Location'])

    def test_success_filter_addition_without_cache(self):
        self.imagine.add_filter_set('test_dynamic_set', [ThumbnailFilter(size=[100, 100], mode='inset')], cached=False)

        url = url_for('imagine', path='flask.png', filter_name='test_dynamic_set', _external=False)

        parsed_url = urlsplit(url)

        self.assertEqual('/media/cache/resolve/test_dynamic_set/flask.png', parsed_url.path)

        response = self.client.get(url)

        self.assert200(response)
