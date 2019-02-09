.. pypirc

.. _internal_pypirc:

Upload to PyPI
==============

Before you can ``upload`` a project to PyPI, you need to ``register`` it.

The register command
--------------------

DEPRECATED

The distutils command ``register`` is NO LONGER USED
to submit your distribution's
meta-data to an index server as follows::

    python setup.py register
    (NO LONGER REQUIRED)

.. _package-upload:

The upload command
------------------

The distutils command ``upload`` pushes the distribution files to PyPI.

The command is invoked immediately after building one or more distribution
files.  For example, the command ::

    python setup.py sdist bdist_wheel upload

will cause the source distribution and the Windows installer to be uploaded to
PyPI.  Note that these will be uploaded even if they are built using an earlier
invocation of :file:`setup.py`, but that only distributions named on the command
line for the invocation including the ``upload`` command are uploaded.

If a ``register`` command was previously called in the same command,
and if the password was entered in the prompt, ``upload`` will reuse the
entered password.  This is useful if you do not want to store a password in
clear text in a :file:`.pypirc` file.

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


