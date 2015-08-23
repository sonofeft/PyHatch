import os

here = os.path.abspath(os.path.dirname(__file__))

#  execfile( os.path.join(here,'_version.py')) # creates local __version__ variable
exec( open(os.path.join( here,'_version.py' )).read() )  # creates local __version__ variable