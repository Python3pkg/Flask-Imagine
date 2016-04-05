class ImagineAdapterInterface(object):
    def get_item(self, path):
        raise NotImplementedError()

    def create_cached_item(self, path, content):
        raise NotImplementedError()

    def get_cached_item(self, path):
        raise NotImplementedError()

    def check_cached_item(self, path):
        raise NotImplementedError()

    def remove_cached_item(self, path):
        raise NotImplementedError()
