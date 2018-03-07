[![](https://img.shields.io/pypi/v/jootranslate.svg)](https://pypi.python.org/pypi?name=jootranslate&:action=display)  [![](https://travis-ci.org/pfitzer/jtranslate.svg?branch=master)](https://travis-ci.org/pfitzer/jtranslate) [![](https://pyup.io/repos/github/pfitzer/jtranslate/shield.svg?t=1520427395490)](https://pyup.io/account/repos/github/pfitzer/jtranslate/) ![](https://pyup.io/repos/github/pfitzer/jtranslate/python-3-shield.svg?t=1520427395491)

## jootranslate
search for JText translations in php files and generates the ini files. If the file exist only new translation strings will
be added.

Your component needs the following directory structure

    administrator
        - components
            - com_COMPONENTNAME
            - controllers
            - language
            - etc ...
    components
        - com_COMPONENTNAME
            - controllers
            - language
            - etc...

**installation**

use pip

    pip install jootranslate

local

    python setup.py install

**usage**


    jootranslate --source /path/to/component/root --com your_component

to see a full list of all options

    jootranslate -h