import os
import unittest
from copy import copy
from PIL import Image
from flask.ext.imagine.filters.rotate import RotateFilter


class TestRotateFilter(unittest.TestCase):
    image_png = None
    image_jpg = None
    image_tif = None
    image_bmp = None

    def setUp(self):
        assets_path = os.path.abspath(os.path.dirname(__file__)) + '/../static/'
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
        rotate_filter = RotateFilter(**{'angle': 0})
        with self.assertRaises(ValueError):
            rotate_filter.apply('string')

    def test_rotate_90(self):
        rotate_filter = RotateFilter(**{'angle': 90})

        image_png = copy(self.image_png)
        image_png = rotate_filter.apply(image_png)
        self.assertTupleEqual((501, 1000), image_png.size)

        image_jpg = copy(self.image_jpg)
        image_jpg = rotate_filter.apply(image_jpg)
        self.assertTupleEqual((501, 1000), image_jpg.size)

        image_tif = copy(self.image_tif)
        image_tif = rotate_filter.apply(image_tif)
        self.assertTupleEqual((501, 1000), image_tif.size)

        image_bmp = copy(self.image_bmp)
        image_bmp = rotate_filter.apply(image_bmp)
        self.assertTupleEqual((501, 1000), image_bmp.size)

    def test_rotate_180(self):
        rotate_filter = RotateFilter(**{'angle': 180})

        image_png = copy(self.image_png)
        image_png = rotate_filter.apply(image_png)
        self.assertTupleEqual((1001, 501), image_png.size)

        image_jpg = copy(self.image_jpg)
        image_jpg = rotate_filter.apply(image_jpg)
        self.assertTupleEqual((1001, 501), image_jpg.size)

        image_tif = copy(self.image_tif)
        image_tif = rotate_filter.apply(image_tif)
        self.assertTupleEqual((1001, 501), image_tif.size)

        image_bmp = copy(self.image_bmp)
        image_bmp = rotate_filter.apply(image_bmp)
        self.assertTupleEqual((1001, 501), image_bmp.size)
