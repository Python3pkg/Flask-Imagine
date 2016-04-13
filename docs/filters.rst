Built-in Filters
================

Autorotate
----------

It rotates the image automatically to display it as correctly as possible. The rotation to apply is obtained through the metadata stored in the EXIF data of the original image. This filter provides no configuration options:

.. code-block:: python
   :linenos:

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

It performs a crop transformation on your image. The start option defines the coordinates of the left-top pixel where the crop begins (the [0, 0] coordinates correspond to the top leftmost pixel of the original image). The size option defines in pixels the width and height (in this order) of the area cropped:

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

It performs a downscale transformation on your image to reduce its size to the given dimensions:

.. code-block:: python
   :linenos:

    app.config['IMAGINE_FILTER_SETS'] = {
        'filter_set_name': {
            'filters': {
                'downscale': {'max': [1920, 1080]}
            }
        }
    }

A smaller image will be left as it.

Relative resize
---------------

The relative_resize filter may be used to heighten, widen, increase or scale an image with respect to its existing dimensions.

.. code-block:: python
   :linenos:

    app.config['IMAGINE_FILTER_SETS'] = {
        'my_heighten': {
            'filters': {
                'relative_resize': {'heighten': 60} #  Transforms 50x40 to 75x60
            }
        },
        'my_widen': {
            'filters': {
                'relative_resize': {'widen': 32}    #  Transforms 50x40 to 32x26
            }
        },
        'my_increase': {
            'filters': {
                'relative_resize': {'increase': 10} #  Transforms 50x40 to 60x50
            }
        },
        'my_decrease': {
            'filters': {
                'relative_resize': {'decrease': 10} #  Transforms 50x40 to 40x30
            }
        },
        'my_scale': {
            'filters': {
                'relative_resize': {'scale': 2.5}   #  Transforms 50x40 to 125x100
            }
        }
    }

Rotate
------

It rotates the image based on specified **angle** (in degrees). The value of the angle configuration option must be a positive integer or float number:

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

The thumbnail filter, as the name implies, performs a thumbnail transformation on your image.

The mode can be either outbound or inset. Option inset does a relative resize, where the height and the width will not exceed the values in the configuration. Option outbound does a relative resize, but the image gets cropped if width and height are not the same.

Given an input image sized 50x40 (width x height), consider the following annotated configuration examples:

.. code-block:: python
   :linenos:

    app.config['IMAGINE_FILTER_SETS'] = {
        'thumb_in': {
            'filters': {
                # Transforms 50x40 to 32x26, no cropping
                'thumbnail': {'size': [32, 32], 'mode': 'inset'}
            }
        },
        'thumb_out': {
            'filters': {
                # Transforms 50x40 to 32x32, while cropping the width
                'thumbnail': {'size': [32, 32], 'mode': 'outbound'}
            }
        }
    }

A smaller image will be left as it. This means you may get images that are smaller than the specified dimensions.

Upscale
-------

It performs an upscale transformation on your image to increase its size to the given dimensions:

.. code-block:: python
   :linenos:

    app.config['IMAGINE_FILTER_SETS'] = {
        'filter_set_name': {
            'filters': {
                'upscale': {'min': [800, 600]}
            }
        }
    }

A biggest image will be left as it.

Watermark
---------

The watermark filter pastes a second image onto your image while keeping its ratio. Configuration looks like this:

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

.. important:: Please note that position of watermark filter is important. If you have some filters like :ref:`crop_filter` after it is possible that watermark image will be **cropped**.
