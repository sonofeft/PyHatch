import sys
import os

sys.path.insert(0, os.path.abspath("../../"))

from pyhatch.hatch_supt import Hatch

IN_TEST_MODE = False

SIMPLEDESC='PyProTem acts as a temporary project for the time being to test tox, travis, futurize, etc.'
LONGDESC="""Use pyProTem to test tox usage locally, travis CI on GitHub on checkin, tk_nosy to watch files locally and alert breakage, operation under both python 2 and 3."""

h = Hatch(projName='PyProTem', 
          in_test_mode=IN_TEST_MODE,
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

h.save_project_below_this_dir( os.path.expanduser('~/') )

