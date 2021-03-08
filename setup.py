import setuptools
import re

about = {}
with open('twseia/__version__.py') as fh:
    for line in fh.readlines():
        about.update(dict(re.findall('__([a-z]+)__ *= *\'([^"]+)\'', line)))

with open('README.rst', 'r') as f:
    readme = f.read()

setuptools.setup(
    name=about.get('title'),
    version=about.get('version'),
    description=about.get('description'),
    long_description=readme,
    long_description_content_type='text/x-rst',
    author=about.get('author'),
    author_email=about.get('author_email'),
    url=about.get('url'),
    license=about.get('license'),
    packages=['twseia'],
    install_requires=['pyserial'],
    classifier=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
