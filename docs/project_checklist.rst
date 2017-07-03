
.. project_checklist

.. _internal_project_checklist:

New Project Checklist
=====================


.. _tox: https://tox.readthedocs.org/en/latest/

.. _Bitbucket: https://bitbucket.org/
.. _GitHub: https://github.com/
.. _PyPI: https://pypi.python.org/pypi
.. _twine: https://pypi.python.org/pypi/twine
.. _Twine: https://pypi.python.org/pypi/twine
.. _sphinx: http://sphinx-doc.org/
.. _tk_nosy: http://tk_nosy.readthedocs.org/en/latest/

The following checklist is designed to help set up and complete a new python programming project and host it on PyPI_.  

Placing the source code on GitHub_ or Bitbucket_ will make the source code and documentation available to others.

Before You Start Programming
----------------------------

#. Check that your project's name is available on PyPI_. Go to `<https://pypi.python.org/pypi>`_ and use the search feature to verify that your desired project name is available. When you decide on an available name, you can create a repository and register it with PyPI_.
    * Also look for a project that already does what you intend to do. 
    * You may be able to contribute to an existing project instead of reinventing the wheel ;-).

#. Set up the project on GitHub_ or Bitbucket_ (I recommend GitHub_).
    * For GitHub_ (see :ref:`internal_new_github_proj`)
        - setup :ref:`internal_read_the_docs` automatic doc creation
        - setup :ref:`internal_travis_ci` for automatic unittests with different Linux python versions
    * on Bitbucket_ (see `<https://bitbucket.org/>`_)
        - Bitbucket_ appears to have fewer features than GitHub_.
        - documentation is often just the README.rst file, there is no direct access to  :ref:`internal_travis_ci` or :ref:`internal_read_the_docs`
        
#. Run ``PyHatch`` to create the project folder and supporting files
    * Use the URL for either GitHub or Bitbucket project as ``project url`` in pyhatch GUI.
        - If using ReadTheDocs, you might want to use the ReadTheDocs url in pyhatch GUI.
    * Optionally delete ``examples`` subdirectory
        - PyHatch creates an ``examples`` subdirectory that you may choose not to use.
    * Optionally create a new ``logo`` image file (PNG, GIF, JPEG, SVG, etc.)
        - PyHatch creates a logo called ``generic_logo.svg`` located in the /docs/_static subdirectory
        - The current logo is a 210x62 pixel SVG file. An image file of similar characteristics would work well in the Sphinx-generated HTML pages.
        - To change the logo, look in the file ``/docs/conf.py`` and change the line::
        
            html_logo = "./_static/generic_logo.svg"
                  to
            html_logo = "./_static/<your new image file name>"
    
#. Register yourself with PyPI (If you haven't already)
    * See https://pypi.python.org/pypi?%3Aaction=register_form to get a username and password

    
#. Configure your ``.pypirc`` file to make register and upload to PyPI_ easier. 
    * Edit the username and password in the ``.pypirc`` file that ``PyHatch`` creates
        - ``PyHatch`` leaves only place-holders for username and password
    * Move ``.pypirc`` to your home directory after editing. See :ref:`package_pypirc` for guidance.

#. Register you package with PyPI (Python Package Index)
    * The preferred way to register your package is by filling the web form at: https://pypi.python.org/pypi?%3Aaction=submit_form 
        - for testPyPI see: https://testpypi.python.org/pypi?%3Aaction=submit_form
    * If the web form is too "clunky" for you, then you can use your ``setup.py`` file, with the command:
        - ``python setup.py register`` for PyPI
        - For testPyPI: ``python setup.py register -r https://testpypi.python.org/pypi``
            - or with ``.pypirc`` file: ``python setup.py register -r testpypi``
        
#. Edit the ``tox.ini`` and ``.travis.yml`` files to match the python versions you want to support
    * :ref:`internal_tox` is excellent for checking multiple versions of python on your development machine.
    * :ref:`internal_travis_ci` is excellent for checking multiple versions of python on generic Linux machines when you check your code into GitHub.
#. Edit ``MANIFEST.in`` and ``setup.py`` (This is the first of perhaps many edits)
    * The ``packages=find_packages(...)`` option within ``setup.py`` and the ``MANIFEST.in`` file both fill very similar roles in specifying what files will be distributed with your code.  
    * See https://docs.python.org/2/distutils/sourcedist.html#manifest for an understanding of how to specify files to distribute.
    * See https://docs.python.org/2/distutils/sourcedist.html#the-manifest-in-template for guidelines on how to make a ``MANIFEST.in`` file.
    
The Programming Cycle
---------------------

#. Start programming and developing the code
    * Use :ref:`internal_tox` and tk_nosy_ to constantly validate the code during development
        - :ref:`internal_tox` makes the virtualenv setup easy for different python versions
            - Tox needs accurate ``requirements.txt`` file
            - Tox needs accurate ``install_requires`` option within ``setup.py``
        - tk_nosy_ makes TDD (Test Driven Development) easy
            - better still, try TDDD (Test Driven Documented Development)
            - tk_nosy_ uses ``nosetests`` to run unittests. By default ``coverage`` is turned on. To turn ``coverage`` off, edit the setup.cfg file under the ``nosetests`` header. Change ``with-coverage`` from one to zero (1 to 0).
            
    * Use :ref:`internal_pylint` on each python file to constantly measure code quality
        - The right IDE should do this automatically
    * Use :ref:`internal_travis_ci` to verify operation on Linux machines with different python versions
        - Each push to GitHub_ should automatically run :ref:`internal_travis_ci`
    * Use sphinx_ to keep documentation current with code
    
#. Constantly Work the Documentation
    * Whether just a README.rst or a full sphinx_ HTML site, keep editing and re-editing the documentation.
    * Consider using the ``sphinxy.py`` script located in the ``docs`` subdirectory.
        - ``sphinxy.py`` rebuilds the HTML docs every time a ``*.rst`` file changes. It can make the documentation development cycle a little more convenient.
            - Note that ``sphinxy.py`` also changes the file system date for all ``*.rst`` files
    * Consider a ``QuickStart`` section in your docs (a quick install and use section)


#. In addition to the :ref:`internal_pylint` already run on your code, consider running `cheesecake <https://github.com/griggheo/cheesecake>`_ to verify your code's "readiness".
    * `Cheesecake <https://github.com/griggheo/cheesecake>`_ is more demanding and makes more value judgements than  :ref:`internal_pylint`.


Upload to PyPI (or testPyPI)
----------------------------

#. Run :ref:`internal_tox` before uploading to PyPI_
    * This will test ``pip`` installs of package dependencies in the tox virtual environment.
    * Make sure that your ``tox.ini`` file dependencies (``deps``) are the same as in your ``setup.py`` and ``requirements.txt`` files.

#. Set the correct version number of the code
    * Open the file ``_version.py`` and edit the version number at the bottom of the file 
        - for example change **__version__ = '0.0.1'**
        - to **__version__ = '0.0.2'**
    * Commit to GitHub_ with comment like::
    
        git add .
        git commit -m "Release 0.0.2"

#. Create ``HISTORY.rst`` by running ``history_from_github_api.py``
    * The above commit will help make ``HISTORY.rst`` current
    * See :ref:`internal_making_history` for guidance
    
#. Verify the docs
    * Whether just a README.rst or a full sphinx_ HTML site, re-read the documentation.
        - If using ReadTheDocs:
            - include a link to ReadTheDocs in README.rst
            - include a link back to GitHub repository somewhere in ReadTheDocs

#. If you skipped this step before, Register you package with PyPI (Python Package Index)
    * Run ``python setup.py register``
        - For testPyPI: ``python setup.py register -r https://testpypi.python.org/pypi``
    * With ``.pypirc`` file can use ``python setup.py register -r pypi``
        - or ``python setup.py register -r testpypi`` on testPyPI
    * Check the site ``http://pypi.python.org/pypi/<projectname>``
        - Make sure that ``Home Page:`` links to your GitHub or Bitbucket source code repository.
    
#. Create release file 
    * Run `` python setup.py sdist``
    * Examine ``MyProject.tar.gz`` or ``MyProject.zip``
         - Make sure the included files are what you want
            - Edit ``MANIFEST.in``
            - Edit packages=find_packages(...) within ``setup.py``
            
    
#. Create ``wheel`` for upload to PyPI
    * ``python setup.py sdist bdist_wheel``

.. warning::

    Twine_ is now the preferred way to register and upload projects. The following ``setup.py`` approach has been abandoned.

#. If twine_ is not available or if you are on Windows (Windows version is buggy right now) upload your package to PyPI_ as follows::

    python setup.py register -r pypi
    python setup.py sdist bdist_wheel upload -r pypi
    
        OR for testPyPI
        
    python setup.py register -r testpypi
    python setup.py sdist bdist_wheel upload -r testpypi


.. note::

    Twine_ is now the preferred way to register and upload projects.

#. If twine_ is available (it's more secure than setup.py upload) and your ``.pypirc`` file is properly located and formatted, then try to upload package to PyPI_ using::

    twine upload dist/*
    
        OR for testPyPI
        
    twine upload -r testpypi dist/*
        
        
#. Test installing your project from PyPI (and/or testPyPI)::

        pip install <package name>
        
            OR for testPyPI
        
        pip install -i https://testpypi.python.org/pypi <package name>
        
            OR for testPyPI with PyPI_ Dependencies
        
        pip install -i https://testpypi.python.org/pypi <package name> --extra-index-url https://pypi.python.org/pypi

        
#. Run unittests on the install with a virtualenv or clean virtual machine.   
    * Either ``nosetests`` or ``py.test`` should work
    
#. Test the ``entry_points`` command from ``setup.py``.
    * Should be able to simply run ``my_command`` from command line environment.
    
#. Check the three main web pages for your project::

    The Code at: https://github.com/<github user name>/<package name>

    The Docs at: http://<package name>.readthedocs.org/en/latest/

    PyPI page at: https://pypi.python.org/pypi/<package name>
   
#. Let the world know what you've done.
    * Announce your project on `<https://mail.python.org/mailman/listinfo/python-announce-list>`_

