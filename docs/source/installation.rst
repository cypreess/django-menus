Installation
============

Getting a module
----------------

Grab a python module from pypi or source repository::

    pip install django-menus

or::

    pip install -r hg+https://bitbucket.org/cypreess/django-menus#egg=menus


``MENUS_CONF`` setting
----------------------

You should create  ``MENUS_CONF`` setting in your settings.py. Point it as a python import path to
a module that stores your project menus, eg.::

    MENUS_CONF = "myproject.menu"

Enabling request template context processor
-------------------------------------------

Menuing system needs to know which page is currently viewed. It reads url from ``request`` attribute of current context, therefore
you need to add proper context processor.

Django brings a ``TEMPLATE_CONTEXT_PROCESSORS`` setting variable to define any set of context processors. To avoid hard-coding the default set of ``TEMPLATE_CONTEXT_PROCESSORS`` use following code::


    from django.conf import global_settings

    TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
        'django.core.context_processors.request',

        )

