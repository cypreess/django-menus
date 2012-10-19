Advanced usages
===============


DRY patterns
------------

To avoid hard-coding link patterns and keeping them DRY it is possible to use django standard ``reverse`` function.

Consider an url in urls.py::

        url(r'^news/$', TemplateView.as_view(template_name="news.html"), name='news')

it can be easily provided to menu declaration::

    def menu(context, variables):
        return [
           {   'name' : 'News',
               'class' : 'news_menu_item',
               'url' : reverse('news'),
               'match' : r'^'+ reverse('news') + r'$',
               'sub' : None,
           },

        ]

Internationalization
--------------------

django-menus support internationalization using ``ugettext``.

