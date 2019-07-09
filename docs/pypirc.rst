.. pypirc

.. _internal_pypirc:

Upload to PyPI
==============

Before you can ``upload`` a project to PyPI, you need to ``register`` it.

The register command
--------------------

.. note:: 

    register command is DEPRECATED

The distutils command ``register`` is NO LONGER USED
to submit your distribution's
meta-data to an index server as follows::

    python setup.py register
    (NO LONGER REQUIRED)

.. _package-upload:

The upload command
------------------

.. note:: 

    upload command is DEPRECATED
    use twine to upload packages

Formerly, the distutils command ``upload`` pushed the distribution files to PyPI.

Twine is now the preferred method.

twine
-----

`Twine <https://pypi.org/project/twine/>`_ is a utility for interacting with PyPI, that offers a secure replacement for setup.py upload.

For any changes in upload procedure see: 
`Uploading the distribution archives <https://packaging.python.org/tutorials/packaging-projects/>`_

`Twine <https://pypi.org/project/twine/>`_ can be installed with::

    python  -m pip install --user --upgrade twine
    ...OR...
    python3 -m pip install --user --upgrade twine

Once installed, run `Twine <https://pypi.org/project/twine/>`_ to upload all of the archives under dist::

    python  -m twine upload dist/*
    ...OR...
    python3 -m twine upload dist/*


The command is normally invoked immediately after building one or more distribution
files.  For example, the commands ::

    python setup.py sdist bdist_wheel
    python -m twine upload dist/*

will cause the source distribution and the Windows installer to be uploaded to
PyPI.  Note that these will be uploaded even if they are built using an earlier
invocation of :file:`setup.py`, but that only distributions named on the command
line for the invocation including the ``upload`` command are uploaded.


.. _package_pypirc:

PyPI Configuration File
-----------------------

The **.pypirc** file will allow the **-r** option with ``register`` and ``upload`` commands to PyPI. It is really just a convenience to prevent having to type full username, password and url when working with PyPI or testpypi.

When properly installed you can register and upload to PyPI with the commands::

    python setup.py register
    python setup.py sdist bdist_wheel upload
            (same as)
    python setup.py register -r pypi
    python setup.py sdist bdist_wheel upload -r pypi
    
Or to the testpypi server with::
            
    python setup.py register -r testpypi
    python setup.py sdist bdist_wheel upload -r testpypi


.. warning::

    The following is the **OLD** way of defining a **.pypirc** file.

The default file, created by PyHatch, is shown below::


    [distutils]
    index-servers=
        pypi
        testpypi

    [testpypi]
    repository = https://testpypi.python.org/pypi
    username = <your test user name goes here>
    password = <your test password goes here>

    [pypi]
    repository = https://pypi.python.org/pypi
    username = <your production user name goes here>
    password = <your production password goes here>

.. warning::

    The above is the **OLD** way of defining a **.pypirc** file.

.. _New PyPi Upload: https://packaging.python.org/guides/migrating-to-pypi-org/#uploading

The new format is described at `New PyPi Upload`_

If you want to use this approach, then edit **.pypirc** to contain your username and password.

Move **.pypirc** (or a copy of **.pypirc**) to your home directory where it will be found automatically by setup.py::

           ~/.pypirc                 Home Directory

    /home/<Your Name>/.pypirc           on Linux
    C:\Users\<Your Name>\.pypirc        on Windows


If you leave a copy of **.pypirc** in your local directory, then add an entry for **.pypirc** into your ``.gitignore`` file. (or ``.hgignore`` file if you use mercurial)

Ignore files define which local files should NOT be in either `git <http://www.git-scm.com/>`_ or `mercurial <https://mercurial.selenic.com/>`_ source control systems respectively. Since **.pypirc** contains your username and password, it should not be posted to GitHub, Bitbucket, etc.


