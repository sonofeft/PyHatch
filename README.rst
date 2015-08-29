

.. image:: https://img.shields.io/travis/sonofeft/PyHatch.svg
        :target: https://travis-ci.org/sonofeft/PyHatch

.. image:: https://img.shields.io/pypi/v/PyHatch.svg
    :target: https://pypi.python.org/pypi/pyhatch
        
.. image:: https://img.shields.io/pypi/pyversions/PyHatch.svg
    :target: https://wiki.python.org/moin/Python2orPython3

.. image:: https://img.shields.io/pypi/l/PyHatch.svg
    :target: https://pypi.python.org/pypi/pyhatch

.. _internal_index:

PyHatch
=======

**Pyhatch Initializes Files And Directory Structures For New Python Projects.**

See the Code at: `<https://github.com/sonofeft/PyHatch>`_

See the Docs at: `<http://pyhatch.readthedocs.org/en/latest/>`_

See PyPI page at:`<https://pypi.python.org/pypi/pyhatch>`_


PyHatch is intended to help technical programmers focus their python
programming efforts on their science and engineering problems by easing
the many source code organizational issues required to build and maintain
a quality code base.  PyHatch will initialize the basic file structure for
project files, documentation, unit testing and licensing.

Each time a new project is started, the user fills in a few simple forms and
selects a directory location for the project layout. The layout used by
PyHatch is shown below.::

    MyProject/
        myproject/
            __init__.py
            mycode.py
            examples/
                example_1.py
            tests/
                __init__.py
                test_mycode.py
        docs/
            conf.py
            index.rst
        .travis.yml
        HISTORY.rst
        history_from_github_api.py
        LICENSE.txt
        MANIFEST.in
        README.rst
        requirements.txt
        setup.cfg
        setup.py
        tox.ini

One goal of PyHatch is to encourage unit testing.  To do that, a "tests"
directory is created and initialized. Of the three common locations of the
test scripts shown below, PyHatch uses the third option. The user is free
to modify this layout, but encouraged to maintain test scripts in one of
the following layouts.

Put test scripts:
    1. Mixed into the same directory as mycode.py   /MyProject/myproject/
    2. At the same level as the code directory      /MyProject/tests/
    3. One level under the code directory           /MyProject/myproject/tests/

A tox.ini file is also created in order to simplify running the unit tests with
a number of different python versions.  Tox_ will need to be installed separately,
however, the new project simply needs to execute tox locally to use it.

The docs/ subdirectory contains the layout required to run sphinx_ and create
documentation for the project.  It is set up to automatically read the project
``*.py`` files and include code documentation on the fly. Note that Sphinx_ will
need to be installed separately.

Run ``make html`` in the docs/ subdirectory (with sphinx_ installed) to generate
HTML documentation for the project. The file ``index.html`` is the main page of 
the documentation in the directory docs/_build/html.

The examples/ subdirectory contains any example files that use the project.

The hope for PyHatch is that better code will result from early organization
and test driven development.

Notice that a configuration file (PyHatch.cfg) is created in the ``pyhatch`` 
subdirectory.  That configuration file holds project and personal data that
will help autofill the PyHatch GUI the second time tht PyHatch is used.


See the Code at: `<https://github.com/sonofeft/PyHatch>`_

See the Docs at: `<http://pyhatch.readthedocs.org/en/latest/>`_



.. _Tox: https://tox.readthedocs.org/en/latest/
.. _sphinx: http://sphinx-doc.org/
.. _Sphinx: http://sphinx-doc.org/

