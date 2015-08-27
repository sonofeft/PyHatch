"""PyHatch __init__ module"""

import os

# pylint: disable=C0326, C0103, W0122

here = os.path.abspath(os.path.dirname(__file__))

#  execfile( os.path.join(here,'_version.py')) # creates local __version__ variable
exec( open(os.path.join( here,'_version.py' )).read() )  # creates local __version__ variable
