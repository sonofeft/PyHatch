#!/usr/bin/env python
# -*- coding: ascii -*-


"""
PyHatch initializes files and directory structure for new python projects.

PyHatch is intended to help technical programmers focus their python
programming efforts on their science and engineering problems by easing
the many source code organizational issues required to build and maintain
a quality code base.  PyHatch will initialize the basic file structure for
project files, documentation, unit testing and licensing.

Each time a new project is started, the user fills in a few simple forms and
selects a directory location for the project layout. The layout used by
PyHatch is shown below::

    MyProject/
        myproject/
            __init__.py
            mycode.py
            examples/
                example_1.py
            tests/
                __init__.py
                test_mycode.py
        docs/
            conf.py
            index.rst
        .travis.yml
        HISTORY.rst
        LICENSE.txt
        MANIFEST.in
        README.rst
        requirements.txt
        setup.cfg
        setup.py
        tox.ini

One goal of PyHatch is to encourage unit testing.  To do that, a "tests"
directory is created and initialized. Of the three common locations of the
test scripts shown below, PyHatch uses the third option. The user is free
to modify this layout, but encouraged to maintain test scripts in one of
the following layouts.

Put test scripts:
    #. Mixed into the same directory as mycode.py   /MyProject/myproject/
    #. At the same level as the code directory      /MyProject/tests/
    #. One level under the code directory           /MyProject/myproject/tests/

A tox.ini file is also created in order to simplify running the unit tests in
a number of different python versions.  Tox will need to be installed separately,
however, the new project simply needs to execute tox locally to use it.

The docs/ subdirectory contains the layout required to run sphinx and create
documentation for the project.  It is set up to automatically read the project
``*.py`` files and include code documentation on the fly.

Run "make html" in the docs/ subdirectory (with sphinx installed) to generate
HTML documentation for the project. The file "index.html" is the main page of
the documentation in the directory docs/_build/html.

The examples/ subdirectory contains any example files that use the project.

The hope for PyHatch is that better code will result from early organization
and test driven development.

Notice that a config file (PyHatch.cfg) is created in the users home directory
(in os.path.expanduser('~/')).  That config file holds project and personal data.

--------------
"""


#    I like extra spaces inside parens and sometimes camelCase
# pylint: disable=C0326
# pylint: disable=C0103
# I would prefer to redefine variable-rgx:??[a-z][A-Za-z0-9]{1,30}$

# pylint: disable=R0902, R0913, R0914, R0912, W0122

from __future__ import absolute_import
from __future__ import print_function

import os
here = os.path.abspath(os.path.dirname(__file__))
#  execfile( os.path.join(here,'_version.py')) # creates local __version__ variable
exec( open(os.path.join( here,'_version.py' )).read() )  # creates local __version__ variable

__author__ = 'Charlie Taylor'
__copyright__ = 'Copyright (c) 2013 Charlie Taylor'
__license__ = 'GNU General Public License v3 or later (GPLv3+)'  # see file LICENSE.TXT
__email__ = "charlietaylor@users.sourceforge.net"
__status__ = "4 - Beta"  # '1 - Planning','2 - Pre-Alpha','3 - Alpha','4 - Beta',
                         # '5 - Production/Stable','6 - Mature','7 - Inactive'

#
# import statements here. (built-in first, then 3rd party, then yours)
#
import sys
if sys.version_info < (3,):
    from future import standard_library
    standard_library.install_aliases()
    text = unicode
else:
    from builtins import str as text  # for python 2/3 unicode issues

import configparser
import stat
import datetime
from io import StringIO
import platform


# Man this is ugly... It's only used during development (prior to running
#   setup.py install) After installed, the pyhatch.xxxx should succeed for 2&3
try:
    from pyhatch.fill_template import get_file_template
    from pyhatch.license_templates import LICENSE_D, HEADER_D, CLASSIFIER_D
    from pyhatch.pySphinxLogo import save_logo_to_file
except:
    from fill_template import get_file_template
    from license_templates import LICENSE_D, HEADER_D, CLASSIFIER_D
    from pySphinxLogo import save_logo_to_file

# Code goes below.
#
# place config file in PyHatch code directory
USER_DATA_DIR = os.path.dirname( os.path.abspath( __file__ ) )
print( 'User Data Directory =',USER_DATA_DIR )
print('')
USER_HOME_DIR = os.path.dirname( os.path.expanduser('~/') )
print( 'User Home Directory =',USER_HOME_DIR )
print('')

DOC_TEMPLATE_DIR = os.path.join( USER_DATA_DIR, 'doc_templates' )
TEMPLATE_DIR = os.path.join( USER_DATA_DIR, 'templates' )

USER_DATA_CFG_FNAME = os.path.join( USER_HOME_DIR, 'PyHatch.cfg' )

print( 'User Config =',USER_DATA_CFG_FNAME )

generalIdL = [ 'author', 'proj_copyright', 'proj_license', 'version', 'email', 'github_user_name']
projectInfoL = ['mainPyFileName', 'mainDefinesClass',
                'mainClassName', 'mainFunctionName', 'status',
                'simpleDesc', 'longDesc']

CONFIG = configparser.SafeConfigParser()
if os.path.isfile(USER_DATA_CFG_FNAME):
    CONFIG.read(USER_DATA_CFG_FNAME)
else:
    CONFIG.add_section('generalId')
    for gid in generalIdL:
        CONFIG.set('generalId', gid, '')
    try:
        with open(USER_DATA_CFG_FNAME, 'w') as configfile:
            CONFIG.write( configfile )
    except:
        pass

DEV_STATUS_OPTIONS = (
    '1 - Planning',
    '2 - Pre-Alpha',
    '3 - Alpha',
    '4 - Beta',
    '5 - Production/Stable',
    '6 - Mature',
    '7 - Inactive')

class Hatch(object):
    """
    Hatch is main administrative class that creates a new project.

    Hatch gathers user data and builds new project with directory structure shown above.

    :param projName: (str) proper name of project ex. 'MyProject'. MUST start with capital letter.
    :param in_test_mode: (boolean) flag to indicate test mode or live mode
    :param mainPyFileName: (str) main file in code directory ex. "main.py"
    :param mainDefinesClass: (boolean) flag to indicate if mainPyFileName defines
        a class or function
    :param mainFunctionName: (str) name of function defined by mainPyFileName
    :param author: (str) author's name, ex. 'John Doe'
    :param proj_copyright: (str) copyright, ex. 'Copyright (c) 2013 John Doe'
    :param proj_license: (str) license, ex. 'GPL-3'
    :param version: (str) version, ex. '0.1.1'
    :param email: (str) author's email ex. "johndoe@happypond.org"
    :param status: (str) common values = "3 - Alpha", "4 - Beta", "5 - Production/Stable"
    :param simpleDesc: (str) short/simple description of project
    :param longDesc: (str) long description of project
    :param year: (str) or (int) year for copyright
    :param organization: (str) name of organization for copyright
    :param github_user_name: (str) user name at GitHub

    """

    def __init__(self, projName='MyProject', in_test_mode=False,
                 mainPyFileName='main.py', mainDefinesClass='Y',
                 mainClassName='MyClass', mainFunctionName='my_function',
                 author='', proj_copyright='',
                 proj_license='GPL-3', version='', email='', status='3 - Alpha',
                 simpleDesc='', longDesc='', year=None, organization=None,
                 github_user_name=''):
        """Inits Hatch.
        """

        # When in test mode, no files are written.
        self.in_test_mode = in_test_mode

        # save any inputs
        #    Set format of projName, strip and force 1st letter capital
        projName = projName.strip()
        projName = projName[:1].upper() + projName[1:]
        self.projName = projName

        self.mainPyFileName = mainPyFileName
        self.mainDefinesClass = mainDefinesClass
        self.mainClassName = mainClassName
        self.mainFunctionName = mainFunctionName
        self.author = author
        self.proj_copyright = proj_copyright
        self.github_user_name = github_user_name

        # print warning if proj_license is not recognized
        self.proj_license = proj_license
        if self.proj_license not in CLASSIFIER_D:
            self.print_proj_license_error()

        self.version = version
        self.email = email
        self.status = status
        if self.status not in DEV_STATUS_OPTIONS:
            self.print_proj_status_error()

        self.simpleDesc = simpleDesc
        self.longDesc = longDesc
        if year == None:
            self.year = datetime.date.today().year
        else:
            self.year = year
            
        self.date_str = datetime.date.today().strftime('%b %d, %Y')

        if organization == None:
            self.organization = author
        else:
            self.organization = organization

        # for general ID stuff, if not input, check CONFIG
        for gen_id in generalIdL:
            if not getattr(self, gen_id, ''): # if not input, check CONFIG
                if CONFIG.has_option('generalId', gen_id):
                    setattr(self, gen_id, CONFIG.get('generalId', gen_id))

    def print_proj_license_error(self):
        """Print Error Message for user input value of license"""
        if self.proj_license not in CLASSIFIER_D:
            print('='*20,' ERROR in Hatch Object ', '='*20)
            print('    proj_license = "%s" which is NOT in supported list.'%self.proj_license)
            print('    Accepted list =',CLASSIFIER_D.keys())
            print("    (if your's is not listed, pick one from above and correct it by hand later.)")
            print('='*55)

    def print_proj_status_error(self):
        """Print Error Message for user input value of project status"""
        if self.status not in DEV_STATUS_OPTIONS:
            print('='*20,' ERROR in Hatch Object ', '='*20)
            print('    status = "%s" which is NOT in supported list.'%self.status)
            print('    Accepted list =',DEV_STATUS_OPTIONS)
            print("    ")
            print('='*55)

    def save_project_below_this_dir(self, save_dir):
        '''Creates file layout of project'''

        # print warning and exit if proj_license is not recognized
        if self.proj_license not in CLASSIFIER_D:
            self.print_proj_license_error()
            return

        # print warning and exit if status is not recognized
        if self.status not in DEV_STATUS_OPTIONS:
            self.print_proj_status_error()
            return

        print( 'save_dir =',save_dir )
        print( 'os.path.abspath( save_dir )=',os.path.abspath( save_dir ) )

        save_dir =  os.path.abspath( save_dir )
        print( 'save_dir =',save_dir )

        projDir = os.path.join( save_dir, self.projName )
        print( 'projDir=',projDir )

        codeDir = os.path.join( projDir, self.projName.lower() )
        print( 'codeDir=',codeDir )

        testDir = os.path.join( projDir, self.projName.lower(), 'tests' )
        print( 'testDir=',testDir )

        docsDir = os.path.join( projDir, 'docs' )
        print( 'docsDir=',docsDir )

        examplesDir = os.path.join( projDir, self.projName.lower(), 'examples' )
        print( 'examplesDir=',examplesDir )

        docsStaticDir = os.path.join( docsDir, '_static' )
        print( 'docsStaticDir=',docsStaticDir )

        docsTemplateDir = os.path.join( docsDir, '_templates' )
        print( 'docsTemplateDir=',docsTemplateDir )
        print()

        if os.path.isdir( projDir ):
            print( 'ERROR... %s already exists'%projDir )
            return 'Dir Already Exists'
        else:

            # Update CONFIG file with current personal info
            for gen_id in generalIdL:
                if getattr(self, gen_id, ''): # if has a value
                    CONFIG.set('generalId', gen_id, getattr(self, gen_id))

            try:
                with open(USER_DATA_CFG_FNAME, 'w') as config_file:
                    CONFIG.write( config_file )
            except:
                pass


            # get dataD dictionary to build file contents strings
            dataD = {}
            for gen_id in generalIdL:
                dataD[gen_id] = getattr(self, gen_id, '')
            for pid in projectInfoL:
                dataD[pid] = getattr(self, pid, '')

            # build specialty dictionary entries
            dataD['projName_lower'] = self.projName.lower()
            dataD['projName'] = self.projName
            dataD['projName_rst'] = self.projName + '\n' + '='*len(self.projName)

            s = self.projName + " Code Functions"
            dataD['projCode_rst'] = s + '\n' + '='*len(s)

            s = self.projName + " Code Functions"
            dataD['projCode_rst'] = s + '\n' + '='*len(s)

            s = "Install " + self.projName
            dataD['install_projName_rst'] = s + '\n' + '-'*len(s)
            s = "Running " + self.projName
            dataD['running_projName_rst'] = s + '\n' + '-'*len(s)

            dataD['version'] = self.version
            dataD['author'] = self.author
            dataD['github_user_name'] = self.github_user_name
            dataD['email'] = self.email
            dataD['proj_license'] = self.proj_license
            dataD['status'] = self.status

            dataD['simpleDesc'] = self.simpleDesc
            dataD['simpleDesc_rst'] = self.simpleDesc.title() + '\n' + '='*len(self.simpleDesc)

            dataD['longDesc'] = self.longDesc
            dataD['year'] = self.year
            dataD['date_str'] = self.date_str
            dataD['organization'] = self.organization

            if self.proj_license in CLASSIFIER_D:
                dataD['license_classifier'] = CLASSIFIER_D[self.proj_license]
            else:
                dataD['license_classifier'] = 'License :: OSI Approved'


            if self.proj_license in  HEADER_D:
                dataD['license_header'] = HEADER_D[self.proj_license] % dataD
            else:
                dataD['license_header'] = ('%(projName)s\nCopyright (C)'+\
                      ' %(year)s  %(organization)s with license:%(proj_license)s') % dataD
            dataD['license_header'] =  dataD['license_header'] + '\n-----------------------\n'

            if self.mainPyFileName.endswith('.py'):
                dataD['mainPyFilePrefix'] = self.mainPyFileName[:-3]
            else:
                dataD['mainPyFilePrefix'] = self.mainPyFileName

            dataD['mainPyFileName'] = dataD['mainPyFilePrefix'] + '.py'

            if self.mainDefinesClass=='Y':
                dataD['func_or_class_name'] = self.mainClassName
                code_contents_str = get_file_template( TEMPLATE_DIR, 'Module_Class.py', dataD )

                # change Class_Test_File.py to Class_Te_st_File.py so nosetests won't find it
                test_contents_str = get_file_template( TEMPLATE_DIR, 'Class_Te_st_File.py', dataD )
                dataD['example_call'] = 'my_class = ' + dataD['mainClassName'] + '()'
            else:
                dataD['func_or_class_name'] = self.mainFunctionName
                code_contents_str = get_file_template( TEMPLATE_DIR, 'Module_Function.py', dataD )

                # change Function_Test_File.py to Function_Te_st_File.py so nosetests won't find it
                test_contents_str = get_file_template( TEMPLATE_DIR, 'Function_Te_st_File.py', dataD )
                dataD['example_call'] = 'my_result = ' + dataD['mainFunctionName'] + '()'

            def make_directory( dirName ):
                """Use os.mkdir to make directory.
                   If in test mode, only print test message
                """
                if self.in_test_mode:
                    print( "TESTING make dir:", dirName )
                else:
                    print( "Making dir:",dirName )
                    os.mkdir( dirName )

            # Start making directories
            make_directory( projDir )
            make_directory( codeDir )
            make_directory( testDir )
            make_directory( docsDir )
            make_directory( docsStaticDir )
            make_directory( docsTemplateDir )
            make_directory( examplesDir )

            def create_file( sdir, file_name, contents=''):
                """Create a file called file_name in directory sdir with
                   contents.
                """
                fname = os.path.join( sdir, file_name )
                if self.in_test_mode:
                    print( "TESTING make file:", fname )
                    f = StringIO()
                    contents = text(contents)
                else:
                    print( "Making file:", fname )
                    f = open(fname, 'w')
                f.write(contents)
                f.close()

                if not self.in_test_mode:
                    # Make sure permissions on file are good for owner
                    st = os.stat(fname)
                    if file_name.endswith('.py'):
                        # read/write/execute by owner
                        os.chmod(fname, st.st_mode | stat.S_IRWXU)
                    else:
                        # read & write by owner
                        os.chmod(fname, st.st_mode | stat.S_IREAD | stat.S_IWRITE)

            #create_file( codeDir, '__init__.py', contents='')
            create_file( codeDir, self.mainPyFileName, contents=code_contents_str)

            # NOTE: pytest.org advises AGAINST putting __init__.py into the test dir.
            #  comment the following line if you agree.
            create_file( testDir, '__init__.py', contents='') # allows "setup.py test" to work
            #  ???????????????????????????????????????????????

            create_file( testDir, 'test_'+self.mainPyFileName, contents=test_contents_str)

            #print( 'dataD =',dataD )
            def place_template_file(dest_dir, fname ):
                """Get template string from template subdirectory, render template
                   and save to dest_dir
                """
                s = get_file_template( TEMPLATE_DIR, fname, dataD )
                create_file( dest_dir, fname, contents=s )

            place_template_file( codeDir, '__init__.py' )
            place_template_file( codeDir, '_version.py' )

            place_template_file( projDir, 'setup.cfg' )
            place_template_file( projDir, 'README.rst' )
            place_template_file( projDir, 'HISTORY.rst' )
            place_template_file( projDir, 'AUTHORS.rst' )
            place_template_file( projDir, 'MANIFEST.in' )
            place_template_file( projDir, 'setup.py' )
            place_template_file( projDir, 'history_from_github_api.py')
            place_template_file( projDir, 'metadata_reset.py' )

            place_template_file( projDir, '.pypirc' )
            #place_template_file( projDir, 'tk_nosy.py' )

            if platform.system() == "Windows":
                create_file( projDir, 'tox.ini', contents=get_file_template(
                             TEMPLATE_DIR, 'tox_windows.ini', dataD ) )
            else:
                create_file( projDir, 'tox.ini', contents=get_file_template(
                             TEMPLATE_DIR, 'tox_linux.ini', dataD ) )


            place_template_file( examplesDir, 'example_1.py' )

            # requirements.txt is empty, just a place-holder to edit later
            place_template_file( projDir, 'requirements.txt' )

            # If using GitHub, Travis CI can be used to verify code on check-in
            place_template_file( projDir, '.travis.yml' )

            # Get license text from LICENSE_D
            create_file( projDir, 'LICENSE.txt', contents=LICENSE_D[self.proj_license]%dataD )

            # Make sphinx doc files
            for fname in ['index.rst', 'Makefile', 'fulltoc.py', 'functions.rst',
                          'conf.py', 'sphinxy.py', 'keyboard_hit.py', 'make.bat',
                          'history.rst', 'build_all_html.py', 'authors.rst',
                          'quickstart.rst']:
                s = get_file_template( DOC_TEMPLATE_DIR, fname, dataD )
                create_file( docsDir, fname, contents=s )

            logoName = os.path.join( docsStaticDir, 'PythonSphinxlogo.png' )
            save_logo_to_file( logoName, in_test_mode=self.in_test_mode )

            return 'Success'

        return 'Hmmm Unusual Return'


if __name__ == '__main__':
    # pylint: disable=W0142


    if 1:
        PROJ_D = {'status': '4 - Beta',
                  'proj_copyright': 'Copyright (c) 2015 Charlie Taylor',
                  'proj_license': 'GPL-3', 'author': 'Charlie Taylor',
                  'longDesc': "MyProject tests the creation of a project using"+\
                  " pyHatch.\nShould be a piece of cake... but might not be, "+\
                  "so I test.",
                  'mainClassName': 'MyClass',
                  'simpleDesc': 'My project does this',
                  'version': '0.1.1', 'mainPyFileName': 'main.py',
                  'email': 'cet@appliedpython.com',
                  'mainFunctionName': 'my_function',
                  'mainDefinesClass': 'Y', 'github_user_name':'GitHub_GooRoo'}

        h = Hatch(projName='DocSampCase9', in_test_mode=True, **PROJ_D)
        h.save_project_below_this_dir( r'D:\temp' )

