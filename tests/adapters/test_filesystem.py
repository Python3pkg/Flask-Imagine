import os
from PIL import Image
from flask import Flask
from flask.ext.imagine import Imagine
from tests import TestCase


class TestSuccessImagineFilesystemAdapter(TestCase):
    adapter = None

    def setUp(self):
        super(TestSuccessImagineFilesystemAdapter, self).setUp()

        self.adapter = self.app.extensions['imagine'].adapter

    def test_filesystem_adapter_success(self):
        image = self.adapter.get_item('flask.png')
        self.assertTrue(isinstance(image, Image.Image))

        cached_image_path = self.adapter.create_cached_item('cached_image.png', image)
        self.assertEqual(cached_image_path, '/static/cache/cached_image.png')

        cached_image = self.adapter.get_cached_item('cached_image.png')
        self.assertTrue(isinstance(cached_image, Image.Image))

        self.assertTrue(self.adapter.check_cached_item('cached_image.png'))
        self.assertFalse(self.adapter.check_cached_item('flask.png'))

        self.assertTrue(self.adapter.remove_cached_item('cached_image.png'))

    def test_filesystem_adapter_fails(self):
        image = self.adapter.get_item('picture.png')
        self.assertFalse(isinstance(image, Image.Image))
        self.assertFalse(image)

        image = self.adapter.get_item('flask.txt')
        self.assertFalse(image)

        cached_image_path = self.adapter.create_cached_item('cached_image.png', '')
        self.assertFalse(cached_image_path)

        cached_item = self.adapter.check_cached_item('cached_image.png')
        self.assertFalse(cached_item)

    def test_make_dirs_method(self):
        with self.assertRaises(Exception):
            self.adapter.make_dirs('')

    def test_init_without_source_folder(self):
        app = Flask(__name__)
        app.root_path = os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/../'))
        app.config['TESTING'] = True
        app.config['SERVER_NAME'] = 'localhost'
        app.config['SECRET_KEY'] = 'secret secret'

        app.config['IMAGINE_ADAPTER'] = {
            'name': 'fs',
            'cache_folder': '/cache/'
        }

        with self.assertRaises(ValueError):
            Imagine(app)

    def test_init_without_cache_folder(self):
        app = Flask(__name__)
        app.root_path = os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/../'))
        app.config['TESTING'] = True
        app.config['SERVER_NAME'] = 'localhost'
        app.config['SECRET_KEY'] = 'secret secret'

        app.config['IMAGINE_ADAPTER'] = {
            'name': 'fs',
            'source_folder': '/static/'
        }

        imagine = Imagine(app)
        self.assertTrue(isinstance(imagine, Imagine))
