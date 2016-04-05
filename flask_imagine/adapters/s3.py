"""
This module implement a Amazon AWS S3 storage adapter.
"""
import boto
from .interface import ImagineAdapterInterface


class ImagineS3Adapter(ImagineAdapterInterface):
    """
    Amazon AWS S3 storage adapter
    """
    s3_conn = None
    bucket = None

    def __init__(self, access_key, secret_key, bucket_name):
        """
        Init adapter
        :param access_key: str
        :param secret_key: str
        :param bucket_name: str
        """
        self.s3_conn = boto.connect_s3(access_key, secret_key)
        self.bucket = self.s3_conn.create_bucket(bucket_name)

    def get_item(self, path):
        """
        Get resource item
        :param path: string
        :return: Image
        """
        item = self.bucket.get_key(path)

        return item.get_contents_as_string()
