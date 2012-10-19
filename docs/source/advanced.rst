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

.. note::

    Attribute ``match`` can be omitted in most cases. It defaults to `` r'^'+ url + r'$',``. This is extremely helpful
    in simple cases where exact match is what you want for menu element selection.




Internationalization
--------------------

django-menus support internationalization using django ``ugettext``.

::

    from django.utils.translation import ugettext_lazy as _

    def menu(context, variables):
        return [
           {   'name' : _('News'),
               'class' : 'news_menu_item',
               'url' : reverse('news'),
           },

        ]
