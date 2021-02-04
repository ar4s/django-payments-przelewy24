=====
Usage
=====

To use django-payments-przelewy24 in a project, add it to your `INSTALLED_APPS`:

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


TODO
