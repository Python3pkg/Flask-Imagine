Adapters
========

Filesystem
----------

.. code-block:: python
   :linenos:

    app.config['IMAGINE_ADAPTER'] = {
        'name': 'fs',
        'source_folder': 'static',
        'cache_folder': 'cache'
    }
