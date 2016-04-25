import os
import unittest
from copy import copy
from PIL import Image
from flask.ext.imagine.filters.thumbnail import ThumbnailFilter


class TestThumbnailFilter(unittest.TestCase):
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

    def test_inset_sizes(self):
        # Target image dimensions equal to original image dimensions.
        self.assertTupleEqual((100, 100), ThumbnailFilter.inset_sizes(100, 100, 100, 100))
        self.assertTupleEqual((100, 40), ThumbnailFilter.inset_sizes(100, 40, 100, 40))
        self.assertTupleEqual((25, 100), ThumbnailFilter.inset_sizes(25, 100, 25, 100))

        # Target image dimensions greater than original image dimensions. Similar proportion.
        self.assertTupleEqual((100, 100), ThumbnailFilter.inset_sizes(100, 100, 150, 150))
        self.assertTupleEqual((100, 100), ThumbnailFilter.inset_sizes(100, 100, 500, 500))
        self.assertTupleEqual((100, 100), ThumbnailFilter.inset_sizes(100, 100, 1000, 1000))
        self.assertTupleEqual((100, 40), ThumbnailFilter.inset_sizes(100, 40, 150, 150))
        self.assertTupleEqual((100, 40), ThumbnailFilter.inset_sizes(100, 40, 500, 500))
        self.assertTupleEqual((100, 40), ThumbnailFilter.inset_sizes(100, 40, 1000, 1000))
        self.assertTupleEqual((25, 100), ThumbnailFilter.inset_sizes(25, 100, 150, 150))
        self.assertTupleEqual((25, 100), ThumbnailFilter.inset_sizes(25, 100, 500, 500))
        self.assertTupleEqual((25, 100), ThumbnailFilter.inset_sizes(25, 100, 1000, 1000))

        # Target image dimensions greater than original image dimensions. Wide proportion.
        self.assertTupleEqual((100, 100), ThumbnailFilter.inset_sizes(100, 100, 200, 100))
        self.assertTupleEqual((100, 100), ThumbnailFilter.inset_sizes(100, 100, 200, 150))
        self.assertTupleEqual((100, 100), ThumbnailFilter.inset_sizes(100, 100, 1000, 200))
        self.assertTupleEqual((100, 40), ThumbnailFilter.inset_sizes(100, 40, 200, 100))
        self.assertTupleEqual((100, 40), ThumbnailFilter.inset_sizes(100, 40, 200, 150))
        self.assertTupleEqual((100, 40), ThumbnailFilter.inset_sizes(100, 40, 1000, 200))
        self.assertTupleEqual((25, 100), ThumbnailFilter.inset_sizes(25, 100, 200, 100))
        self.assertTupleEqual((25, 100), ThumbnailFilter.inset_sizes(25, 100, 200, 150))
        self.assertTupleEqual((25, 100), ThumbnailFilter.inset_sizes(25, 100, 1000, 200))

        # Target image dimensions greater than original image dimensions. Tall proportion.
        self.assertTupleEqual((100, 100), ThumbnailFilter.inset_sizes(100, 100, 100, 200))
        self.assertTupleEqual((100, 100), ThumbnailFilter.inset_sizes(100, 100, 150, 200))
        self.assertTupleEqual((100, 100), ThumbnailFilter.inset_sizes(100, 100, 200, 1000))
        self.assertTupleEqual((100, 40), ThumbnailFilter.inset_sizes(100, 40, 100, 200))
        self.assertTupleEqual((100, 40), ThumbnailFilter.inset_sizes(100, 40, 150, 200))
        self.assertTupleEqual((100, 40), ThumbnailFilter.inset_sizes(100, 40, 200, 1000))
        self.assertTupleEqual((25, 100), ThumbnailFilter.inset_sizes(25, 100, 100, 200))
        self.assertTupleEqual((25, 100), ThumbnailFilter.inset_sizes(25, 100, 150, 200))
        self.assertTupleEqual((25, 100), ThumbnailFilter.inset_sizes(25, 100, 200, 1000))

        # Target image dimensions less than original image dimensions. Similar proportion.
        self.assertTupleEqual((25, 25), ThumbnailFilter.inset_sizes(100, 100, 25, 25))
        self.assertTupleEqual((50, 50), ThumbnailFilter.inset_sizes(100, 100, 50, 50))
        self.assertTupleEqual((80, 80), ThumbnailFilter.inset_sizes(100, 100, 80, 80))
        self.assertTupleEqual((25, 10), ThumbnailFilter.inset_sizes(100, 40, 25, 25))
        self.assertTupleEqual((50, 20), ThumbnailFilter.inset_sizes(100, 40, 50, 50))
        self.assertTupleEqual((80, 32), ThumbnailFilter.inset_sizes(100, 40, 80, 80))
        self.assertTupleEqual((10, 25), ThumbnailFilter.inset_sizes(40, 100, 25, 25))
        self.assertTupleEqual((20, 50), ThumbnailFilter.inset_sizes(40, 100, 50, 50))
        self.assertTupleEqual((32, 80), ThumbnailFilter.inset_sizes(40, 100, 80, 80))

        # Wide transform
        self.assertTupleEqual((80, 80), ThumbnailFilter.inset_sizes(100, 100, 1000, 80))
        self.assertTupleEqual((80, 80), ThumbnailFilter.inset_sizes(100, 100, 120, 80))
        self.assertTupleEqual((50, 50), ThumbnailFilter.inset_sizes(100, 100, 150, 50))

        # Tall transform
        self.assertTupleEqual((80, 80), ThumbnailFilter.inset_sizes(100, 100, 80, 1000))
        self.assertTupleEqual((80, 80), ThumbnailFilter.inset_sizes(100, 100, 80, 120))
        self.assertTupleEqual((50, 50), ThumbnailFilter.inset_sizes(100, 100, 50, 150))

    def test_outbound_sizes(self):
        # Target image dimensions equal to original image dimensions.
        self.assertTupleEqual((100, 100), ThumbnailFilter.outbound_sizes(100, 100, 100, 100))
        self.assertTupleEqual((100, 40), ThumbnailFilter.outbound_sizes(100, 40, 100, 40))
        self.assertTupleEqual((25, 100), ThumbnailFilter.outbound_sizes(25, 100, 25, 100))

        # Target image dimensions greater than original image dimensions. Similar proportion.
        self.assertTupleEqual((100, 100), ThumbnailFilter.outbound_sizes(100, 100, 150, 150))
        self.assertTupleEqual((100, 100), ThumbnailFilter.outbound_sizes(100, 100, 500, 500))
        self.assertTupleEqual((100, 100), ThumbnailFilter.outbound_sizes(100, 100, 1000, 1000))
        self.assertTupleEqual((100, 40), ThumbnailFilter.outbound_sizes(100, 40, 150, 150))
        self.assertTupleEqual((100, 40), ThumbnailFilter.outbound_sizes(100, 40, 500, 500))
        self.assertTupleEqual((100, 40), ThumbnailFilter.outbound_sizes(100, 40, 1000, 1000))
        self.assertTupleEqual((25, 100), ThumbnailFilter.outbound_sizes(25, 100, 150, 150))
        self.assertTupleEqual((25, 100), ThumbnailFilter.outbound_sizes(25, 100, 500, 500))
        self.assertTupleEqual((25, 100), ThumbnailFilter.outbound_sizes(25, 100, 1000, 1000))

        # Target image dimensions greater than original image dimensions. Wide proportion.
        self.assertTupleEqual((100, 100), ThumbnailFilter.outbound_sizes(100, 100, 200, 100))
        self.assertTupleEqual((100, 100), ThumbnailFilter.outbound_sizes(100, 100, 200, 150))
        self.assertTupleEqual((100, 100), ThumbnailFilter.outbound_sizes(100, 100, 1000, 200))
        self.assertTupleEqual((100, 40), ThumbnailFilter.outbound_sizes(100, 40, 200, 100))
        self.assertTupleEqual((100, 40), ThumbnailFilter.outbound_sizes(100, 40, 200, 150))
        self.assertTupleEqual((100, 40), ThumbnailFilter.outbound_sizes(100, 40, 1000, 200))
        self.assertTupleEqual((25, 100), ThumbnailFilter.outbound_sizes(25, 100, 200, 100))
        self.assertTupleEqual((25, 100), ThumbnailFilter.outbound_sizes(25, 100, 200, 150))
        self.assertTupleEqual((25, 100), ThumbnailFilter.outbound_sizes(25, 100, 1000, 200))

        # Target image dimensions greater than original image dimensions. Tall proportion.
        self.assertTupleEqual((100, 100), ThumbnailFilter.outbound_sizes(100, 100, 100, 200))
        self.assertTupleEqual((100, 100), ThumbnailFilter.outbound_sizes(100, 100, 150, 200))
        self.assertTupleEqual((100, 100), ThumbnailFilter.outbound_sizes(100, 100, 200, 1000))
        self.assertTupleEqual((100, 40), ThumbnailFilter.outbound_sizes(100, 40, 100, 200))
        self.assertTupleEqual((100, 40), ThumbnailFilter.outbound_sizes(100, 40, 150, 200))
        self.assertTupleEqual((100, 40), ThumbnailFilter.outbound_sizes(100, 40, 200, 1000))
        self.assertTupleEqual((25, 100), ThumbnailFilter.outbound_sizes(25, 100, 100, 200))
        self.assertTupleEqual((25, 100), ThumbnailFilter.outbound_sizes(25, 100, 150, 200))
        self.assertTupleEqual((25, 100), ThumbnailFilter.outbound_sizes(25, 100, 200, 1000))

        # Target image dimensions less than original image dimensions. Similar proportion.
        self.assertTupleEqual((25, 25), ThumbnailFilter.outbound_sizes(100, 100, 25, 25))
        self.assertTupleEqual((50, 50), ThumbnailFilter.outbound_sizes(100, 100, 50, 50))
        self.assertTupleEqual((80, 80), ThumbnailFilter.outbound_sizes(100, 100, 80, 80))
        self.assertTupleEqual((50, 20), ThumbnailFilter.outbound_sizes(100, 40, 20, 20))
        self.assertTupleEqual((100, 40), ThumbnailFilter.outbound_sizes(100, 40, 50, 50))
        self.assertTupleEqual((100, 40), ThumbnailFilter.outbound_sizes(100, 40, 80, 80))
        self.assertTupleEqual((20, 50), ThumbnailFilter.outbound_sizes(40, 100, 20, 20))
        self.assertTupleEqual((40, 100), ThumbnailFilter.outbound_sizes(40, 100, 50, 50))
        self.assertTupleEqual((40, 100), ThumbnailFilter.outbound_sizes(40, 100, 80, 80))

        # Target image dimensions less than original image dimensions. Wide transform
        self.assertTupleEqual((100, 100), ThumbnailFilter.outbound_sizes(100, 100, 1000, 80))
        self.assertTupleEqual((100, 100), ThumbnailFilter.outbound_sizes(100, 100, 120, 80))
        self.assertTupleEqual((100, 100), ThumbnailFilter.outbound_sizes(100, 100, 150, 50))

        # Target image dimensions less than original image dimensions. Tall transform
        self.assertTupleEqual((100, 100), ThumbnailFilter.outbound_sizes(100, 100, 80, 1000))
        self.assertTupleEqual((100, 100), ThumbnailFilter.outbound_sizes(100, 100, 80, 120))
        self.assertTupleEqual((100, 100), ThumbnailFilter.outbound_sizes(100, 100, 50, 150))

    def test_crop_sizes(self):
        # Target image dimensions equal to original image dimensions.
        self.assertTupleEqual((0, 0, 100, 100), ThumbnailFilter.crop_sizes(100, 100, 100, 100))

        # Target image dimensions greater than original image dimensions. Wide proportion.
        self.assertTupleEqual((0, 0, 100, 80), ThumbnailFilter.crop_sizes(100, 80, 150, 100))

        # Target image dimensions greater than original image dimensions. Tall proportion.
        self.assertTupleEqual((0, 0, 80, 100), ThumbnailFilter.crop_sizes(80, 100, 100, 150))

        # Target image dimensions less than original image dimensions. Wide transform
        self.assertTupleEqual((0, 10, 100, 90), ThumbnailFilter.crop_sizes(100, 100, 100, 80))
        self.assertTupleEqual((25, 0, 75, 80), ThumbnailFilter.crop_sizes(100, 80, 50, 100))

        # Target image dimensions less than original image dimensions. Tall transform
        self.assertTupleEqual((10, 0, 90, 100), ThumbnailFilter.crop_sizes(100, 100, 80, 100))
        self.assertTupleEqual((0, 25, 80, 75), ThumbnailFilter.crop_sizes(80, 100, 100, 50))

    def test_inset_png(self):
        thumbnail_filter = ThumbnailFilter(size=[100, 100], mode='inset')
        image_png = copy(self.image_png)
        image_png = thumbnail_filter.apply(image_png)
        self.assertTupleEqual((100, 50), image_png.size)

        thumbnail_filter = ThumbnailFilter(size=[500, 100], mode='inset')
        image_png = copy(self.image_png)
        image_png = thumbnail_filter.apply(image_png)
        self.assertTupleEqual((200, 100), image_png.size)

        thumbnail_filter = ThumbnailFilter(size=[100, 50], mode='inset')
        image_png = copy(self.image_png)
        image_png = thumbnail_filter.apply(image_png)
        self.assertTupleEqual((100, 50), image_png.size)

        thumbnail_filter = ThumbnailFilter(size=[2000, 50], mode='inset')
        image_png = copy(self.image_png)
        image_png = thumbnail_filter.apply(image_png)
        self.assertTupleEqual((100, 50), image_png.size)

        thumbnail_filter = ThumbnailFilter(size=[2000, 1000], mode='inset')
        image_png = copy(self.image_png)
        image_png = thumbnail_filter.apply(image_png)
        self.assertTupleEqual((1000, 500), image_png.size)

    def test_inset_jpg(self):
        thumbnail_filter = ThumbnailFilter(size=[100, 100], mode='inset')
        image_jpg = copy(self.image_jpg)
        image_jpg = thumbnail_filter.apply(image_jpg)
        self.assertTupleEqual((100, 50), image_jpg.size)

        thumbnail_filter = ThumbnailFilter(size=[500, 100], mode='inset')
        image_jpg = copy(self.image_jpg)
        image_jpg = thumbnail_filter.apply(image_jpg)
        self.assertTupleEqual((200, 100), image_jpg.size)

        thumbnail_filter = ThumbnailFilter(size=[100, 50], mode='inset')
        image_jpg = copy(self.image_jpg)
        image_jpg = thumbnail_filter.apply(image_jpg)
        self.assertTupleEqual((100, 50), image_jpg.size)

        thumbnail_filter = ThumbnailFilter(size=[2000, 50], mode='inset')
        image_jpg = copy(self.image_jpg)
        image_jpg = thumbnail_filter.apply(image_jpg)
        self.assertTupleEqual((100, 50), image_jpg.size)

        thumbnail_filter = ThumbnailFilter(size=[2000, 1000], mode='inset')
        image_jpg = copy(self.image_jpg)
        image_jpg = thumbnail_filter.apply(image_jpg)
        self.assertTupleEqual((1000, 500), image_jpg.size)

    def test_inset_tif(self):
        thumbnail_filter = ThumbnailFilter(size=[100, 100], mode='inset')
        image_tif = copy(self.image_tif)
        image_tif = thumbnail_filter.apply(image_tif)
        self.assertTupleEqual((100, 50), image_tif.size)

        thumbnail_filter = ThumbnailFilter(size=[500, 100], mode='inset')
        image_tif = copy(self.image_tif)
        image_tif = thumbnail_filter.apply(image_tif)
        self.assertTupleEqual((200, 100), image_tif.size)

        thumbnail_filter = ThumbnailFilter(size=[100, 50], mode='inset')
        image_tif = copy(self.image_tif)
        image_tif = thumbnail_filter.apply(image_tif)
        self.assertTupleEqual((100, 50), image_tif.size)

        thumbnail_filter = ThumbnailFilter(size=[2000, 50], mode='inset')
        image_tif = copy(self.image_tif)
        image_tif = thumbnail_filter.apply(image_tif)
        self.assertTupleEqual((100, 50), image_tif.size)

        thumbnail_filter = ThumbnailFilter(size=[2000, 1000], mode='inset')
        image_tif = copy(self.image_tif)
        image_tif = thumbnail_filter.apply(image_tif)
        self.assertTupleEqual((1000, 500), image_tif.size)

    def test_inset_bmp(self):
        thumbnail_filter = ThumbnailFilter(size=[100, 100], mode='inset')
        image_bmp = copy(self.image_bmp)
        image_bmp = thumbnail_filter.apply(image_bmp)
        self.assertTupleEqual((100, 50), image_bmp.size)

        thumbnail_filter = ThumbnailFilter(size=[500, 100], mode='inset')
        image_bmp = copy(self.image_bmp)
        image_bmp = thumbnail_filter.apply(image_bmp)
        self.assertTupleEqual((200, 100), image_bmp.size)

        thumbnail_filter = ThumbnailFilter(size=[100, 50], mode='inset')
        image_bmp = copy(self.image_bmp)
        image_bmp = thumbnail_filter.apply(image_bmp)
        self.assertTupleEqual((100, 50), image_bmp.size)

        thumbnail_filter = ThumbnailFilter(size=[2000, 50], mode='inset')
        image_bmp = copy(self.image_bmp)
        image_bmp = thumbnail_filter.apply(image_bmp)
        self.assertTupleEqual((100, 50), image_bmp.size)

        thumbnail_filter = ThumbnailFilter(size=[2000, 1000], mode='inset')
        image_bmp = copy(self.image_bmp)
        image_bmp = thumbnail_filter.apply(image_bmp)
        self.assertTupleEqual((1000, 500), image_bmp.size)

    def test_outbound_png(self):
        thumbnail_filter = ThumbnailFilter(size=[100, 100], mode='outbound')
        image_png = copy(self.image_png)
        image_png = thumbnail_filter.apply(image_png)
        self.assertTupleEqual((100, 100), image_png.size)

        thumbnail_filter = ThumbnailFilter(size=[500, 100], mode='outbound')
        image_png = copy(self.image_png)
        image_png = thumbnail_filter.apply(image_png)
        self.assertTupleEqual((500, 100), image_png.size)

        thumbnail_filter = ThumbnailFilter(size=[100, 50], mode='outbound')
        image_png = copy(self.image_png)
        image_png = thumbnail_filter.apply(image_png)
        self.assertTupleEqual((100, 50), image_png.size)

        thumbnail_filter = ThumbnailFilter(size=[2000, 50], mode='outbound')
        image_png = copy(self.image_png)
        image_png = thumbnail_filter.apply(image_png)
        self.assertTupleEqual((1000, 50), image_png.size)

        thumbnail_filter = ThumbnailFilter(size=[2000, 1000], mode='outbound')
        image_png = copy(self.image_png)
        image_png = thumbnail_filter.apply(image_png)
        self.assertTupleEqual((1000, 500), image_png.size)

    def test_outbound_jpg(self):
        thumbnail_filter = ThumbnailFilter(size=[100, 100], mode='outbound')
        image_jpg = copy(self.image_jpg)
        image_jpg = thumbnail_filter.apply(image_jpg)
        self.assertTupleEqual((100, 100), image_jpg.size)

        thumbnail_filter = ThumbnailFilter(size=[500, 100], mode='outbound')
        image_jpg = copy(self.image_jpg)
        image_jpg = thumbnail_filter.apply(image_jpg)
        self.assertTupleEqual((500, 100), image_jpg.size)

        thumbnail_filter = ThumbnailFilter(size=[100, 50], mode='outbound')
        image_jpg = copy(self.image_jpg)
        image_jpg = thumbnail_filter.apply(image_jpg)
        self.assertTupleEqual((100, 50), image_jpg.size)

        thumbnail_filter = ThumbnailFilter(size=[2000, 50], mode='outbound')
        image_jpg = copy(self.image_jpg)
        image_jpg = thumbnail_filter.apply(image_jpg)
        self.assertTupleEqual((1000, 50), image_jpg.size)

        thumbnail_filter = ThumbnailFilter(size=[2000, 1000], mode='outbound')
        image_jpg = copy(self.image_jpg)
        image_jpg = thumbnail_filter.apply(image_jpg)
        self.assertTupleEqual((1000, 500), image_jpg.size)

    def test_outbound_tif(self):
        thumbnail_filter = ThumbnailFilter(size=[100, 100], mode='outbound')
        image_tif = copy(self.image_tif)
        image_tif = thumbnail_filter.apply(image_tif)
        self.assertTupleEqual((100, 100), image_tif.size)

        thumbnail_filter = ThumbnailFilter(size=[500, 100], mode='outbound')
        image_tif = copy(self.image_tif)
        image_tif = thumbnail_filter.apply(image_tif)
        self.assertTupleEqual((500, 100), image_tif.size)

        thumbnail_filter = ThumbnailFilter(size=[100, 50], mode='outbound')
        image_tif = copy(self.image_tif)
        image_tif = thumbnail_filter.apply(image_tif)
        self.assertTupleEqual((100, 50), image_tif.size)

        thumbnail_filter = ThumbnailFilter(size=[2000, 50], mode='outbound')
        image_tif = copy(self.image_tif)
        image_tif = thumbnail_filter.apply(image_tif)
        self.assertTupleEqual((1000, 50), image_tif.size)

        thumbnail_filter = ThumbnailFilter(size=[2000, 1000], mode='outbound')
        image_tif = copy(self.image_tif)
        image_tif = thumbnail_filter.apply(image_tif)
        self.assertTupleEqual((1000, 500), image_tif.size)

    def test_outbound_bmp(self):
        thumbnail_filter = ThumbnailFilter(size=[100, 100], mode='outbound')
        image_bmp = copy(self.image_bmp)
        image_bmp = thumbnail_filter.apply(image_bmp)
        self.assertTupleEqual((100, 100), image_bmp.size)

        thumbnail_filter = ThumbnailFilter(size=[500, 100], mode='outbound')
        image_bmp = copy(self.image_bmp)
        image_bmp = thumbnail_filter.apply(image_bmp)
        self.assertTupleEqual((500, 100), image_bmp.size)

        thumbnail_filter = ThumbnailFilter(size=[100, 50], mode='outbound')
        image_bmp = copy(self.image_bmp)
        image_bmp = thumbnail_filter.apply(image_bmp)
        self.assertTupleEqual((100, 50), image_bmp.size)

        thumbnail_filter = ThumbnailFilter(size=[2000, 50], mode='outbound')
        image_bmp = copy(self.image_bmp)
        image_bmp = thumbnail_filter.apply(image_bmp)
        self.assertTupleEqual((1000, 50), image_bmp.size)

        thumbnail_filter = ThumbnailFilter(size=[2000, 1000], mode='outbound')
        image_bmp = copy(self.image_bmp)
        image_bmp = thumbnail_filter.apply(image_bmp)
        self.assertTupleEqual((1000, 500), image_bmp.size)

    def test_wrong_thumbnail_size(self):
        with self.assertRaises(ValueError):
            ThumbnailFilter(size='', mode='inset')

        with self.assertRaises(ValueError):
            ThumbnailFilter(size=[100, 100], mode='')

        with self.assertRaises(ValueError):
            ThumbnailFilter(size=[100], mode='')

        with self.assertRaises(TypeError):
            ThumbnailFilter(size='size')

    def test_wrong_resource_type(self):
        thumbnail_filter = ThumbnailFilter(size=[100, 100], mode='outbound')
        with self.assertRaises(ValueError):
            thumbnail_filter.apply('')
