.. new_github_proj


.. _internal_new_github_proj:

New GitHub Project
==================

.. _sphinx: http://sphinx-doc.org/


Create a GitHub Account
-----------------------

Before you can start a project on GitHub, you will need to `Get Set Up <https://help.github.com/articles/set-up-git/>`_ with GitHub by creating an account.

Go to `<https://help.github.com/articles/set-up-git/>`_ and follow the directions to create your account.


Set Up Git
----------

If git is not already on your system, go to `<http://git-scm.com/downloads>`_ and download it.

It is easiest to install Git on Linux using the preferred package manager of your Linux distribution, for example on Debian/Ubuntu::

    apt-get install git
            OR
    sudo apt-get install git

GitHub for Windows or `GitHub Desktop <https://desktop.github.com/>`_ is very convenient for Windows users.

For all operating systems it's a good idea to set your credentials via::

    git config --global user.name "YOUR NAME"
    git config --global user.email "YOUR EMAIL ADDRESS"

For privacy concerns, consider using an email address of: <username>@users.noreply.github.com See: `Keeping your email address private <https://help.github.com/articles/keeping-your-email-address-private/>`_

These housekeeping tasks are covered at `<https://help.github.com/articles/set-up-git/>`_.

Create New Repository
---------------------

The instructions to create a new repository are at `<https://help.github.com/articles/create-a-repo/>`_.

It is six simple steps to create the new repo.


1) click "New repository" (+ sign at upper right of `<https://github.com/>`_)
2) create a short, memorable name
3) add a description
4) choose between public or private (public is simpler)
5) Select ``Initialize this repository with a README`` (allows immediate cloning)
    * Use the option to create a .gitignore file, select **Python**
        - This will ignore things python creates that just get in the way; things like __pycache__ and .tox subdirectories, \*.pyc and \*.pyo files, .coverage files and much more.
    * You can also select a license
6) Click Create repository

Clone Your New Repository
-------------------------

Suppose that your GitHub username is "MrEd" and your project name is "ApplePy", then at the GitHub website of your new repository::

    for example...    https://github.com/MrEd/ApplePy
    
If your browser supports it, click the **Clone in Desktop** button to create a local clone. Start adding and editing files in the local repository and committing them whenever you like.

.. note::

    When you **Clone in Desktop**, a new subdirectory will be created **below** whatever directory location you select. That **new** subdirectory will have your projects name.  You do **NOT** need to first create a subdirectory with your projects name.

.. note::

    You may want to delete **README.md** and replace it with **README.rst**
    (Replace Markdown with ReStructuredText since sphinx_ uses \*.rst files.)

If you use ``git`` from the command line, you should navigate to the location where you want the cloned project to be stored.  Look for an entry box on the project's GitHub web page just above **Download ZIP** called ``HTTPS clone URL``. Copy and paste that URL into the command::

    git clone <pasted url>
            FOR EXAMPLE
    git clone https://github.com/mred/applepy.git
    
You will now have a cloned project.

If you have been doing some development already, simply paste your existing files into the new repository and commit them.

Set up ReadTheDocs
------------------

.. _Read the Docs on GitHub: https://github.com/rtfd/readthedocs.org

You'll want your documentation to automatically update to your ReadTheDocs page, whenever you commit changes to GitHub.

Go to `<https://readthedocs.org/>`_ and Log In. (If you do not yet have an account on ReadTheDocs, look at :ref:`internal_read_the_docs`.

Logging in to ReadTheDocs, takes you to the ReadTheDocs dashboard. Select **Import a Project**  followed by **Import from GitHub**.

You may have to select **Sync Your GitHub Projects** to see the new project.

Select the **Create** button for the new project.

If you select "Edit advanced project options" and hit the **Next** button, You can select ``Python`` as the Programming Language and  paste the GitHub url for your project as the ``Project homepage:``. ("https://github.com/MrEd/ApplePy" in the previous example)

Finally select the **Build** button.

Given a little time, the **View Docs** button will jump to your documentation. (http://applepy.readthedocs.org/en/latest/ in the previous example)

Automatically Update ReadTheDocs
--------------------------------

Your docs on ReadTheDocs should update whenever you push updates to GitHub. To verify this, go to your new repository::

    for example...    https://github.com/MrEd/ApplePy
    
and click the ``Settings`` button.

Click ``Webhooks & Services`` at the upper left. You should see a ReadTheDocs link in the Services section.

Click ``ReadTheDocs`` and verify that it is set to ``Active``.  If it's active, your good.


Turn on Travis CI
-----------------

While in the ``Webhooks & Services`` option from the above ReadTheDocs section, select the drop-down menu for ``Add service`` and select ``Travis CI``. After activating, you can push the ``Test service`` button to run ``Travis CI`` immediately.

You may have to go to your Travis CI profile page, Sync your repositories and activate the service.
(for example, https://travis-ci.org/profile/<your account name> )

Now, whenever you push new code to GitHub, Travis CI will run.

Also make sure the link in your ``README.rst`` file to the Travis CI build status is correct.  It should look something like::


    .. image:: https://travis-ci.org/<MyGitHubName>/<MyProjectName>.svg?branch=master
        :target: https://travis-ci.org/<MyGitHubName>/<MyProjectName>


See :ref:`internal_travis_ci` for more information regarding :ref:`internal_travis_ci`



