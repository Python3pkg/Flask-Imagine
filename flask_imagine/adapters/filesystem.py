import errno
import os
from flask import current_app
from .interface import ImagineAdapterInterface
from PIL import Image


class ImagineFilesystemAdapter(ImagineAdapterInterface):
    source_folder = None
    cache_folder = None

    def __init__(self, **kwargs):
        if 'source_folder' in kwargs:
            self.source_folder = kwargs.pop('source_folder').strip('/')
        else:
            raise ValueError('Folder is not set.')

        self.cache_folder = kwargs['cache_folder'].strip('/')

    def get_item(self, path):
        return Image.open('%s/%s/%s' % (current_app.root_path, self.source_folder, path.strip('/')))

    def create_cached_item(self, path, content):
        item_path = '%s/%s/%s/%s' % (current_app.root_path, self.source_folder, self.cache_folder, path.strip('/'))
        self.make_dirs(item_path)

        content.save(item_path)

        return '/%s/%s/%s' % (self.source_folder, self.cache_folder, path.strip('/'))

    def get_cached_item(self, path):
        return Image.open('%s/%s/%s/%s' % (current_app.root_path, self.source_folder, self.cache_folder, path.strip('/')))

    def check_cached_item(self, path):
        return os.path.isfile(
            '%s/%s/%s/%s' % (current_app.root_path, self.source_folder, self.cache_folder, path.strip('/'))
        )

    def remove_cached_item(self, path):
        os.remove('%s/%s/%s/%s' % (current_app.root_path, self.source_folder, self.cache_folder, path.strip('/')))

        return True

    @staticmethod
    def make_dirs(path):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
