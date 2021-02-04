=============================
django-payments-przelewy24
=============================

.. image:: https://badge.fury.io/py/django-payments-przelewy24.svg
    :target: https://badge.fury.io/py/django-payments-przelewy24

.. image:: https://travis-ci.org/ar4s/django-payments-przelewy24.svg?branch=master
    :target: https://travis-ci.org/ar4s/django-payments-przelewy24

.. image:: https://codecov.io/gh/ar4s/django-payments-przelewy24/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/ar4s/django-payments-przelewy24

Your project description goes here

Documentation
-------------

The full documentation is at https://django-payments-przelewy24.readthedocs.io.

Quickstart
----------

Install django-payments-przelewy24::

    pip install django-payments-przelewy24

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'payments_przelewy24.apps.DjangoPaymentsPrzelewy24Config',
        ...
    )

Add django-payments-przelewy24's URL patterns:

.. code-block:: python

    from payments_przelewy24 import urls as payments_przelewy24_urls


    urlpatterns = [
        ...
        url(r'^', include(payments_przelewy24_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
