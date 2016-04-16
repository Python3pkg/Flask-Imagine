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

Google Cloud Storage
--------------------

.. note:: Need to install additional package **Flask-Imagine-GoogleAdapter**

Installation
""""""""""""

.. code-block:: shell
   :linenos:

    $ pip install Flask-Imagine-GoogleAdapter

Configuration
"""""""""""""

.. code-block:: python
   :linenos:

    from flask.ext.imagine_google_adapter import FlaskImagineGoogleCloudAdapter

    app.config['IMAGINE_ADAPTERS'] = {
        'gcs': FlaskImagineGoogleCloudAdapter
    }

    app.config['IMAGINE_ADAPTER'] = {
        'name': 'gcs',
        'client_id': 'your_client_id',
        'client_secret': 'your_client_secret',
        'bucket_name': 'your_bucket_name',
        'domain': 'domain.tld'      #  Optional. Domain name for using ASW S3 static website hosting.
        'schema': 'https'           #  Optional.
    }

Microsoft Azure BLOB
--------------------

.. note:: Need to install additional package **Flask-Imagine-AzureAdapter**

Installation
""""""""""""

.. code-block:: shell
   :linenos:

    $ pip install Flask-Imagine-AzureAdapter

Configuration
"""""""""""""

.. code-block:: python
   :linenos:

    from flask.ext.imagine_azure_adapter import FlaskImagineAzureAdapter

    app.config['IMAGINE_ADAPTERS'] = {
        'azure': FlaskImagineAzureAdapter
    }

    app.config['IMAGINE_ADAPTER'] = {
        'name': 'azure',
        'account_name': 'your_account_name',
        'account_key': 'your_account_key',
        'container_name': 'your_container_name',
        'domain': 'domain.tld'      #  Optional. Domain name for using static website hosting.
        'schema': 'https'           #  Optional.
    }

Rackspace Files
---------------

.. note:: Need to install additional package **Flask-Imagine-RackspaceAdapter**

Installation
""""""""""""

.. code-block:: shell
   :linenos:

    $ pip install Flask-Imagine-RackspaceAdapter

Configuration
"""""""""""""

.. code-block:: python
   :linenos:

    from flask.ext.imagine_rackspace_adapter import FlaskImagineRackspaceAdapter

    app.config['IMAGINE_ADAPTERS'] = {
        'rackspace': FlaskImagineRackspaceAdapter
    }

    app.config['IMAGINE_ADAPTER'] = {
        'name': 'rackspace',
        'region': 'your_region',
        'user_name': 'your_user_name',
        'api_key': 'your_api_key',
        'container_name': 'your_container_name'
    }
