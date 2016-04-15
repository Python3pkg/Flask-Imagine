Load your Custom Filters
========================

The Flask-Imagine allows you to load your own custom filter classes. The only requirement is that each filter loader implements the following interface:

.. code-block:: python
   :linenos:

    from flask.ext.imagine.filters.interface import ImagineFilterInterface

    class MyCustomFilter(ImagineFilterInterface):
        configuration_parameter = None

        def __init__(self, configuration_parameter, **kwargs):
            self.configuration_parameter = configuration_parameter

        def apply(self, resource):
            # Some adjustments

            return resource

You can now reference and use your custom filter when defining filter sets you'd like to apply in your configuration:

.. code-block:: python
   :linenos:

    app.config['IMAGINE_FILTERS'] = {
        'my_custom_filter': MyCustomFilter
    }

    app.config['IMAGINE_FILTER_SETS'] = {
        'filter_set_name': {
            'filters': {
                'my_custom_filter': {'configuration_parameter': 'configuration_parameter_value'}
            }
        }
    }
