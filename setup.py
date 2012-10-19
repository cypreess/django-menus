import os

from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
    
setup(
    name = "menus",
    version = "0.0.1",
    author = "Krzysztof Dorosz",
    author_email = "cypreess@gmail.com",
    description = ("Django menuing system"),
    license = "MIT",
    packages = ['menus',],
    install_requires = [
                        'django>=1.1',
                        ],
)