import os
import shutil

from PIL import Image
from flask import Flask
from flask.ext.imagine import Imagine
from tests import TestCase


class TestImagineFilesystemAdapter(TestCase):
    app = None
    app_ctx = None
    client = None
    adapter = None

    def setUp(self):
        self.remove_cache()
        self.app = self.create_app()
        self.app_ctx = self.app.app_context()
        self.app_ctx.push()
        self.req_ctx = self.app.test_request_context('http://localhost:8000/')
        self.req_ctx.push()
        self.client = self.app.test_client()

        self.adapter = self.app.extensions['imagine'].adapter

    def tearDown(self):
        self.app = None
        self.remove_cache()

    def remove_cache(self):
        cache_path = os.path.abspath(os.path.dirname(__file__)) + '/../static/cache'
        if os.path.exists(cache_path):
            shutil.rmtree(cache_path)

    def create_app(self):
        app = Flask(__name__)
        app.root_path = os.path.abspath(os.path.normpath(os.path.dirname(__file__) + '/../'))
        app.config['TESTING'] = True
        app.config['SERVER_NAME'] = 'localhost'
        app.config['SECRET_KEY'] = 'secret secret'

        app.config['IMAGINE_ADAPTER'] = {
            'name': 'fs',
            'source_folder': '/static/',
            'cache_folder': '/cache/'
        }

        self.images = Imagine(app)
        return app

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
