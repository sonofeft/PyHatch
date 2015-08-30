
.. quickstart

QuickStart
==========

Verify tkinter Installed
------------------------

.. note::
    You only need tkinter if you use the PyHatch GUI.
    (The GUI is recommended, but not required)

**In Theory** tkinter is included with all standard Python distributions.
(In practice, it might not be included.)
It's almost certainly there on a Windows machine, however,
on Linux you might have to try::

    sudo apt-get update
    sudo apt-get install python-tk
    sudo apt-get install python3-tk
    
In order to get tkinter/Tkinter for python 2 & 3.

You can test the installation from a terminal window with::

    >>> import Tkinter       # python2
    >>> Tkinter._test()      # python2
    
    >>> import tkinter       # python3
    >>> tkinter._test()      # python3

This should pop up a small test window.

Verify Sphinx Installed
-----------------------

.. _Sphinx: http://sphinx-doc.org/

Sphinx_ is highly recommended for creating your project's documentation.

See `<http://sphinx-doc.org/latest/install.html>`_ for Install Instructions.

Install PyHatch
---------------

The easiest way to install PyHatch is::

    pip install pyhatch
    
        OR on Linux
    sudo pip install pyhatch
        OR perhaps
    pip install --user pyhatch

In case of error, see :ref:`internal_pip_error`

.. _internal_source_install:

Installation From Source
------------------------

Much less common, but if installing from source, then
the best way to install pyhatch is to use pip after navigating to the directory holding pyhatch source code::

    cd full/path/to/pyhatch
    pip install -e .
    
        OR on Linux
    sudo pip install -e .
        OR perhaps
    pip install --user -e .
    
This will execute the local ``setup.py`` file and insure that the pip-specific commands in ``setup.py`` are run.

Running pyhatch
---------------

.. note::
    Before running PyHatch, it is best to complete the first two steps of the :ref:`internal_project_checklist`

After installing with pip, there will be a launch command line program called **pyhatch** or, on Windows, **pyhatch.exe**. From a terminal or command prompt window simply type::

    pyhatch

and the ``PyHatch GUI`` should pop up. If not, then there may be an issue with your system path.
The path for the pyhatch executable might be something like::

    /usr/local/bin/pyhatch             (if installed with sudo pip install -e .)
         or 
    /home/<user>/.local/bin/pyhatch    (if installed with pip install -e .)
         or 
    C:\Python27\Scripts\pyhatch.exe    (on Windows)

Make sure your system path includes the above path to **pyhatch**.


After launching pyhatch, you simply fill in the form, select a directory in which to place the new project and hit the **Build Project** button.

It is possible to run the ``PyHatch GUI`` directly from source without installing it. Simply navigate to the source files and type::

    python hatch_gui.py


.. _internal_pip_error:

pip Error Messages
------------------

If you get an error message that ``pip`` is not found, see `<https://pip.pypa.io/en/latest/installing.html>`_ for full description of pip installation.

I've sometimes had issues with pip failing on Linux with a message like::


    InsecurePlatformWarning
            or    
    Cannot fetch index base URL https://pypi.python.org/simple/

Certain Python platforms (specifically, versions of Python earlier than 2.7.9) have the InsecurePlatformWarning. If you encounter this warning, it is strongly recommended you upgrade to a newer Python version, or that you use pyOpenSSL.    

Also ``pip`` may be mis-configured and point to the wrong PyPI repository.
You need to fix this global problem with ``pip`` just to make python usable on your system.


If you give up on upgrading python or fixing ``pip``, 
you might also try downloading the pyhatch source package 
(and all dependency source packages)
from PyPI and installing from source as shown above at :ref:`internal_source_install`


