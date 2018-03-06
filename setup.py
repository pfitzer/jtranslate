from codecs import open
from os.path import abspath, dirname, join
from setuptools import setup, find_packages
from jootranslate import __version__, __author__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name = 'jootranslate',
    version = __version__,
    description = 'cli tool to generate translation files for joomla',
    long_description = long_description,
    url = 'https://github.com/pfitzer/jootranslate.git',
    author = __author__,
    author_email = 'michael@mp-development.de',
    license = 'MIT',
    keywords = 'joomla cli translations',
    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            'jootranslate=jootranslate.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Localization'
    ]
)