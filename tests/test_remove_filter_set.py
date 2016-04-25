from . import TestCase
from flask import url_for
from flask.ext.imagine.filters import ThumbnailFilter
from six.moves.urllib.parse import urlsplit


class TestRemoveFilterSet(TestCase):
    def test_wrong_parameters(self):
        with self.assertRaises(TypeError):
            self.imagine.remove_filter_set()

        with self.assertRaises(ValueError):
            self.imagine.remove_filter_set('')

    def test_remove_filter(self):
        thumbnail_filter = ThumbnailFilter(size=[100, 100], mode='inset')
        self.imagine.add_filter_set('test_removable_set', [thumbnail_filter, ])

        self.imagine.remove_filter_set('test_removable_set')

        self.assertFalse('test_removable_set' in self.imagine._filter_sets)
