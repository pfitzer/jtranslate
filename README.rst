============
jootranslate
============

search for JText translations in php files and generates the ini files. If the file exist only new translation strings will
be added.

Your component needs the following directory structure

| ``administrator``
| - ``components``
| -- ``com_COMPONENTNAME``
| --- ``controllers``
| --- ``language``
| ---- ``en-GB``
| --- ``etc``
| ``components``
| - ``com_COMPONENTNAME``
| -- ``controllers``
| -- ``language``
| --- ``en-GB``
| -- ``etc``

************
installation
************

**with pip**

``pip install jootranslate``

**local**

``python setup.py install``

*****
usage
*****
``jootranslate --source /path/to/component/root --com your_component``

``jootranslate -h`` to see a full list of all options