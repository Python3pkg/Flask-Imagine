Filters
=======

.. _autorotate_filter:

Autorotate
----------

Automatically rotate image based on EXIF information
::

    app.config['IMAGINE_FILTER_SETS'] = {
        'filter_set_name': {
            'filters': {
                'autorotate': {}
            }
        }
    }

.. _crop_filter:

Crop
----
::

    app.config['IMAGINE_FILTER_SETS'] = {
        'filter_set_name': {
            'filters': {
                'crop': {'start': [10, 10], 'size': [100, 100]}
            }
        }
    }

.. _downscale_filter:

Downscale
---------
::

    app.config['IMAGINE_FILTER_SETS'] = {
        'filter_set_name': {
            'filters': {
                'downscale': {'max': [1920, 1080]}
            }
        }
    }

.. _relative_resize_filter:

Relative resize
---------------
::

    app.config['IMAGINE_FILTER_SETS'] = {
        'my_heighten': {
            'filters': {
                'relative_resize': {'heighten': 60}
            }
        },
        'my_widen': {
            'filters': {
                'relative_resize': {'widen': 32}
            }
        },
        'my_increase': {
            'filters': {
                'relative_resize': {'increase': 10}
            }
        },
        'my_decrease': {
            'filters': {
                'relative_resize': {'decrease': 10}
            }
        },
        'my_scale': {
            'filters': {
                'relative_resize': {'scale': 2.5}
            }
        }
    }

.. _rotate_filter:

Rotate
------
::

    app.config['IMAGINE_FILTER_SETS'] = {
        'filter_set_name': {
            'filters': {
                'rotate': {'angle': 90}
            }
        }
    }

.. _thumbnail_filter:

Thumbnail
---------
::

    app.config['IMAGINE_FILTER_SETS'] = {
        'thumb_in': {
            'filters': {
                'thumbnail': {'size': [32, 32], 'mode': 'inset'}
            }
        },
        'thumb_out': {
            'filters': {
                'thumbnail': {'size': [32, 32], 'mode': 'outbound'}
            }
        }
    }

.. _upscale_filter:

Upscale
-------
::

    app.config['IMAGINE_FILTER_SETS'] = {
        'filter_set_name': {
            'filters': {
                'upscale': {'min': [800, 600]}
            }
        }
    }
