=============================
crm-push
=============================

.. image:: https://badge.fury.io/py/crm-push.svg
    :target: https://badge.fury.io/py/crm-push

.. image:: https://travis-ci.org/dcopm999/crm-push.svg?branch=master
    :target: https://travis-ci.org/dcopm999/crm-push

.. image:: https://codecov.io/gh/dcopm999/crm-push/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dcopm999/crm-push

PUSH Application

Documentation
-------------

The full documentation is at https://crm-push.readthedocs.io.

Quickstart
----------

Install crm-push::

    pip install crm-push

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'push.apps.PushConfig',
        ...
    )

Add crm-push's URL patterns:

.. code-block:: python

    from push import urls as push_urls


    urlpatterns = [
        ...
        url(r'^', include(push_urls)),
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

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
