=====
Usage
=====

To use crm-push in a project, add it to your `INSTALLED_APPS`:

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
