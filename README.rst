==============
combinePatches
==============


.. image:: https://img.shields.io/pypi/v/combinepatches.svg
        :target: https://pypi.python.org/pypi/combinepatches

.. image:: https://img.shields.io/travis/AZjk/combinepatches.svg
        :target: https://travis-ci.com/AZjk/combinepatches

.. image:: https://readthedocs.org/projects/combinepatches/badge/?version=latest
        :target: https://combinepatches.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




A package that combines images obtained with an area detector at different positions.


* Free software: MIT license
* Documentation: https://combinepatches.readthedocs.io.


Usage
--------
.. code-block:: python
    
    images = [np.ones((100, 100)) for _ in range(100)]
    pixel_size = 75E-3  # typical pixel size for Eiger detectors 75um
    positions = list(np.random.randint(-10, 10, size=(100, 2)) * pixel_size)
    a = combine_patches(images, positions, pixel_size)


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
