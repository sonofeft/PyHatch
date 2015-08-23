import unittest
# import unittest2 as unittest # for versions of python < 2.7

import sys, os

here = os.path.abspath(os.path.dirname(__file__)) # Needed for py.test
up_one = os.path.split( here )[0]  # Needed to find {{projName_lower}} development version
if here not in sys.path[:2]:
    sys.path.insert(0, here)
if up_one not in sys.path[:2]:
    sys.path.insert(0, up_one)
    
from {{projName_lower}}.{{mainPyFilePrefix}} import {{func_or_class_name}}

class MyTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_should_always_pass_cleanly(self):
        """Should always pass cleanly."""
        pass

    def test_myclass_existence(self):
        """Check that function returns result"""
        result = {{mainFunctionName}}()

        # Function should return None
        self.assertEqual(result, None)

if __name__ == '__main__':
    # Can test just this file from command prompt
    #  or it can be part of test discovery from nose, unittest, pytest, etc.
    unittest.main()

