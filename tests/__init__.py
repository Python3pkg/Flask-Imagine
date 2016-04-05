import flask
import os
import shutil
import unittest
from flask import Flask
from flask.ext.imagine import Imagine
from moto import mock_s3

flask_version = tuple(map(int, flask.__version__.split('.')))


class TestCase(unittest.TestCase):
    @mock_s3
    def setUp(self):
        self.remove_cache()
        self.app = self.create_app()
        self.app_ctx = self.app.app_context()
        self.app_ctx.push()
        self.req_ctx = self.app.test_request_context('http://localhost:8000/')
        self.req_ctx.push()
        self.client = self.app.test_client()

    def remove_cache(self):
        cache_path = os.path.abspath(os.path.dirname(__file__)) + '/assets/cache'
        shutil.rmtree(cache_path)

    @mock_s3
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['SERVER_NAME'] = 'localhost'
        app.config['SECRET_KEY'] = 'secret secret'

        app.config['IMAGINE_ADAPTER'] = {
            'name': 'fs',
            'source_folder': '/assets/',
            'cache_folder': '/cache/'
        }

        app.config['IMAGINE_FILTER_SETS'] = {
            'test_scale': {
                'filters': {
                    'thumbnail': {'size': [100, 100], 'mode': 'inset'}
                }
            }
        }
        self.images = Imagine(app)
        return app

    def assert200(self, res):
        self.assertEqual(res.status_code, 200)

    def assert302(self, res):
        self.assertEqual(res.status_code, 302)
