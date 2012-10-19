from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.template.base import TemplateSyntaxError
from django.test import TestCase
from menus.templatetags.menus import Menus
from mock import Mock, patch


class MenusTest(TestCase):


    def setUp(self):
        super(MenusTest, self).setUp()
        settings.MENUS_CONF = 'menus.menu'


    @patch('django.template.Variable')
    def test_static(self, Variable):

        parser = Mock()
        token = Mock(methods=['split_contents'])
        token.split_contents.return_value = ('get_menu', 'static_menu')
        Menus.tag(parser, token)


    @patch('django.template.Variable')
    def test_no_settings(self, Variable):
        del settings.MENUS_CONF
        parser = Mock()
        token = Mock(methods=['split_contents'])
        token.split_contents.return_value = ('get_menu', 'static_menu')
        self.assertRaises(ImproperlyConfigured, Menus.tag, parser, token)

    @patch('django.template.Variable')
    def test_syntax_2(self, Variable):
        parser = Mock()
        token = Mock(methods=['split_contents'])
        token.split_contents.return_value = ('get_menu', 'test', '1', '2')

        self.assertRaises(TemplateSyntaxError, Menus.tag, parser, token)

    @patch('django.template.Variable')
    def test_syntax_3(self, Variable):
        parser = Mock()
        token = Mock(methods=['split_contents'])
        token.split_contents.return_value = ('get_menu', 'test', 'as')

        self.assertRaises(TemplateSyntaxError, Menus.tag, parser, token)

    @patch('django.template.Variable')
    def test_syntax_4(self, Variable):
        parser = Mock()
        token = Mock(methods=['split_contents'])
        token.split_contents.return_value = ('get_menu', 'test', 'with', '12345')

        self.assertRaises(TemplateSyntaxError, Menus.tag, parser, token)

    @patch('django.template.Variable')
    def test_syntax_5(self, Variable):
        parser = Mock()
        token = Mock(methods=['split_contents'])
        token.split_contents.return_value = ('get_menu', 'test', 'as' 'test', 'test', 'with', '12345')

        self.assertRaises(TemplateSyntaxError, Menus.tag, parser, token)