#!/usr/bin/env python
# -*- coding: ascii -*-

r"""
{{simpleDesc}}

<Paragraph description  see docstrings at http://www.python.org/dev/peps/pep-0257/>
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

def {{mainFunctionName}}():
    """{{simpleDesc}}

    Args:
        arg1: 1st argument of function.

    Returns:
        None, always returns None

    Raises:
        No Exceptions raised.
    """
    return None


if __name__=='__main__':
    {{mainFunctionName}}()

