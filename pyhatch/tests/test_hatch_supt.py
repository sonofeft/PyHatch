import unittest
# import unittest2 as unittest # for versions of python < 2.7

"""
        Method                  Checks that
self.assertEqual(a, b)           a == b   
self.assertNotEqual(a, b)        a != b   
self.assertTrue(x)               bool(x) is True  
self.assertFalse(x)              bool(x) is False     
self.assertIs(a, b)              a is b
self.assertIsNot(a, b)           a is not b
self.assertIsNone(x)             x is None 
self.assertIsNotNone(x)          x is not None 
self.assertIn(a, b)              a in b
self.assertNotIn(a, b)           a not in b
self.assertIsInstance(a, b)      isinstance(a, b)  
self.assertNotIsInstance(a, b)   not isinstance(a, b)  

See:
      https://docs.python.org/2/library/unittest.html
         or
      https://docs.python.org/dev/library/unittest.html
for more assert options
"""

import sys, os
here = os.path.abspath(os.path.dirname(__file__))
up_one = os.path.split( here )[0]  # Needed to find pyhatch development version
if here not in sys.path[:2]:
    sys.path.insert(0, here)
if up_one not in sys.path[:2]:
    sys.path.insert(0, up_one)
from pyhatch.hatch_supt import Hatch

class MyTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.myclass = Hatch()

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        del( self.myclass )

    def test_should_always_pass_cleanly(self):
        """Should always pass cleanly."""
        pass

    def test_myclass_existence(self):
        """Check that myclass exists"""
        result = self.myclass

        # See if the self.myclass object exists
        self.assertTrue(result)

    def test_save_project(self):
        """Check that myclass exists"""
        result = self.myclass

        PROJ_D = {'status': '3 - Alpha',
                  'proj_copyright': 'Copyright (c) 2015 Charlie Taylor',
                  'proj_license': 'MIT', 'author': 'Charlie Taylor',
                  'longDesc': "MyProject tests the creation of a project using"+\
                  " pyHatch.\nShould be a piece of cake... but might not be, "+\
                  "so I test.",
                  'mainClassName': 'MyClass',
                  'simpleDesc': 'My project does this',
                  'version': '0.1.1', 'mainPyFileName': 'main.py',
                  'email': 'cet@appliedpython.com',
                  'mainFunctionName': 'my_function',
                  'mainDefinesClass': 'Y'}

        h = Hatch(projName='DocSampCase6', in_test_mode=True, **PROJ_D)
        h.save_project_below_this_dir( r'.' )


if __name__ == '__main__':
    # Can test just this file from command prompt
    #  or it can be part of test discovery from nose, unittest, pytest, etc.
    unittest.main()

