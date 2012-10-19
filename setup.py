import os

from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
    
setup(
    name = "menus",
    version = "1.0",
    author = "Krzysztof Dorosz",
    author_email = "cypreess@gmail.com",
    description = ("Django menuing system"),
    license = "MIT",
    packages = [    'menus',
                    'menus.templatetags',
    ],
    install_requires = [
                        'django>=1.1',
                        ],
)