
"""
fill_template will take an input string, and substitute any target strings
with values from an input dictionary.

The keys of the dictionary must match the name of the substitute string.

For Example:
   s = 'How now {{color}} cow.'
   D = {'color':'brown'}

   render(s, D) will return:   'How now brown cow.'
"""
from __future__ import absolute_import
from __future__ import print_function

import os
# pylint: disable=C0326, C0103, W0702

class MyTemplateError(Exception):
    """Custom exception handler for ill-formed templates"""
    def __init__(self, msg):
        Exception.__init__(self, msg)
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

    _s = get_file_template( './templates', 'MANIFEST.in', {} )
    print( _s )

    _s = get_file_template( './templates', 'README.rst', {'simpleDesc_rst':'123',
                           'longDesc':'abcdefghijklmnop'} )
    print( _s )

    sys.exit()
    def tryit(s, D, allow_exception=False):
        """A test function to try different template substitutions"""
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


    _D = {'color':'brown', 'animal':'aardvark'}
    _s = 'How now {{color}} cow.'

    tryit(_s, _D)
    tryit('How now brown cow.', _D)

    tryit('How now {{color cow.', _D)

    tryit('How now {{col}} cow.', _D)

    tryit('How now {{color}} {{animal}}.', _D)

    tryit('How now color}} {{animal}}.', _D)
