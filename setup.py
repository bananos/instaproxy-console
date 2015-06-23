try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import instaproxy

setup(
    name='instaproxy',
    version='0.1',
    author='Andrew Druchenko',
    author_email='bananos@dev.co.ua',
    url='',
    description='A command line tool to work with InstantProxies.com service',
    long_description=open('README.rst').read(),
    entry_points={
            'console_scripts': [
                'instaproxy = instaproxy.core:main',
            ],
        },
    packages=['instaproxy'],
    license="Apache 2.0",
    keywords='instantproxies.com proxy console cli',
    install_requires=['requests>=2.3.0'],
    classifiers = [ 'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
        'Topic :: System :: Networking',
        'Topic :: Terminals',
        'Topic :: Text Processing',
        'Topic :: Utilities']
)
