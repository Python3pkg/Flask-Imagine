import os
import unittest
from copy import copy

from PIL import Image
from flask.ext.imagine.filters.autorotate import AutorotateFilter


class TestAutorotateFilter(unittest.TestCase):
    image_png = None
    image_jpg = None
    image_tif = None
    image_bmp = None

    def setUp(self):
        assets_path = os.path.abspath(os.path.dirname(__file__)) + '/../assets/'
        assets_path = os.path.normpath(assets_path)

        image_png_path = assets_path + '/flask.png'
        self.image_png = Image.open(image_png_path)

        image_jpg_path = assets_path + '/flask.jpg'
        self.image_jpg = Image.open(image_jpg_path)

        image_tif_path = assets_path + '/flask.tif'
        self.image_tif = Image.open(image_tif_path)

        image_bmp_path = assets_path + '/flask.bmp'
        self.image_bmp = Image.open(image_bmp_path)

    def test_wrong_resource_type(self):
        autorotate_filter = AutorotateFilter()
        with self.assertRaises(ValueError):
            autorotate_filter.apply('')

    def test_apply_method(self):
        autorotate_filter = AutorotateFilter()

        image_png = copy(self.image_png)
        image_png = autorotate_filter.apply(image_png)
        self.assertTrue(isinstance(image_png, Image.Image))

        image_jpg = copy(self.image_jpg)
        image_jpg = autorotate_filter.apply(image_jpg)
        self.assertTrue(isinstance(image_jpg, Image.Image))

        image_tif = copy(self.image_tif)
        image_tif = autorotate_filter.apply(image_tif)
        self.assertTrue(isinstance(image_tif, Image.Image))

        image_bmp = copy(self.image_bmp)
        image_bmp = autorotate_filter.apply(image_bmp)
        self.assertTrue(isinstance(image_bmp, Image.Image))
