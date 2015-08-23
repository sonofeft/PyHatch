.. project_layout


Project Layout
==============

.. _Read the docs: http://readthedocs.org/
.. _Sphinx: http://sphinx.pocoo.org/
.. _reStructuredText: http://sphinx.pocoo.org/rest.html

.. _Travis CI: http://docs.travis-ci.com
.. _GitHub: https://github.com/
.. _tox automation: https://testrun.org/tox/latest/
.. _PyPy: http://pypy.org/

PyHatch creates a ``typical`` project layout for your new project.
(The definition of ``typical`` might be the subject of much discussion).

Some new project called ``NewPyGithubProject`` would be created with the layout below::


    NewPyGithubProject/
        .pypirc
        .travis.yml
        docs/
            conf.py
            fulltoc.py
            functions.rst
            index.rst
            make.bat
            Makefile
            sphinxy.py
        newpygithubproject/
            __init__.py
            mycode.py
            examples/
                example_1.py
            tests/
                __init__.py
                test_hatch_supt.py
        LICENSE.txt
        MANIFEST.in
        README.rst
        requirements.txt
        setup.cfg
        setup.py
        tox.ini

PyHatch itself is laid out very similar to the projects it creates.

PyHatch is tested with `tox automation`_ usage locally and `Travis CI`_ on GitHub_. The goal is to operate with python 2, 3 and PyPy_.

tk_nosy is a helper tool that watches local files, detects changes and runs nosetests when changes are detected.  For Test Driven Development (TDD), this is a desirable workflow. It is recommended to install and use tk_nosy.

The documentation of PyHatch is hosted on `Read the docs`_.  It is created by Sphinx_ using reStructuredText_ and linked to the GitHub repository.  Whenever the RST files change on GitHub, the docs are updated on `Read the docs`_.


.. note::

    pytest.org advises AGAINST putting __init__.py into the test dir, however, that is what allows "setup.py test" to work. Feel free to delete the __init__.py file if you have issues with it.
