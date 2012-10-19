Using menus in templates
========================

django-menus provides only one template tag.

Loading template tags
---------------------

Remember to load ``menus`` in every template you use menuing.
::

    {% load menus %}

``get_menu`` template tag
-------------------------
The template tag has following syntax::

    {% get_menu MENU_NAME [as VARIABLE_NAME] [with VAR1=VAL1 VAR2=VAL2] %}

It propagates a menu data structure to the ``VARIABLE_NAME``.

.. note::

    If ``VARIABLE_NAME`` is omitted ``MENU_NAME`` is used.


Accessing and displaying menus
------------------------------

django-menus support multilevel  menus