Building menus
==============

First of all you should make a file that is pointed by setting ``MENUS_CONF``. You will put your
menus code there.

.. note::

    By the convention use just ``menu.py`` in root project structure (on the ``settings.py`` level).



Static menu
-----------

The most simple and fast type of menu is a static menu. This is just a list that is declared in global scope of file named after
``MENUS_CONF``.
::

    # In menu.py file

    static_menu = [
            {   'name' : 'Test 1',
                'class' : 'test_1',
                'url' : 'test1/',
                'match' : r'^test1/$',
                'sub' : None,
            },
            {   'name' : 'Test 2',
                'class' : 'test_2',
                'url' : 'test2/',
                'match' : r'^test2/$',
                'sub' : None,
            },

    ]

.. warning::

    In static menu you cannot use ``reverse()`` function for dry links.


Dynamic menu
------------

Menu can be also represented by any callable. The simplest is using a function::

        # In menu.py file

        def menu(context, variables):
            return [
               {   'name' : 'News',
                   'class' : 'news_menu_item',
                   'url' : reverse('news'),
                   'match' : r'^'+ reverse('news') + r'$',
                   'sub' : None,
               },

            ]

this allows to use some additional information like template context.