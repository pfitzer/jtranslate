from setuptools import setup, find_packages
from jootranslate import __version__, __author__

setup(
    name='jootranslate',
    version=__version__,
    description='cli tool to generate translation files for joomla',
    long_description_markdown_filename='README.md',
    url='https://github.com/pfitzer/jtranslate.git',
    author=__author__,
    author_email='michael@mp-development.de',
    license='MIT',
    keywords='joomla cli translations',
    setup_requires=['pytest-runner', 'setuptools-markdown'],
    tests_require=['pytest'],
    extras_require={
        'docs': [
            'sphinx >= 1.7.1',
            'sphinx_rtd_theme']
    },
    packages=find_packages(),
    entry_points={
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
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Localization'
    ]
)
