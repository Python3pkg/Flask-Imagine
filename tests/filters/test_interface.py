import unittest
from flask.ext.imagine.filters.interface import ImagineFilterInterface


class TestImagineFilterInterface(unittest.TestCase):
    interface = None

    def setUp(self):
        self.interface = ImagineFilterInterface()

    def test_not_implemented_apply_method(self):
        with self.assertRaises(NotImplementedError):
            self.interface.apply('')
