#!/usr/bin/env python
# -*- coding: ascii -*-

r"""
{{simpleDesc}}

<Paragraph description see docstrings at http://www.python.org/dev/peps/pep-0257/>
{{longDesc}}

{{license_header}}
"""
import os
here = os.path.abspath(os.path.dirname(__file__))


# for multi-file projects see LICENSE file for authorship info
# for single file projects, insert following information
__author__ = '{{author}}'
__copyright__ = '{{proj_copyright}}'
__license__ = '{{proj_license}}'
exec( open(os.path.join( here,'_version.py' )).read() )  # creates local __version__ variable
__email__ = "{{email}}"
__status__ = "{{status}}" # "3 - Alpha", "4 - Beta", "5 - Production/Stable"

#
# import statements here. (built-in first, then 3rd party, then yours)
#
# Code goes below.
# Adjust docstrings to suite your taste/requirements.
#

class {{mainClassName}}(object):
    """{{simpleDesc}}

    Longer class information....
    Longer class information....

    Attributes::
    
        likes_spam: A boolean indicating if we like SPAM or not.

        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self):
        """Inits {{mainClassName}} with blah."""
        self.likes_spam = True
        self.eggs = 3

    def public_method(self, arg1, arg2, mykey=True):
        """Performs operation blah.
        
        :param arg1: description of arg1
        :param arg2: description of arg2
        :type arg1: int
        :type arg2: float
        :keyword mykey: a needed input
        :type mykey: boolean
        :return: None
        :rtype: None
        
        .. seealso:: blabla see stuff
        
        .. note:: blabla noteworthy stuff
        
        .. warning:: blabla arg2 must be non-zero.
        
        .. todo:: blabla  lots to do
        """
        #  Answer to the Ultimate Question of Life, The Universe, and Everything
        return 42

if __name__ == '__main__':
    C = {{mainClassName}}()
