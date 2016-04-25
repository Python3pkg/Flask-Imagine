import os
from tests import TestCase
from copy import copy
from PIL import Image
from flask.ext.imagine.filters.watermark import WatermarkFilter


class TestWatermarkFilter(TestCase):
    image_png = None
    image_jpg = None
    image_tif = None
    image_bmp = None

    def setUp(self):
        super(TestWatermarkFilter, self).setUp()

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
            WatermarkFilter(**{})

        with self.assertRaises(ValueError):
            WatermarkFilter(**{'image': 1})

        with self.assertRaises(ValueError):
            WatermarkFilter(**{'image': 'watermark.png', 'size': 'string', 'position': 'center'})

        with self.assertRaises(ValueError):
            WatermarkFilter(**{'image': 'watermark.png', 'size': 0.5, 'position': 1})

        with self.assertRaises(ValueError):
            WatermarkFilter(**{'image': 'watermark.png', 'size': 0.5})

        with self.assertRaises(ValueError):
            WatermarkFilter(**{'image': 'watermark.png', 'size': 0.5, 'position': 'center', 'opacity': 'string'})

        with self.assertRaises(ValueError):
            WatermarkFilter(**{'image': 'watermark.png', 'size': 1.5, 'position': 'center', 'opacity': 'string'})

        with self.assertRaises(ValueError):
            WatermarkFilter(**{'image': 'watermark.png', 'size': 0.5, 'position': 'center', 'opacity': 1.5})

    def test_wrong_watermark_path(self):
        with self.app.app_context():
            watermark_filter = WatermarkFilter(**{
                'image': 'file.png',
                'size': 0.5,
                'position': 'center'
            })
            image_jpg = copy(self.image_png)
            with self.assertRaises(ValueError):
                watermark_filter.apply(image_jpg)

    def test_wrong_resource_type(self):
        with self.app.app_context():
            watermark_filter = WatermarkFilter(**{
                'image': 'file.png',
                'size': 0.5,
                'position': 'center'
            })
            with self.assertRaises(ValueError):
                watermark_filter.apply('string')

    def test_top_left_position_with_horizontal_watermark(self):
        with self.app.app_context():
            watermark_filter = WatermarkFilter(**{
                'image': 'watermark.png',
                'size': 0.5,
                'position': 'top_left'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_top_left_position')(image_jpg)
            self.assertTupleEqual((500, 70), image.size)
            self.assertEqual(0, left)
            self.assertEqual(0, upper)

            watermark_filter = WatermarkFilter(**{
                'image': 'watermark.png',
                'size': 0.25,
                'position': 'top_left'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_top_left_position')(image_jpg)
            self.assertTupleEqual((250, 35), image.size)
            self.assertEqual(0, left)
            self.assertEqual(0, upper)

    def test_top_left_position_with_vertical_watermark(self):
        with self.app.app_context():
            watermark_filter = WatermarkFilter(**{
                'image': 'watermark_vertical.png',
                'size': 0.5,
                'position': 'top_left'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_top_left_position')(image_jpg)
            self.assertTupleEqual((35, 250), image.size)
            self.assertEqual(0, left)
            self.assertEqual(0, upper)

            watermark_filter = WatermarkFilter(**{
                'image': 'watermark_vertical.png',
                'size': 0.25,
                'position': 'top_left'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_top_left_position')(image_jpg)
            self.assertTupleEqual((17, 125), image.size)
            self.assertEqual(0, left)
            self.assertEqual(0, upper)

    def test_top_position_with_horizontal_watermark(self):
        with self.app.app_context():
            watermark_filter = WatermarkFilter(**{
                'image': 'watermark.png',
                'size': 0.5,
                'position': 'top'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_top_position')(image_jpg)
            self.assertTupleEqual((500, 70), image.size)
            self.assertEqual(250, left)
            self.assertEqual(0, upper)

            watermark_filter = WatermarkFilter(**{
                'image': 'watermark.png',
                'size': 0.25,
                'position': 'top'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_top_position')(image_jpg)
            self.assertTupleEqual((250, 35), image.size)
            self.assertEqual(375, left)
            self.assertEqual(0, upper)

    def test_top_position_with_vertical_watermark(self):
        with self.app.app_context():
            watermark_filter = WatermarkFilter(**{
                'image': 'watermark_vertical.png',
                'size': 0.5,
                'position': 'top'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_top_position')(image_jpg)
            self.assertTupleEqual((35, 250), image.size)
            self.assertEqual(483, left)
            self.assertEqual(0, upper)

            watermark_filter = WatermarkFilter(**{
                'image': 'watermark_vertical.png',
                'size': 0.25,
                'position': 'top'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_top_position')(image_jpg)
            self.assertTupleEqual((17, 125), image.size)
            self.assertEqual(492, left)
            self.assertEqual(0, upper)

    def test_top_right_position_with_horizontal_watermark(self):
        with self.app.app_context():
            watermark_filter = WatermarkFilter(**{
                'image': 'watermark.png',
                'size': 0.5,
                'position': 'top_right'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_top_right_position')(image_jpg)
            self.assertTupleEqual((500, 70), image.size)
            self.assertEqual(500, left)
            self.assertEqual(0, upper)

            watermark_filter = WatermarkFilter(**{
                'image': 'watermark.png',
                'size': 0.25,
                'position': 'top_right'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_top_right_position')(image_jpg)
            self.assertTupleEqual((250, 35), image.size)
            self.assertEqual(750, left)
            self.assertEqual(0, upper)

    def test_top_right_position_with_vertical_watermark(self):
        with self.app.app_context():
            watermark_filter = WatermarkFilter(**{
                'image': 'watermark_vertical.png',
                'size': 0.5,
                'position': 'top_right'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_top_right_position')(image_jpg)
            self.assertTupleEqual((35, 250), image.size)
            self.assertEqual(965, left)
            self.assertEqual(0, upper)

            watermark_filter = WatermarkFilter(**{
                'image': 'watermark_vertical.png',
                'size': 0.25,
                'position': 'top_right'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_top_right_position')(image_jpg)
            self.assertTupleEqual((17, 125), image.size)
            self.assertEqual(983, left)
            self.assertEqual(0, upper)

    def test_left_position_with_horizontal_watermark(self):
        with self.app.app_context():
            watermark_filter = WatermarkFilter(**{
                'image': 'watermark.png',
                'size': 0.5,
                'position': 'left'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_left_position')(image_jpg)
            self.assertTupleEqual((500, 70), image.size)
            self.assertEqual(0, left)
            self.assertEqual(215, upper)

            watermark_filter = WatermarkFilter(**{
                'image': 'watermark.png',
                'size': 0.25,
                'position': 'left'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_left_position')(image_jpg)
            self.assertTupleEqual((250, 35), image.size)
            self.assertEqual(0, left)
            self.assertEqual(233, upper)

    def test_left_position_with_vertical_watermark(self):
        with self.app.app_context():
            watermark_filter = WatermarkFilter(**{
                'image': 'watermark_vertical.png',
                'size': 0.5,
                'position': 'left'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_left_position')(image_jpg)
            self.assertTupleEqual((35, 250), image.size)
            self.assertEqual(0, left)
            self.assertEqual(125, upper)

            watermark_filter = WatermarkFilter(**{
                'image': 'watermark_vertical.png',
                'size': 0.25,
                'position': 'left'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_left_position')(image_jpg)
            self.assertTupleEqual((17, 125), image.size)
            self.assertEqual(0, left)
            self.assertEqual(188, upper)

    def test_center_position_with_horizontal_watermark(self):
        with self.app.app_context():
            watermark_filter = WatermarkFilter(**{
                'image': 'watermark.png',
                'size': 0.5,
                'position': 'center'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_center_position')(image_jpg)
            self.assertTupleEqual((500, 70), image.size)
            self.assertEqual(250, left)
            self.assertEqual(215, upper)

            watermark_filter = WatermarkFilter(**{
                'image': 'watermark.png',
                'size': 0.25,
                'position': 'center'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_center_position')(image_jpg)
            self.assertTupleEqual((250, 35), image.size)
            self.assertEqual(375, left)
            self.assertEqual(233, upper)

    def test_center_position_with_vertical_watermark(self):
        with self.app.app_context():
            watermark_filter = WatermarkFilter(**{
                'image': 'watermark_vertical.png',
                'size': 0.5,
                'position': 'center'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_center_position')(image_jpg)
            self.assertTupleEqual((35, 250), image.size)
            self.assertEqual(483, left)
            self.assertEqual(125, upper)

            watermark_filter = WatermarkFilter(**{
                'image': 'watermark_vertical.png',
                'size': 0.25,
                'position': 'center'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_center_position')(image_jpg)
            self.assertTupleEqual((17, 125), image.size)
            self.assertEqual(492, left)
            self.assertEqual(188, upper)

    def test_right_position_with_horizontal_watermark(self):
        with self.app.app_context():
            watermark_filter = WatermarkFilter(**{
                'image': 'watermark.png',
                'size': 0.5,
                'position': 'right'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_right_position')(image_jpg)
            self.assertTupleEqual((500, 70), image.size)
            self.assertEqual(500, left)
            self.assertEqual(215, upper)

            watermark_filter = WatermarkFilter(**{
                'image': 'watermark.png',
                'size': 0.25,
                'position': 'right'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_right_position')(image_jpg)
            self.assertTupleEqual((250, 35), image.size)
            self.assertEqual(750, left)
            self.assertEqual(233, upper)

    def test_right_position_with_vertical_watermark(self):
        with self.app.app_context():
            watermark_filter = WatermarkFilter(**{
                'image': 'watermark_vertical.png',
                'size': 0.5,
                'position': 'right'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_right_position')(image_jpg)
            self.assertTupleEqual((35, 250), image.size)
            self.assertEqual(965, left)
            self.assertEqual(125, upper)

            watermark_filter = WatermarkFilter(**{
                'image': 'watermark_vertical.png',
                'size': 0.25,
                'position': 'right'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_right_position')(image_jpg)
            self.assertTupleEqual((17, 125), image.size)
            self.assertEqual(983, left)
            self.assertEqual(188, upper)

    def test_bottom_left_position_with_horizontal_watermark(self):
        with self.app.app_context():
            watermark_filter = WatermarkFilter(**{
                'image': 'watermark.png',
                'size': 0.5,
                'position': 'bottom_left'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_bottom_left_position')(image_jpg)
            self.assertTupleEqual((500, 70), image.size)
            self.assertEqual(0, left)
            self.assertEqual(430, upper)

            watermark_filter = WatermarkFilter(**{
                'image': 'watermark.png',
                'size': 0.25,
                'position': 'bottom_left'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_bottom_left_position')(image_jpg)
            self.assertTupleEqual((250, 35), image.size)
            self.assertEqual(0, left)
            self.assertEqual(465, upper)

    def test_bottom_left_position_with_vertical_watermark(self):
        with self.app.app_context():
            watermark_filter = WatermarkFilter(**{
                'image': 'watermark_vertical.png',
                'size': 0.5,
                'position': 'bottom_left'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_bottom_left_position')(image_jpg)
            self.assertTupleEqual((35, 250), image.size)
            self.assertEqual(0, left)
            self.assertEqual(250, upper)

            watermark_filter = WatermarkFilter(**{
                'image': 'watermark_vertical.png',
                'size': 0.25,
                'position': 'bottom_left'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_bottom_left_position')(image_jpg)
            self.assertTupleEqual((17, 125), image.size)
            self.assertEqual(0, left)
            self.assertEqual(375, upper)

    def test_bottom_position_with_horizontal_watermark(self):
        with self.app.app_context():
            watermark_filter = WatermarkFilter(**{
                'image': 'watermark.png',
                'size': 0.5,
                'position': 'bottom'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_bottom_position')(image_jpg)
            self.assertTupleEqual((500, 70), image.size)
            self.assertEqual(250, left)
            self.assertEqual(430, upper)

            watermark_filter = WatermarkFilter(**{
                'image': 'watermark.png',
                'size': 0.25,
                'position': 'bottom'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_bottom_position')(image_jpg)
            self.assertTupleEqual((250, 35), image.size)
            self.assertEqual(375, left)
            self.assertEqual(465, upper)

    def test_bottom_position_with_vertical_watermark(self):
        with self.app.app_context():
            watermark_filter = WatermarkFilter(**{
                'image': 'watermark_vertical.png',
                'size': 0.5,
                'position': 'bottom'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_bottom_position')(image_jpg)
            self.assertTupleEqual((35, 250), image.size)
            self.assertEqual(483, left)
            self.assertEqual(250, upper)

            watermark_filter = WatermarkFilter(**{
                'image': 'watermark_vertical.png',
                'size': 0.25,
                'position': 'bottom'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_bottom_position')(image_jpg)
            self.assertTupleEqual((17, 125), image.size)
            self.assertEqual(492, left)
            self.assertEqual(375, upper)

    def test_bottom_right_position_with_horizontal_watermark(self):
        with self.app.app_context():
            watermark_filter = WatermarkFilter(**{
                'image': 'watermark.png',
                'size': 0.5,
                'position': 'bottom_right'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_bottom_right_position')(image_jpg)
            self.assertTupleEqual((500, 70), image.size)
            self.assertEqual(500, left)
            self.assertEqual(430, upper)

            watermark_filter = WatermarkFilter(**{
                'image': 'watermark.png',
                'size': 0.25,
                'position': 'bottom_right'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_bottom_right_position')(image_jpg)
            self.assertTupleEqual((250, 35), image.size)
            self.assertEqual(750, left)
            self.assertEqual(465, upper)

    def test_bottom_right_position_with_vertical_watermark(self):
        with self.app.app_context():
            watermark_filter = WatermarkFilter(**{
                'image': 'watermark_vertical.png',
                'size': 0.5,
                'position': 'bottom_right'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_bottom_right_position')(image_jpg)
            self.assertTupleEqual((35, 250), image.size)
            self.assertEqual(965, left)
            self.assertEqual(250, upper)

            watermark_filter = WatermarkFilter(**{
                'image': 'watermark_vertical.png',
                'size': 0.25,
                'position': 'bottom_right'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_bottom_right_position')(image_jpg)
            self.assertTupleEqual((17, 125), image.size)
            self.assertEqual(983, left)
            self.assertEqual(375, upper)

    def test_watermark_non_rgb(self):
        with self.app.app_context():
            watermark_filter = WatermarkFilter(**{
                'image': 'watermark_nonrgb.tif',
                'size': 0.5,
                'position': 'top_left'
            })
            image_jpg = copy(self.image_png)
            image, left, upper = getattr(watermark_filter, '_top_left_position')(image_jpg)
            self.assertTupleEqual((500, 70), image.size)
            self.assertEqual(0, left)
            self.assertEqual(0, upper)

            image_jpg = watermark_filter.apply(image_jpg)
            self.assertTupleEqual((1000, 500), image_jpg.size)
