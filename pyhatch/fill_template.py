from __future__ import absolute_import
from __future__ import print_function

import os


"""
fill_template will take an input string, and substitute any target strings
with values from an input dictionary.

The keys of the dictionary must match the name of the substitute string.

For Example:
   s = 'How now {{color}} cow.'
   D = {'color':'brown'}
   
   render(s, D) will return:   'How now brown cow.'
"""

class MyTemplateError(Exception):
    """Custom exception handler for ill-formed templates"""
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)
        
def get_file_template( data_dir, fname, valueD ):
    """Returns rendered template 
    
        :param data_dir: (str) directory holding template file
        :param fname: (str) file name containing template with {{xxx}} style replacement
        :param valueD: (dict) dictionary with (key,value) pairs
    """
    
    fullname = os.path.join( os.path.abspath(data_dir), fname )
    print( 'fullname =',fullname )
    f = open(fullname, 'r')
    template_str = f.read()
    f.close()
    
    return render( template_str, valueD )
    

def render( template_str, valueD ):
    """Returns rendered template 
    
        :param template_str: (str) template with {{key}} values in it
        :param valueD: (dict) dictionary with (key,value) pairs
    """
    
    sL = template_str.split('{{')
    
    if len(sL) == 0:
        return '' # Let an empty input slide
        
    if len(sL) == 1:
        if template_str.find('}}') < 0:
            return template_str
        ssL = template_str.split('}}')
        raise  MyTemplateError('Closing brackets w/o opening brackets at string="%s"'%ssL[0][-20:])

    if sL[0].find('}}') >= 0:
        ssL = sL[0].split('}}')
        raise  MyTemplateError('Closing brackets w/o opening brackets at string="%s"'%ssL[0][-20:])

    
    if len(sL) < 2: # No Opening Brackets anywhere
        sL = template_str.split('}}')
        if len(sL) > 1: # Closing Brackets w/o Opening Brackets
            raise MyTemplateError('No opening brackets at string="%s"'%sL[0][-20:])
        return template_str
    
    for i in range(1, len(sL)):
        s = sL[i]
        ssL = s.split('}}')
        if len(ssL) != 2:
            raise MyTemplateError('No closing brackets at string="%s"'%s[:20])
        key = ssL[0].strip() # allow some spaces around key

        if key in valueD:
            sL[i] = valueD[key] + ssL[1]
        else:
            raise MyTemplateError('Missing dictionary key at string="%s"'%s[:20])
            
    
    return ''.join(sL)
    
if __name__ == "__main__":
    
    import sys
    
    s = get_file_template( './templates', 'MANIFEST.in', {} )
    print( s )
    
    s = get_file_template( './templates', 'README.rst', {'simpleDesc_rst':'123', 'longDesc':'abcdefghijklmnop'} )
    print( s )
    
    sys.exit()
    def tryit(s, D, allow_exception=False):
        print( '  For s=',s )
        print( '  And D=',D )
        try:
            result = render(s, D)
            print( 'Result =', result )
        except:
            result = '======= ERROR ======='
            print( 'Result =', result )
            
            if allow_exception:
                render(s, D)
        print(' ')
        
    
    D = {'color':'brown', 'animal':'aardvark'}
    s = 'How now {{color}} cow.'
    
    tryit(s, D)
    tryit('How now brown cow.', D)
    
    tryit('How now {{color cow.', D)

    tryit('How now {{col}} cow.', D)
    
    tryit('How now {{color}} {{animal}}.', D)

    tryit('How now color}} {{animal}}.', D)
    