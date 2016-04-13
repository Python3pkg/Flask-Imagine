from flask import url_for
from flask.ext.imagine import imagine_cache_clear
from . import TestCase


class TestCacheClear(TestCase):
    def test_direct_cache_clear(self):
        url = url_for('imagine', path='flask.png', filter_name='test_scale', _external=False)

        response = self.client.get(url)
        self.assert302(response)

        imagine_cache_clear('flask.png', 'test_scale')

        url = url_for('imagine', path='flask.png', filter_name='test_scale', _external=False)

        response = self.client.get(url)
        self.assert302(response)

    def test_batch_cache_clear(self):
        url = url_for('imagine', path='flask.png', filter_name='test_scale', _external=False)

        response = self.client.get(url)
        self.assert302(response)

        imagine_cache_clear('flask.png')

        url = url_for('imagine', path='flask.png', filter_name='test_scale', _external=False)

        response = self.client.get(url)
        self.assert302(response)

