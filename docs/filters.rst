Filters
=======

Autorotate
----------

Automatically rotate image based on EXIF information

.. code-block:: python
   :linenos:

    app.config['IMAGINE_FILTER_SETS'] = {
        'filter_set_name': {
            'filters': {
                'autorotate': {}
            }
        }
    }

Crop
----
.. code-block:: python
   :linenos:

    app.config['IMAGINE_FILTER_SETS'] = {
        'filter_set_name': {
            'filters': {
                'crop': {'start': [10, 10], 'size': [100, 100]}
            }
        }
    }

Downscale
---------
.. code-block:: python
   :linenos:

    app.config['IMAGINE_FILTER_SETS'] = {
        'filter_set_name': {
            'filters': {
                'downscale': {'max': [1920, 1080]}
            }
        }
    }

Relative resize
---------------
.. code-block:: python
   :linenos:

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

Rotate
------
.. code-block:: python
   :linenos:

    app.config['IMAGINE_FILTER_SETS'] = {
        'filter_set_name': {
            'filters': {
                'rotate': {'angle': 90}
            }
        }
    }

Thumbnail
---------
.. code-block:: python
   :linenos:

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

Upscale
-------
.. code-block:: python
   :linenos:

    app.config['IMAGINE_FILTER_SETS'] = {
        'filter_set_name': {
            'filters': {
                'upscale': {'min': [800, 600]}
            }
        }
    }

Watermark
---------
.. code-block:: python
   :linenos:

    app.config['IMAGINE_FILTER_SETS'] = {
        'filter_set_name': {
            'filters': {
                'watermark': {
                    # Relative to 'static' folder
                    'image': 'images/watermark.png',
                    # Size of the watermark relative to the origin images size (between 0 and 1)
                    'size': 0.5,
                    # Position: One of top_left, top, top_right, left, center, right, bottom_left, bottom, bottom_right
                    'position': 'center',
                    # The watermark opacity (between 0 and 1), default: 0.3
                    'opacity': 0.3
                }
            }
        }
    }
