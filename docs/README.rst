|image0| |image1| |image2| |Python 3| |PyPI - Python Version|
|Documentation Status|

jootranslate
------------

Searches for JText::\_ translations in php and label\|description in xml
files and generates the ini files. If the file exist only new
translation strings will be added. Your translation strings have to
start with COM\_COMPONENTNAME to get accepted.

This is just a little helper so you don\`t have to copy and paste all
your translation strings by hand.

Your component needs the following directory structure

::

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

::

    pip install jootranslate

local

::

    python setup.py install

**usage**

::

    jootranslate --source /path/to/component/root --com your_component

to see a full list of all options

::

    jootranslate -h

**todo**

Generate the \*.sys.ini files

.. |image0| image:: https://img.shields.io/pypi/v/jootranslate.svg
   :target: https://pypi.python.org/pypi?name=jootranslate&:action=display
.. |image1| image:: https://travis-ci.org/pfitzer/jtranslate.svg?branch=master
   :target: https://travis-ci.org/pfitzer/jtranslate
.. |image2| image:: https://pyup.io/repos/github/pfitzer/jtranslate/shield.svg?t=1520427395490
   :target: https://pyup.io/account/repos/github/pfitzer/jtranslate/
.. |Python 3| image:: https://pyup.io/repos/github/pfitzer/jtranslate/python-3-shield.svg
   :target: https://pyup.io/repos/github/pfitzer/jtranslate/
.. |PyPI - Python Version| image:: https://img.shields.io/pypi/pyversions/jootranslate.svg
   :target: https://pypi.python.org/pypi?name=jootranslate&:action=display
.. |Documentation Status| image:: https://readthedocs.org/projects/jootranslate/badge/?version=latest
   :target: http://jootranslate.readthedocs.io/?badge=latest
