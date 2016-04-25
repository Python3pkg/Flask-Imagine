Getting started
===============

Installation
------------
.. code-block:: bash
   :linenos:

    $ pip install Flask-Imagine


Configuration example
---------------------
.. code-block:: python
   :linenos:

    from flask import Flask
    from flask.ext.imagine import Imagine

    app = Flask(__name__)

    app.config['IMAGINE_ADAPTER'] = {
        'name': 'fs',
        'source_folder': 'images',
        'cache_folder': 'cache'
    }

    app.config['IMAGINE_FILTER_SETS'] = {
        'filter_set_name': {
            'cache': True,
            'filters': {
                # Filters initialization parameters
            }
        }
    }

Dynamic filter sets configuration
---------------------------------
.. code-block:: python
   :linenos:

    from flask import Flask
    from flask.ext.imagine import Imagine

    app = Flask(__name__)

    app.config['IMAGINE_ADAPTER'] = {
        'name': 'fs',
        'source_folder': 'images',
        'cache_folder': 'cache'
    }

    imagine = Imagine(app)

    # Add filter set
    imagine.add_filter_set(
        'filter_set_name',
        [
            Filter(parameter='value')  # List of preconfigured filters
        ],
        cached=True
    )

    # Update existing filter set
    imagine.update_filter_set(
        'filter_set_name',
        [
            NewFilter(parameter='value')  # List of preconfigured filters
        ],
        cached=False
    )

    # Remove existing filter set
    imagine.remove_filter_set('filter_set_name')
