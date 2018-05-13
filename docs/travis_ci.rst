.. travis_ci

.. _internal_travis_ci:

Travis CI
=========

.. _Travis CI for Complete Beginners: http://docs.travis-ci.com/user/for-beginners/

Travis CI is a tool for continuous integration on GitHub. It allows your code to be automatically run through its unittest suite every time the your code is committed to GitHub. The unittest suite will be run for every python version of interest.

Bear in mind that Travis CI at GitHub will run the unittests on Linux machines.  If you need the tests run on a different platform, consider using :ref:`internal_tox` on a Windows or Mac machine and letting GitHub use Travis CI on its Linux machines.

For an introduction to Travis CI, see `Travis CI for Complete Beginners`_. 

Turning on the Travis CI Switch
-------------------------------

I had trouble finding the right location to turn on Travis CI for the GitHub project.

.. _Travis CI Getting Started: http://docs.travis-ci.com/user/getting-started/

.. _Sign in to Travis CI: https://travis-ci.org/

I started at the `Travis CI Getting Started`_ page, followed by signing into Travis CI at `Sign in to Travis CI`_

After fumbling around and getting signed in, I got to the "Settings" option for my project and flipped the buttons to "ON" for running a build on pushes and pulls using my .travis.yml file.


My baseline .travis.yml file seemed to work just fine::

    language: python
    python:
        - "2.7"
        - "pypy"
        - "3.3"
        - "3.4"

    install:
        - pip install -r requirements.txt
    script:
        - py.test
    
I received an email after syncing the file with GitHub that the above tests were successfully run.

Note that I have ``Travis CI`` set up to run ``py.test`` whereas I set up ``TOX`` to run ``nosetests``. Feel free to change them around to your test suite of choice.

Using apt-get
-------------

It may be necessary to add packages to Travis CI via ``apt-get`` for your project to work.  
If so, in your your .travis.yml file try something like::

    before_install:
        - sudo apt-get install python-matplotlib
        - sudo apt-get install python-numpy
        - sudo apt-get install python-scipy

Module import Errors
--------------------

You may get messages such as: `Failure: ImportError (No module named <Some Module Name>)`

If so try adding the following to your .travis.yml file::
    
    virtualenv:
        system_site_packages: true


.. _internal_travis_ci_wrinkle:

Test Discovery Wrinkle
----------------------

The only wrinkle was a difference in test discovery between nosetests and py.test.  The directory in which the test file executes appears to be different between the two.

With nosetests, it was enough to add to the search path at the beginning of the unittest file::

    sys.path.insert(0, os.path.abspath("../"))
    
With py.test it was necessary to add::

    sys.path.insert(0, os.path.abspath("."))
    
So now to be independent of testing software I add both at the beginning::

    import sys, os
    sys.path.insert(0, os.path.abspath("."))
    sys.path.insert(0, os.path.abspath("../"))

