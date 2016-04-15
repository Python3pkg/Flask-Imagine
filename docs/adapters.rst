Storage adapters
================

Filesystem
----------

.. note:: Built-in by default

.. code-block:: python
   :linenos:

    app.config['IMAGINE_ADAPTER'] = {
        'name': 'fs',
        'source_folder': 'images',  #  Relative to 'static' folder.
        'cache_folder': 'cache'     #  Optional. Default: 'cache'.
    }

Amazon AWS S3
-------------

.. note:: Need to install additional package **Flask-Imagine-S3Adapter**

Installation
""""""""""""

.. code-block:: shell
   :linenos:

    $ pip install Flask-Imagine-S3Adapter

Configuration
"""""""""""""

.. code-block:: python
   :linenos:

    from flask.ext.imagine_s3_adapter import FlaskImagineS3Adapter

    app.config['IMAGINE_ADAPTERS'] = {
        's3': FlaskImagineS3Adapter
    }

    app.config['IMAGINE_ADAPTER'] = {
        'name': 's3',
        'access_key': 'your_access_key',
        'secret_key': 'your_secret_key',
        'bucket_name': 'your_bucket_name',
        'domain': 'domain.tld'      #  Optional. Domain name for using ASW S3 static website hosting.
        'schema': 'https'           #  Optional.
    }
