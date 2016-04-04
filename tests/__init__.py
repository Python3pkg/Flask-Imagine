from moto import mock_s3
import unittest
from flask import Flask
import flask
from flask.ext.imagine import Imagine

flask_version = tuple(map(int, flask.__version__.split('.')))


class TestCase(unittest.TestCase):
    @mock_s3
    def setUp(self):
        self.app = self.create_app()
        self.app_ctx = self.app.app_context()
        self.app_ctx.push()
        self.req_ctx = self.app.test_request_context('http://localhost:8000/')
        self.req_ctx.push()
        self.client = self.app.test_client()

    @mock_s3
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['SERVER_NAME'] = 'localhost'
        app.config['SECRET_KEY'] = 'secret secret'
        app.config['IMAGINE_S3_ACCESS_KEY'] = 'access_key'
        app.config['IMAGINE_S3_SECRET_KEY'] = 'secret_key'
        app.config['IMAGINE_S3_BUCKET'] = 'bucket'
        app.config['IMAGINE_FILTERS'] = {
            'test_scale': {
                'filter': 'scale',
                'width': 105,
                'height': 65
            }
        }
        self.images = Imagine(app)
        return app

    def assert200(self, res):
        self.assertEqual(res.status_code, 200)
