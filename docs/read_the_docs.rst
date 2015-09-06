.. read_the_docs

.. _internal_read_the_docs:

Read the Docs
=============

.. _Read the Docs on GitHub: https://github.com/rtfd/readthedocs.org

A very easy way to publish sphinx_ docs from a GitHub project is to follow the 
instructions at `Read the Docs on GitHub`_. Some of those instructions are pasted
below.

From github rtfd
----------------


`Read the Docs`_ hosts documentation for the open source community. It supports
Sphinx_ docs written with reStructuredText_, and can pull from your Subversion_,
Bazaar_, Git_, and Mercurial_ repositories.

.. _Read the docs: http://readthedocs.org/
.. _Sphinx: http://sphinx-doc.org/
.. _sphinx: http://sphinx-doc.org/
.. _reStructuredText: http://sphinx-doc.org/rest.html
.. _Subversion: http://subversion.tigris.org/
.. _Bazaar: http://bazaar.canonical.com/
.. _Git: http://git-scm.com/
.. _Mercurial: http://mercurial.selenic.com/

Documentation for RTD
---------------------

You will find complete documentation for setting up your project at `the Read
the Docs site`_.

.. _the Read the Docs site: https://docs.readthedocs.org/


Quickstart for GitHub-Hosted Projects
-------------------------------------

Follow these steps and you will have a new project automatically updated
when you push to GitHub.

#. Create an account on `Read the Docs`_.  You will get an email verifying your
   email address which you should accept within 7 days.

#. Log in and click on "Import".

#. Give your project a name, add the HTTPS link for your GitHub project, and
   select Git as your repository type.

#. Fill in the rest of the form as needed and click "Create".

#. On GitHub, navigate to your repository and click on "Settings".

#. In the sidebar, click on "Web Hooks & Services", then find and click on the
   "ReadTheDocs" service.

#. Check the "Active" setting and click "Update Settings".

#. All done.  Commit away and your project will auto-update.


Mock Modules
------------

ReadTheDocs may need to mock certain module imports in order for sphinx to build the project.
Add the snippet below to your ``conf.py`` file where ``MOCK_MODULES`` is replaced with your list of modules::

    import sys
    if sys.version_info < (3,):
        from mock import Mock as MagicMock
    else:
        from unittest.mock import MagicMock # added to unittest in python 3.3

    class Mock(MagicMock):
        @classmethod
        def __getattr__(cls, name):
                return Mock()

    MOCK_MODULES = ['pygtk', 'gtk', 'gobject', 'argparse', 'numpy', 'pandas']
    sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

.. note::

    For python2.7, MagicMock will need to be installed.
    Excute the ``pip install mock`` by including mock in your requirements.txt file

In the setup.py file you may need::

    on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
    if on_rtd:
        if sys.version_info < (3,3):
            requires = ['mock']  # for python2 and python < 3.3
        else:
            requires = []  # for >= python3.3
        
    else:
        # Place install_requires into the text file "requirements.txt"
        with open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as f2:
            requires = f2.read().strip().splitlines()

.. note::
    
    You may also need to check the box on ReadTheDocs advanced options.
    
    Use system packages:
       Give the virtual environment access to the global site-packages dir.

Using Sphinx extensions
-----------------------

.. _sphinxcontrib-fulltoc: http://sphinxcontrib-fulltoc.readthedocs.org/en/latest/

I am using the `sphinxcontrib-fulltoc`_ extension to build my docs and ReadTheDocs kept failing with::

   ExtensionError: Could not import extension sphinxcontrib.fulltoc
   
To solve the problem, I placed the fulltoc.py file from the ../Lib/site-packages/sphinxcontrib subdirectory into the docs/ GitHub subdirectory right next to conf.py.  It was then necessary to modify conf.py to use the local name of "fulltoc" instead of the full import path of "sphinxcontrib.fulltoc"::

    sys.path.append("../")
    sys.path.append(".")  # Needed to find fulltoc

    # If extensions (or modules to document with autodoc) are in another directory,
    # add these directories to sys.path here. If the directory is relative to the
    # documentation root, use os.path.abspath to make it absolute, like shown here.
    #sys.path.insert(0, os.path.abspath('.'))

    # -- General configuration ------------------------------------------------

    # If your documentation needs a minimal Sphinx version, state it here.
    #needs_sphinx = '1.0'

    # Add any Sphinx extension module names here, as strings. They can be
    # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
    # ones.
    extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.intersphinx',
        'sphinx.ext.todo',
        'sphinx.ext.ifconfig',
        'fulltoc'
    ]

I tried to modify my requirements.txt file to include `sphinxcontrib-fulltoc`_, but it never worked out for me.

