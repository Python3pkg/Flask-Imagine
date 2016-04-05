import unittest
from flask.ext.imagine.adapters.interface import ImagineAdapterInterface


class TestImagineAdapterInterface(unittest.TestCase):
    interface = None

    def setUp(self):
        self.interface = ImagineAdapterInterface()

    def test_not_implemented_get_item_method(self):
        with self.assertRaises(NotImplementedError):
            self.interface.get_item('')

    def test_not_implemented_create_cached_item_method(self):
        with self.assertRaises(NotImplementedError):
            self.interface.create_cached_item('', '')

    def test_not_implemented_get_cached_item_method(self):
        with self.assertRaises(NotImplementedError):
            self.interface.get_cached_item('')

    def test_not_implemented_check_cached_item_method(self):
        with self.assertRaises(NotImplementedError):
            self.interface.check_cached_item('')

    def test_not_implemented_remove_cached_item_method(self):
        with self.assertRaises(NotImplementedError):
            self.interface.remove_cached_item('')
