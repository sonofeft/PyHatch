

History
=======

GitHub Log
----------

* Jul 18, 2019
    - (by: sonofeft)
        - Modified upload batch file to use twine
        - Made some twine doc changes

* Jul 9, 2019
    - (by: sonofeft)
        - Update README.rst
        - twine is having trouble with RestructuredText in README.rst

* Jul 8, 2019
    - (by: sonofeft)
        - Create .readthedocs.yml
        - Added some doc links
        - Update HISTORY.rst
        - version 0.0.19 dropped python 3.3 and 3.4 support
        - fixed Travis CI for python 3.4 and added spell check notes
        - Add Twine documentation for project upload
        
* Feb 09, 2019
    - (by: sonofeft) 
        - depricated register command
* May 13, 2018
    - (by: sonofeft) 
        - Added Spell Checking
* Jul 13, 2017
    - (by: sonofeft) 
        - doc tweek
* Jul 03, 2017
    - (by: sonofeft) 
        - fixed  ConfigParser  import for python 2.7
        - changed "bdist_wininst" to "bdist_wheel" in setup.py upload command
        - Added some changes due to time passage (Twine, python versions)
* Sep 14, 2015
    - (by: sonofeft) 
        - History api change and logo PNG change
            Can now hand edit HISTORY.rst file and history_from_github_api.py will
            keep hand edits untouched, only adding new GitHub commits to HISTORY.rst
* Sep 08, 2015
    - (by: sonofeft) 
        - updated history
        - version 0.0.15
            Tweeked history.rst
            Fixed examples subdirectory install
* Sep 06, 2015
    - (by: sonofeft) 
        - Update HISTORY.rst
        - Version 0.0.14
        - removed make_toctree from fulltoc.py
            Added some mock module logic to read_the_docs.rst
            Added some apt-get logic to travis_ci.rst
* Sep 02, 2015
    - (by: sonofeft) 
        - History update
        - Version 0.0.13
            package_data needed to be added for templates
        - History update
        - Version 0.0.10
* Aug 31, 2015
    - (by: sonofeft) 
        - Version 0.0.9
            Updated HISTORY.rst
        - Cosmetic tweek to generic_log.svg file
* Aug 30, 2015
    - (by: sonofeft) 
        - Added Generic SVG Logo
        - Updated HISTORY.rst by running history_from_github_api.py
        - Version 0.0.8
            Added copyright page to docs.
        - Version 0.0.7
            Cleaned up history.rst and authors.rst as well as quickstart template
        - Added Quickstart page to docs
            Added logo changeout instructions.
            Added PyHatch links to history.rst page.
        - Version 0.0.6
            Added AUTHORS.rst, fixed history script bug, and link error
* Aug 29, 2015
    - (by: sonofeft) 
        - fixed doc error on PyHatch.cfg location
        - Added ``Making History`` page
            In sphinx docs, described how to run history_from_github_api.py python
            script.
            Also added a little doc cleanup.
* Aug 28, 2015
    - (by: sonofeft) 
        - Added HISTORY.rst generation from GitHub API
            Included all the scripts and templates to make a History page in the
            Sphinx docs.  Also added build_all_html.py in /docs/ subdirectory to
            ``touch`` all rst files such that sphinx will rebuild the whole site.
