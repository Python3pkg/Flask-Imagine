import os
import unittest
from copy import copy
from PIL import Image
from flask.ext.imagine.filters.relative_resize import RelativeResizeFilter


class TestRelativeResizeFilter(unittest.TestCase):
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
            RelativeResizeFilter(**{})

        with self.assertRaises(ValueError):
            RelativeResizeFilter(**{'method': 'string'})

        with self.assertRaises(ValueError):
            RelativeResizeFilter(**{'heighten': 'height'})

        with self.assertRaises(ValueError):
            RelativeResizeFilter(**{'widen': 'width'})

        with self.assertRaises(ValueError):
            RelativeResizeFilter(**{'increase': 'increase'})

        with self.assertRaises(ValueError):
            RelativeResizeFilter(**{'decrease': 'decrease'})

        with self.assertRaises(ValueError):
            RelativeResizeFilter(**{'scale': 'scale'})

    def test_wrong_resource_type(self):
        relative_resize = RelativeResizeFilter(**{'heighten': 50})
        with self.assertRaises(ValueError):
            relative_resize.apply('string')

    def test_heighten(self):
        relative_resize = RelativeResizeFilter(**{'heighten': 50})
        image_png = copy(self.image_png)
        image_png = relative_resize.apply(image_png)
        self.assertTupleEqual((100, 50), image_png.size)

        relative_resize = RelativeResizeFilter(**{'heighten': 50})
        image_jpg = copy(self.image_jpg)
        image_jpg = relative_resize.apply(image_jpg)
        self.assertTupleEqual((100, 50), image_jpg.size)

        relative_resize = RelativeResizeFilter(**{'heighten': 50})
        image_tif = copy(self.image_tif)
        image_tif = relative_resize.apply(image_tif)
        self.assertTupleEqual((100, 50), image_tif.size)

        relative_resize = RelativeResizeFilter(**{'heighten': 50})
        image_bmp = copy(self.image_bmp)
        image_bmp = relative_resize.apply(image_bmp)
        self.assertTupleEqual((100, 50), image_bmp.size)

    def test_widen(self):
        relative_resize = RelativeResizeFilter(**{'widen': 100})
        image_png = copy(self.image_png)
        image_png = relative_resize.apply(image_png)
        self.assertTupleEqual((100, 50), image_png.size)

        relative_resize = RelativeResizeFilter(**{'widen': 100})
        image_jpg = copy(self.image_jpg)
        image_jpg = relative_resize.apply(image_jpg)
        self.assertTupleEqual((100, 50), image_jpg.size)

        relative_resize = RelativeResizeFilter(**{'widen': 100})
        image_tif = copy(self.image_tif)
        image_tif = relative_resize.apply(image_tif)
        self.assertTupleEqual((100, 50), image_tif.size)

        relative_resize = RelativeResizeFilter(**{'widen': 100})
        image_bmp = copy(self.image_bmp)
        image_bmp = relative_resize.apply(image_bmp)
        self.assertTupleEqual((100, 50), image_bmp.size)

    def test_increase(self):
        relative_resize = RelativeResizeFilter(**{'increase': 1000})
        image_png = copy(self.image_png)
        image_png = relative_resize.apply(image_png)
        self.assertTupleEqual((2000, 1500), image_png.size)

        relative_resize = RelativeResizeFilter(**{'increase': 1000})
        image_jpg = copy(self.image_jpg)
        image_jpg = relative_resize.apply(image_jpg)
        self.assertTupleEqual((2000, 1500), image_jpg.size)

        relative_resize = RelativeResizeFilter(**{'increase': 1000})
        image_tif = copy(self.image_tif)
        image_tif = relative_resize.apply(image_tif)
        self.assertTupleEqual((2000, 1500), image_tif.size)

        relative_resize = RelativeResizeFilter(**{'increase': 1000})
        image_bmp = copy(self.image_bmp)
        image_bmp = relative_resize.apply(image_bmp)
        self.assertTupleEqual((2000, 1500), image_bmp.size)

    def test_decrease_success(self):
        relative_resize = RelativeResizeFilter(**{'decrease': 100})
        image_png = copy(self.image_png)
        image_png = relative_resize.apply(image_png)
        self.assertTupleEqual((900, 400), image_png.size)

        relative_resize = RelativeResizeFilter(**{'decrease': 100})
        image_jpg = copy(self.image_jpg)
        image_jpg = relative_resize.apply(image_jpg)
        self.assertTupleEqual((900, 400), image_jpg.size)

        relative_resize = RelativeResizeFilter(**{'decrease': 100})
        image_tif = copy(self.image_tif)
        image_tif = relative_resize.apply(image_tif)
        self.assertTupleEqual((900, 400), image_tif.size)

        relative_resize = RelativeResizeFilter(**{'decrease': 100})
        image_bmp = copy(self.image_bmp)
        image_bmp = relative_resize.apply(image_bmp)
        self.assertTupleEqual((900, 400), image_bmp.size)

    def test_decrease_fail(self):
        relative_resize = RelativeResizeFilter(**{'decrease': 500})
        image_png = copy(self.image_png)

        with self.assertRaises(ValueError):
            relative_resize.apply(image_png)

    def test_scale(self):
        relative_resize = RelativeResizeFilter(**{'scale': 1.5})
        image_png = copy(self.image_png)
        image_png = relative_resize.apply(image_png)
        self.assertTupleEqual((1500, 750), image_png.size)

        relative_resize = RelativeResizeFilter(**{'scale': 1.5})
        image_jpg = copy(self.image_jpg)
        image_jpg = relative_resize.apply(image_jpg)
        self.assertTupleEqual((1500, 750), image_jpg.size)

        relative_resize = RelativeResizeFilter(**{'scale': 1.5})
        image_tif = copy(self.image_tif)
        image_tif = relative_resize.apply(image_tif)
        self.assertTupleEqual((1500, 750), image_tif.size)

        relative_resize = RelativeResizeFilter(**{'scale': 1.5})
        image_bmp = copy(self.image_bmp)
        image_bmp = relative_resize.apply(image_bmp)
        self.assertTupleEqual((1500, 750), image_bmp.size)
