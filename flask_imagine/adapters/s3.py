import boto
from .interface import ImagineAdapterInterface


class ImagineS3Adapter(ImagineAdapterInterface):
    s3_conn = None
    bucket = None

    def __init__(self, access_key, secret_key, bucket_name):
        self.s3_conn = boto.connect_s3(access_key, secret_key)
        self.bucket = self.s3_conn.create_bucket(bucket_name)

    def create_item(self, path, content):
        item = self.bucket.new_key(path)
        item.set_contents_from_string(content)
        item.make_public()

        return True

    def get_item(self, path):
        item = self.bucket.get_key(path)

        return item.get_contents_as_string()

    def remove_item(self, path):
        self.bucket.delete_key(path)

        return True
