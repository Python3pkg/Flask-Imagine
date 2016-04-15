Load your Custom Storage Adapters
=================================

The Flask-Imagine allows you to load your own custom storage adapter classes. The only requirement is that each adapter implements the following interface:

.. code-block:: python
   :linenos:

    from flask.ext.imagine.adapters.interface import ImagineAdapterInterface

    class MyCustomStorageAdapter(ImagineAdapterInterface):
        configuration_parameter = None

        def __init__(self, configuration_parameter, **kwargs):
            self.configuration_parameter = configuration_parameter

        def get_item(self, path):
            """Get original image"""
            return PIL.Image

        def create_cached_item(self, path, content):
            """Create cached resource item"""
            return str(web_path_to_resource)

        def get_cached_item(self, path):
            """Get cached resource item"""
            return PIL.Image

        def check_cached_item(self, path):
            """Check for cached resource item exists"""
            return bool()

        def remove_cached_item(self, path):
            """Remove cached resource item"""
            return bool()

You can now reference and use your custom storage adapter in your configuration:

.. code-block:: python
   :linenos:

    app.config['IMAGINE_ADAPTERS'] = {
        'my_custom_adapter': MyCustomStorageAdapter
    }

    app.config['IMAGINE_ADAPTER'] = {
        'name': 'my_custom_adapter',
        'configuration_parameter': 'configuration_parameter_value'
    }
