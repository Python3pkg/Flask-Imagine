from PIL import Image
from tests import TestCase


class TestImagineFilesystemAdapter(TestCase):
    adapter = None

    def setUp(self):
        super(TestImagineFilesystemAdapter, self).setUp()

        self.adapter = self.app.extensions['imagine'].adapter

    def test_filesystem_adapter(self):
        image = self.adapter.get_item('flask.png')
        self.assertTrue(isinstance(image, Image.Image))

        cached_image_path = self.adapter.create_cached_item('cached_image.png', image)
        self.assertEqual(cached_image_path, '/static/cache/cached_image.png')

        cached_image = self.adapter.get_cached_item('cached_image.png')
        self.assertTrue(isinstance(cached_image, Image.Image))

        self.assertTrue(self.adapter.check_cached_item('cached_image.png'))
        self.assertFalse(self.adapter.check_cached_item('flask.png'))

        self.assertTrue(self.adapter.remove_cached_item('cached_image.png'))

    def test_make_dirs_method(self):
        with self.assertRaises(Exception):
            self.adapter.make_dirs('')
