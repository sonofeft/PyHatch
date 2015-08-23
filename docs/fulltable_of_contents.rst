.. fulltable_of_contents

Full Table of Contents (fulltoc)
================================

.. _Sphinx: http://sphinx-doc.org/

By default, ``PyHatch`` includes ``fulltoc`` as part of the Sphinx_ document setup.
This results in a more complete set of links in the sidebar.

I modified my ``conf.py`` file to include ``fulltoc`` and had to make some special changes for :ref:`internal_travis_ci` to work (see :ref:`internal_travis_ci_wrinkle`).

**The information below is the normal setup for fulltoc, shown here for information only.**

======================
 sphinxcontrib-fulltoc
======================

 -- Include a full table of contents in your sidebar.

sphinxcontrib-fulltoc is an extension for the Sphinx_ documentation
system that changes the HTML output to include a more detailed table
of contents in the sidebar. By default Sphinx only shows the local
headers for the current page. With the extension installed, all of the
page titles are included, and the local headers for the current page
are also included in the appropriate place within the document.


Basic Installation
------------------

.. _Install sphinxcontrib-fulltoc: https://sphinxcontrib-fulltoc.readthedocs.org/en/latest/install.html

Install info found at `Install sphinxcontrib-fulltoc`_.


1. Install the package along with Sphinx.

   There are two ways to install the extension. Using pip::

     $ pip install sphinxcontrib-fulltoc

   or from the source tree::

     $ python setup.py install

2. Add the extension to the list in your ``conf.py`` settings file for
   each project where you want to use it::

      # conf.py
      ...
      extensions = ['sphinxcontrib.fulltoc']
      ...
      
3. Rebuild all of the HTML output for your project.

