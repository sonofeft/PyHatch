""" Visit https://developer.github.com/v3/repos/statistics/
    for API tips.

    This code builds the HISTORY.rst file using the GitHub API

"""

#    I like extra spaces inside parens and sometimes camelCase
# pylint: disable=C0326, C0325
# pylint: disable=C0103

import requests
import os
import datetime
import getpass

GITHUB_USER = '{{github_user_name}}'

here = os.path.abspath(os.path.dirname(__file__))
print( '='*55 )
print( '     Building HISTORY.rst file' )
print( '     at: ' + here )
print( '     Need GitHub user password for ' + GITHUB_USER)
print( '='*55 )
PASSWORD = getpass.getpass(prompt='Enter Password: ')

github_url = "https://api.github.com/repos/{{github_user_name}}/{{projName}}/commits"
headers = {'content-type': 'application/json'}

t = requests.get(github_url, auth=(GITHUB_USER,PASSWORD))

fOut = open(os.path.join(here, 'HISTORY.rst'), 'w')
fOut.write("""

History
=======

GitHub Log
----------

""")


print( 'len(t.json()) =' + '%s'%len(t.json()) )
last_date_str = ''
last_author_str = ''
for D in t.json():
    date_str = D['commit']['author']['date'][:10]
    author_str = D['commit']['author']['name']

    if date_str != last_date_str:
        com_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        fOut.write( '* ' + com_date.strftime('%b %d, %Y') + '\n' )

    if (date_str != last_date_str) or (author_str != last_author_str):
        fOut.write( '    '  +'- (by: %s) '%author_str + '\n' )

    msgL = D['commit']['message'].split('\n')
    pad = '        - '
    for msg in msgL:
        if msg:
            fOut.write(pad + '%s'%msg + '\n' )
        else:
            pad = '            '



    print( D['commit']['author']['date'][:10] + ' ' + D['commit']['message'] )

    last_date_str = date_str
    last_author_str = author_str

fOut.write("""
* {{date_str}}
    - (by: {{github_user_name}})
        - First Created {{projName}} with PyHatch
""")


fOut.close()
