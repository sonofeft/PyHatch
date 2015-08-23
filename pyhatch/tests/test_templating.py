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
here = os.path.abspath(os.path.dirname(__file__)) # Needed to find fulltoc
up_one = os.path.split( here )[0]  # Needed to find pyhatch development version
if here not in sys.path[:2]:
    sys.path.insert(0, here)
if up_one not in sys.path[:2]:
    sys.path.insert(0, up_one)
    
from pyhatch.fill_template import render, MyTemplateError, get_file_template

here = os.path.abspath(os.path.dirname(__file__))
up_one = os.path.split( here )[0]
template_dir = os.path.join( up_one, 'templates')

class MyTest(unittest.TestCase):

    def test_should_always_pass_cleanly(self):
        """Should always pass cleanly."""
        pass

    def test_nominal_subst(self):
        """Typical subst"""
        D = {'color':'brown', 'animal':'aardvark'}
        s = 'How now {{color}} cow.'
        self.assertEqual(render(s,D), 'How now brown cow.')
        
    def test_bad_closing_bracket(self):
        """Test Missing Closing Bracket"""
        D = {'color':'brown', 'animal':'aardvark'}
        s = 'How now {{color cow.'
        with self.assertRaises(MyTemplateError):
            render(s,D)

        s = 'How now {{color}} {{animal.'
        with self.assertRaises(MyTemplateError):
            render(s,D)

        s = 'How now {{color {{animal}}.'
        with self.assertRaises(MyTemplateError):
            render(s,D)

    def test_bad_open_bracket(self):
        """Test Missing Opening Bracket"""
        D = {'color':'brown', 'animal':'aardvark'}
            
        s = 'How now color}} cow.'
        with self.assertRaises(MyTemplateError):
            render(s,D)

        s = 'How now color}} {{animal}}.'
        with self.assertRaises(MyTemplateError):
            render(s,D)

        s = 'How now {{color}} animal}}.'
        with self.assertRaises(MyTemplateError):
            render(s,D)

    def test_bad_key(self):
        """Test Missing Dictionary Key"""
        D = {'col':'brown', 'animal':'aardvark'}
            
        s = 'How now {{color}} {{animal}}.'
        with self.assertRaises(MyTemplateError):
            render(s,D)

    def test_get_manifest_from_template(self):
        """Test Getting the MANIFEST.in file from templates subdirectory"""
        D = {'projName_lower':'myproject'}
        s = get_file_template( template_dir, 'MANIFEST.in', D )
        self.assertTrue( s.find('graft myproject') >= 0 )

    def test_get_simpleDesc_from_template(self):
        """Test Getting the MANIFEST.in file from templates subdirectory"""
        D = {'simpleDesc_rst':'123', 'longDesc':'abcdefghijklmnop'}
        s = get_file_template( template_dir, 'README.rst', D)
        sout = '123\n\nabcdefghijklmnop'
        self.assertEqual(s, sout)



if __name__ == '__main__':
    # Can test just this file from command prompt
    #  or it can be part of test discovery from nose, unittest, pytest, etc.
    unittest.main()

