import flask
import os
import shutil
import unittest
from flask import Flask
from flask.ext.imagine import Imagine

flask_version = tuple(map(int, flask.__version__.split('.')))


class TestCase(unittest.TestCase):
    def setUp(self):
        self.remove_cache()
        self.app = self.create_app()
        self.app_ctx = self.app.app_context()
        self.app_ctx.push()
        self.req_ctx = self.app.test_request_context('http://localhost:8000/')
        self.req_ctx.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app = None
        self.remove_cache()

    def remove_cache(self):
        cache_path = os.path.abspath(os.path.dirname(__file__)) + '/static/cache'
        if os.path.exists(cache_path):
            shutil.rmtree(cache_path)

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['SERVER_NAME'] = 'localhost'
        app.config['SECRET_KEY'] = 'secret secret'

        app.config['IMAGINE_ADAPTER'] = {
            'name': 'fs',
        }

        app.config['IMAGINE_FILTER_SETS'] = {
            'test_scale_cached': {
                'cached': True,
                'filters': {
                    'thumbnail': {'size': [100, 100], 'mode': 'inset'}
                }
            },
            'test_scale_dynamic': {
                'cached': False,
                'filters': {
                    'thumbnail': {'size': [100, 100], 'mode': 'inset'}
                }
            }
        }
        self.imagine = Imagine(app)
        return app

    def assert200(self, res):
        self.assertEqual(res.status_code, 200)

    def assert302(self, res):
        self.assertEqual(res.status_code, 302)

    def assert404(self, res):
        self.assertEqual(res.status_code, 404)
