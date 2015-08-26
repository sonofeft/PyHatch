import sys
import os

from pyhatch.hatch_supt import Hatch

SIMPLEDESC='''PyProTem acts as a temporary project for test purposes.'''

LONGDESC="""Use pyProTem to test tox usage locally, travis CI on checkin to 
GitHub, tk_nosy to watch files locally and alert breakage, operation under 
both python 2 and 3 on Windows and Linux."""

h = Hatch(projName='PyProTem', 
          mainPyFileName='main.py', 
          mainDefinesClass='Y',
          mainClassName='ProTem', 
          mainFunctionName='my_function',
          author='Some Guy', 
          github_user_name='somekindaguy',
          proj_copyright='Copyright (c) 2015 Some Guy',
          proj_license='GPL-3', 
          version='0.1.3', 
          email='someguy@someplace.com', 
          status='4 - Beta',
          simpleDesc=SIMPLEDESC, 
          longDesc=LONGDESC, 
          year=None,   # if None, set to this year
          organization=None)  # if None, set to author

# This example places project into user home directory
h.save_project_below_this_dir( os.path.expanduser('~/') )

