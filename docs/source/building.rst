Building menus
==============

First of all you should make a file that is pointed by setting ``MENUS_CONF``. You will put your
menus code there.

Static menu
-----------

The most simple and fast type of menu is a static menu. This is just a list that is declared in global scope of
``MENUS_CONF``.
::

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
