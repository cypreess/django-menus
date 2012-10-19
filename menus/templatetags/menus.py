from django.core.exceptions import ImproperlyConfigured
from django.template import Library, Node, TemplateSyntaxError, Variable
from django.template.base import VariableDoesNotExist
from django.conf import settings
import re
import sys

register = Library()



def match_path(match, path):
    if re.search(match, path):
        return True
    else:
        return False

class Menus(Node):
    def __init__(self, menu_name, menu_variable, variables={}):
        self.menu_variable = menu_variable
        self.menu_name = menu_name
        try:
            MENUS_CONF = getattr(settings, 'MENUS_CONF')
        except AttributeError:
            raise ImproperlyConfigured('Menus application requires configuring MENUS_CONF setting.')
        __import__(MENUS_CONF)
        self.project_menus =  sys.modules[MENUS_CONF]


        self.variables = {}
        for object in variables:
            self.variables[object] = Variable(variables[object])


    def render(self, context):
        objects = {}
        for object in self.variables:
            try:
                objects[object] = self.variables[object].resolve(context)
            except VariableDoesNotExist, e:
                objects[object] = str(self.variables[object])
        level = getattr(self.project_menus, self.menu_name)
        if hasattr(level, '__call__'):
            level = level(context, objects)
        context[self.menu_variable] = self.get_menu_level(level, context)
        return ''

    def get_menu_level(self, level, context):
        sub_node = None
        for node in level:
            if not node.has_key('match') or node['match'] is None:
                node['match'] = r'^' + node['url'] + r'$'
            node['selected'] = match_path(node['match'], context['request'].path)
            if node['selected'] and node.has_key('sub'):
                sub_node = node['sub']

        if sub_node :
            return [level, ] + self.get_menu_level(sub_node, context)
        else:
            return [level]

    @classmethod
    def tag(cls, parser, token):
        bits = list(token.split_contents())
        tag_name = bits.pop(0)
        menu_name = bits.pop(0)
        menu_variable = menu_name
        variables = {}
        if bits:
            bit = bits.pop(0)
            if bit == 'as':
                try:
                    menu_variable = bits.pop(0)
                except IndexError:
                    raise TemplateSyntaxError("%r tag requires a variable name after 'as' statement" % tag_name)
                bit = None
                try:
                    bit = bits.pop(0)
                except IndexError:
                    pass

            if bit == 'with':
                while 1 :
                    try:
                        bit = bits.pop(0)
                    except IndexError:
                        break
                    try:
                        variable_name, variable_value = bit.split('=')
                        variables[variable_name] = variable_value
                    except:
                        raise TemplateSyntaxError("%r tag requires a name=value pairs after 'with' statement" % tag_name)
            elif bit is not None:
                raise TemplateSyntaxError("%r tag syntax error, 'as' or 'with' expected." % tag_name)
        return cls(menu_name, menu_variable, variables)

get_menu = register.tag('get_menu', Menus.tag)
