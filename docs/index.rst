.. Flask-Imagine documentation master file, created by
   sphinx-quickstart on Wed Apr 13 04:39:22 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Flask-Imagine's documentation!
=========================================

Extension which provides easy image manipulation support in Flask applications.

Installation
^^^^^^^^^^^^
::

    $ pip install Flask-Imagine

Configuration example
^^^^^^^^^^^^^^^^^^^^^
::

    from flask import Flask
    from flask.ext.imagine import Imagine

    app = Flask(__name__)

    app.config['IMAGINE_ADAPTER'] = {
        'name': 'fs',
        'source_folder': 'static',
        'cache_folder': 'cache'
    }

    app.config['IMAGINE_FILTER_SETS'] = {
        'filter_set_name': {
            'cache': True,
            'filters': {
                # Filters initialisation parameters
            }
        }
    }

Available filters:
^^^^^^^^^^^^^^^^^^

* :ref:`thumbnail_filter`
* :ref:`autorotate_filter`
* :ref:`crop_filter`
* :ref:`rotate_filter`
* :ref:`upscale_filter`
* :ref:`downscale_filter`
* :ref:`relative_resize_filter`


Indices and tables
==================

* :doc:`filters`
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
