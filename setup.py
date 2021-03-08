import setuptools
import twseia.__version__ as about

setuptools.setup(
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
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
