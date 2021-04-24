=============================
django-payments-przelewy24
=============================

.. image:: https://img.shields.io/pypi/v/django-payments-przelewy24
    :target: https://pypi.org/project/django-payments-przelewy24/

.. image:: https://circleci.com/gh/ar4s/django-payments-przelewy24.svg?style=shield
    :target: https://circleci.com/gh/ar4s/django-payments-przelewy24


Your project description goes here


Quickstart
----------

Install django-payments-przelewy24::

    pip install django-payments-przelewy24

Add it to your `INSTALLED_APPS`:

.. code-block:: python
    
    from payments_przelewy24.config import Przelewy24Config

    PAYMENT_VARIANTS = {
        "przelewy24": (
            "payments_przelewy24.provider.Przelewy24Provider",
            {
                "config": Przelewy24Config(
                    pos_id=123,
                    merchant_id=123,
                    crc="e34a1",
                    api_key="d876a3ba780cb",
                    sandbox=True
                ),
            },
        ),
    }

You can also use environment to configure provider:

.. code-block:: python
    
    from payments_przelewy24.config import Przelewy24Config
    
    # PAYMENTS_P24_POS_ID=123
    # PAYMENTS_P24_MERCHANT_ID=123
    # PAYMENTS_P24_CRC=e34a1
    # PAYMENTS_P24_API_KEY=d876a3ba780cb
    # PAYMENTS_P24_SANDBOX=1

    PAYMENT_VARIANTS = {
        "przelewy24": (
            "payments_przelewy24.provider.Przelewy24Provider",
            {
                "config": Przelewy24Config.from_env(),
            },
        ),
    }


Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements_test.txt
    (myenv) $ pytest


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Documentation
-------------

* Przelewy24 REST API_


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
.. _API: https://developers.przelewy24.pl/index.php
