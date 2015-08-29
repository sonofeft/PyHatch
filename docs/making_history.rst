.. making_history

.. _internal_making_history:

Making History
==============

The history (i.e. Changelog) of a project created by PyHatch is displayed on the project's ``History`` page. 

For PyHatch itself, that page is here at  :ref:`internal_history` .

The ``History`` page is created by running the script ``history_from_github_api.py``.

As the name implies, it queries the GitHub repository for the project's commit data and reformats it into the file ``HISTORY.rst``.

Building HISTORY.rst
--------------------

From a terminal (i.e. command line window), navigate to the project directory where ``history_from_github_api.py`` resides and enter::

    python history_from_github_api.py
    
The screen will respond with::

    =========================================================
         Building HISTORY.rst file
         at: <Path to Your Project>
         Need GitHub user password for <Your GitHub Username>
    =========================================================
    Enter Password:
    
After entering your GitHub password (via the python ``getpass`` module for privacy), GitHub will be queried and a new ``HISTORY.rst`` will be created in the same directory as  ``history_from_github_api.py``.

.. note::

    When PyHatch creates your project, it creates a version of ``history_from_github_api.py`` **specifically** for the Project Name and GitHub Username.  If you use ``history_from_github_api.py`` for another user or project, ``history_from_github_api.py``  will need to be edited.
