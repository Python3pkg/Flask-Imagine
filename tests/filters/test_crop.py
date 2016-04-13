import os
import unittest
from copy import copy
from PIL import Image
from flask.ext.imagine.filters.crop import CropFilter


class TestCropFilter(unittest.TestCase):
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
            CropFilter(**{})

        with self.assertRaises(ValueError):
            CropFilter(**{'start': 'string'})

        with self.assertRaises(ValueError):
            CropFilter(**{'size': 'string'})

        with self.assertRaises(ValueError):
            CropFilter(**{'start': 'string', 'size': 'string'})

        with self.assertRaises(ValueError):
            CropFilter(**{'start': 'string', 'size': [100, 100]})

        with self.assertRaises(ValueError):
            CropFilter(**{'start': [0, 0], 'size': 'string'})

        with self.assertRaises(ValueError):
            CropFilter(**{'start': [1], 'size': [100, 100]})

        with self.assertRaises(ValueError):
            CropFilter(**{'start': [0, 0], 'size': [100]})

        with self.assertRaises(ValueError):
            CropFilter(**{'start': [1, 2, 3], 'size': [100, 100]})

        with self.assertRaises(ValueError):
            CropFilter(**{'start': [0, 0], 'size': [100, 100, 100]})

    def test_wrong_resource_type(self):
        crop = CropFilter(**{'start': [0, 0], 'size': [800, 600]})
        with self.assertRaises(ValueError):
            crop.apply('string')

    def test_success_horizontal_with_start_from_zero(self):
        crop = CropFilter(**{'start': [0, 0], 'size': [800, 600]})

        image_png = copy(self.image_png)
        image_png = crop.apply(image_png)
        self.assertTupleEqual((800, 500), image_png.size)

        image_jpg = copy(self.image_jpg)
        image_jpg = crop.apply(image_jpg)
        self.assertTupleEqual((800, 500), image_jpg.size)

        image_tif = copy(self.image_tif)
        image_tif = crop.apply(image_tif)
        self.assertTupleEqual((800, 500), image_tif.size)

        image_bmp = copy(self.image_bmp)
        image_bmp = crop.apply(image_bmp)
        self.assertTupleEqual((800, 500), image_bmp.size)

    def test_success_horizontal_with_start_from_point(self):
        crop = CropFilter(**{'start': [100, 100], 'size': [800, 600]})

        image_png = copy(self.image_png)
        image_png = crop.apply(image_png)
        self.assertTupleEqual((800, 400), image_png.size)

        image_jpg = copy(self.image_jpg)
        image_jpg = crop.apply(image_jpg)
        self.assertTupleEqual((800, 400), image_jpg.size)

        image_tif = copy(self.image_tif)
        image_tif = crop.apply(image_tif)
        self.assertTupleEqual((800, 400), image_tif.size)

        image_bmp = copy(self.image_bmp)
        image_bmp = crop.apply(image_bmp)
        self.assertTupleEqual((800, 400), image_bmp.size)

    def test_success_with_oversize(self):
        crop = CropFilter(**{'start': [0, 0], 'size': [1500, 1000]})

        image_png = copy(self.image_png)
        image_png = crop.apply(image_png)
        self.assertTupleEqual((1000, 500), image_png.size)

        image_jpg = copy(self.image_jpg)
        image_jpg = crop.apply(image_jpg)
        self.assertTupleEqual((1000, 500), image_jpg.size)

        image_tif = copy(self.image_tif)
        image_tif = crop.apply(image_tif)
        self.assertTupleEqual((1000, 500), image_tif.size)

        image_bmp = copy(self.image_bmp)
        image_bmp = crop.apply(image_bmp)
        self.assertTupleEqual((1000, 500), image_bmp.size)

    def test_error_with_out_of_range(self):
        crop = CropFilter(**{'start': [1000, 1000], 'size': [1500, 1000]})

        image_png = copy(self.image_png)
        image_png = crop.apply(image_png)
        self.assertTupleEqual((1000, 500), image_png.size)

        image_jpg = copy(self.image_jpg)
        image_jpg = crop.apply(image_jpg)
        self.assertTupleEqual((1000, 500), image_jpg.size)

        image_tif = copy(self.image_tif)
        image_tif = crop.apply(image_tif)
        self.assertTupleEqual((1000, 500), image_tif.size)

        image_bmp = copy(self.image_bmp)
        image_bmp = crop.apply(image_bmp)
        self.assertTupleEqual((1000, 500), image_bmp.size)
