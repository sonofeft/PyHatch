.. pylint

.. _internal_pylint:

Pylint
======

Pylint_ is a tool that checks for errors in Python code, tries to enforce a coding standard and looks for refactoring opportunities. It is very good at flagging areas of your code that deserve a second look for possible errors or clean-up.

While Pylint can be run from the command line, it is much more convenient in an IDE.  The IDE that I use for this is `Spyder IDE`_. It is available on all major platforms, see: `Install Spyder`_. For other IDEs with integrated Pylint_ go to http://www.pylint.org/.

When you run Pylint_, remember that what it recommends is not to be taken as gospel. It may warn you about things that you have conscientiously done.  Don't be afraid to disable Pylint_ warnings that you have thought about and determined to be spurious.  For example the following comment in a python source file::

   # pylint: disable=C0321
 
will disable the pylint warning message C0321 ("more than one statement on a single line").

In my opinion, the greatest benefit of Pylint_ is to simply draw your attention to a questionable piece of code and make you think about it. Each *disable* comment is a testament to the fact that your judgement is better than some rigid set of guidelines.

Check out `Pylint Documentation`_ for further documentation.

.. _Pylint Documentation: http://docs.pylint.org/

.. _Spyder IDE: https://pythonhosted.org/spyder/pylint.html

.. _Install Spyder: https://pythonhosted.org/spyder/installation.html

.. _Pylint: http://www.pylint.org/
