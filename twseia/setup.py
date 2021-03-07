from setuptools import setup
import __version__ as about

setup(
    name=about.__title__,
    version=about.__version__,
    description=about.__description__,
    author=about.__author__,
    author_email=about.__author_email__,
    url=about.__url__,
    license=about.__license__,
    packages=['twseia'],
    install_requires=['pyserial'],
    classifier=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
