"""
This module implement a Relative resize filter.
"""
from .interface import ImagineFilterInterface
from PIL import Image


class RelativeResizeFilter(ImagineFilterInterface):
    """
    Relative resize filter
    """
    methods = ['heighten', 'widen', 'increase', 'scale']
    method = None
    value = None

    def __init__(self, method, value):
        """
        :param method: str
        :param value: int or float
        """
        if method in self.methods:
            self.method = method
        else:
            raise ValueError('Unknown method: %s' % method)

        if self.method == 'scale':
            try:
                self.value = float(value)
            except Exception, e:
                raise ValueError('Wrong value type: %s' % unicode(e))
        else:
            try:
                self.value = int(value)
            except Exception, e:
                raise ValueError('Wrong value type: %s' % unicode(e))

    def apply(self, resource):
        """
        :param resource: Image
        :return: Image
        """
        if isinstance(resource, Image.Image):
            return getattr(self, '_' + self.method)(resource)
        else:
            raise ValueError('Unsupported resource format: %s' % str(type(resource)))

    def _heighten(self, resource):
        """
        Change image size by height
        :param resource: Image
        :return: Image
        """
        original_width, original_height = resource.size

        target_height = self.value
        target_width = (target_height / original_height) * original_width

        resource = resource.resize((target_width, target_height), Image.ANTIALIAS)

        return resource

    def _widen(self, resource):
        """
        Change image size by width
        :param resource: Image
        :return: Image
        """
        original_width, original_height = resource.size

        target_width = self.value
        target_height = (target_width / original_width) * original_height

        resource = resource.resize((target_width, target_height), Image.ANTIALIAS)

        return resource

    def _increase(self, resource):
        """
        Increase image size
        :param resource: Image
        :return: Image
        """
        original_width, original_height = resource.size

        target_width = original_width + self.value
        target_height = original_height + self.value

        resource = resource.resize((target_width, target_height), Image.ANTIALIAS)

        return resource

    def _scale(self, resource):
        """
        Scale image
        :param resource: Image
        :return: Image
        """
        original_width, original_height = resource.size

        target_width = int(round(original_width * self.value))
        target_height = int(round(original_height * self.value))

        resource = resource.resize((target_width, target_height), Image.ANTIALIAS)

        return resource
