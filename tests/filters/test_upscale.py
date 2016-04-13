import os
import unittest
from copy import copy
from PIL import Image
from flask.ext.imagine.filters.upscale import UpscaleFilter


class TestUpscaleFilter(unittest.TestCase):
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

    def test_wrong_init_parameters(self):
        with self.assertRaises(ValueError):
            UpscaleFilter(**{})

        with self.assertRaises(ValueError):
            UpscaleFilter(**{'min': 'string'})

        with self.assertRaises(ValueError):
            UpscaleFilter(**{'min': []})

        with self.assertRaises(ValueError):
            UpscaleFilter(**{'min': [1]})

        with self.assertRaises(ValueError):
            UpscaleFilter(**{'min': [1, 2, 3]})

    def test_wrong_resource_type(self):
        upscale = UpscaleFilter(**{'min': [800, 600]})
        with self.assertRaises(ValueError):
            upscale.apply('string')

    def test_small_image(self):
        upscale = UpscaleFilter(**{'min': [1920, 1080]})

        image_png = copy(self.image_png)
        image_png = upscale.apply(image_png)
        self.assertTupleEqual((1920, 960), image_png.size)

        image_jpg = copy(self.image_jpg)
        image_jpg = upscale.apply(image_jpg)
        self.assertTupleEqual((1920, 960), image_jpg.size)

        image_tif = copy(self.image_tif)
        image_tif = upscale.apply(image_tif)
        self.assertTupleEqual((1920, 960), image_tif.size)

        image_bmp = copy(self.image_bmp)
        image_bmp = upscale.apply(image_bmp)
        self.assertTupleEqual((1920, 960), image_bmp.size)

    def test_big_image(self):
        upscale = UpscaleFilter(**{'min': [800, 600]})

        image_png = copy(self.image_png)
        image_png = upscale.apply(image_png)
        self.assertTupleEqual((1000, 500), image_png.size)

        image_jpg = copy(self.image_jpg)
        image_jpg = upscale.apply(image_jpg)
        self.assertTupleEqual((1000, 500), image_jpg.size)

        image_tif = copy(self.image_tif)
        image_tif = upscale.apply(image_tif)
        self.assertTupleEqual((1000, 500), image_tif.size)

        image_bmp = copy(self.image_bmp)
        image_bmp = upscale.apply(image_bmp)
        self.assertTupleEqual((1000, 500), image_bmp.size)
