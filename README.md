[![](https://img.shields.io/pypi/v/jootranslate.svg)](https://pypi.python.org/pypi?name=jootranslate&:action=display)  [![](https://travis-ci.org/pfitzer/jtranslate.svg?branch=master)](https://travis-ci.org/pfitzer/jtranslate) [![](https://pyup.io/repos/github/pfitzer/jtranslate/shield.svg?t=1520427395490)](https://pyup.io/account/repos/github/pfitzer/jtranslate/) [![Python 3](https://pyup.io/repos/github/pfitzer/jtranslate/python-3-shield.svg)](https://pyup.io/repos/github/pfitzer/jtranslate/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/jootranslate.svg)](https://pypi.python.org/pypi?name=jootranslate&:action=display) [![Documentation Status](https://readthedocs.org/projects/jootranslate/badge/?version=latest)](http://jootranslate.readthedocs.io/?badge=latest)


## jootranslate
Searches for JText::_ translations in php and label|description in xml files and generates the ini files. If the file exist only new translation strings will
be added. Your translation strings have to start with COM_COMPONENTNAME to get accepted.

This is just a little helper so you don`t have to copy and paste all your translation strings by hand.

Your component needs the following directory structure

    admin
        - components
            - com_COMPONENTNAME
                - controllers
                - language
                - etc ...
    site
        - com_COMPONENTNAME
            - controllers
            - language
            - etc...
            
**new in v0.4.0**

You can now translate directly on console it you want. Jootranslate now uses configobj to read and write the ini files so you
have to make some changes to yout existing translation files.

Joomla normaly use translations like this

    COM_TEST_KEEPME="translated"
    
    but we need it in this format
    
    COM_TEST_KEEPME = 'translated'
    
    This is working in joomla too, so don`t worry. Please take a look on your existing files, otherwise allready translated
    strings will be lost!

**installation**

    with pip

    pip install --user --upgrade jootranslate

    local

    python setup.py install

**usage**


    jootranslate --source /path/to/component/root --com your_component
    
    if yout want translate on the fly add -t
    
    jootranslate -t --source /path/to/component/root --com your_component

    to see a full list of all options

    jootranslate -h

**todo**

Generate the *.sys.ini files
