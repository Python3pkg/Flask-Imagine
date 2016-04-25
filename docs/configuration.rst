Configuration guide
===================

.. code-block:: python
   :linenos:

    from flask import Flask
    from flask.ext.imagine import Imagine

    app = Flask(__name__)

    app.config['IMAGINE_URL'] = '/media/cache/resolve'

    app.config['IMAGINE_NAME'] = 'imagine'

    app.config['IMAGINE_CACHE_ENABLED'] = True

    app.config['IMAGINE_ADAPTERS'] = {
        'fs': ImagineFilesystemAdapter
    }

    app.config['IMAGINE_FILTERS'] = {
        'autorotate': AutorotateFilter,
        'crop': CropFilter,
        'downscale': DownscaleFilter,
        'relative_resize': RelativeResizeFilter,
        'rotate': RotateFilter,
        'thumbnail': ThumbnailFilter,
        'upscale': UpscaleFilter
    }

    app.config['IMAGINE_ADAPTER'] = {
        'name': 'fs',
        'source_folder': 'images',
        'cache_folder': 'cache'
    }

    app.config['IMAGINE_FILTER_SETS'] = {
        'filter_set_name': {
            'cache': False,
            'filters': {
                # Filters initialization parameters
            }
        }
    }
