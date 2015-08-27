#!/usr/bin/env python
# -*- coding: ascii -*-

"""Gets Version Info from PyPI for package_name"""
# pylint: disable=C0326, C0103
#import json
import requests
from distutils.version import StrictVersion

FIRST_VERSION = '0.1.1'   # Assumed starting version

def versions(package_name):
    """Get all version numbers on PyPI for package_name"""
    url = "https://pypi.python.org/pypi/{}/json".format(package_name)
    data = requests.get(url).json()
    return sorted(list(data["releases"].keys()), key=StrictVersion, reverse=True)

def newest_version(package_name):
    """Get newest version number from PyPI for package_name"""
    versionL = versions(package_name)
    if versionL:
        return versionL[0]
    else:
        return None

def inc_version( ipos, vstr ):
    """Increment version string at postion, ipos
       for micro, ipos == 2
       for minor, ipos == 1
       for major, ipos == 0
    """
    sL = vstr.split('.')
    sL[ipos] = '%i'%( int(sL[ipos]) + 1 )
    if ipos == 0: # for inc major, zero minor and micro
        sL[1]='0'
        sL[2]='0'
    elif ipos==1: # for inc minor, zero micro
        sL[2]='0'
    return '.'.join(sL)

def next_micro_version(package_name):
    """Get next micro version of package_name, based on PyPI latest version"""
    curr_ver = newest_version(package_name)
    if curr_ver:
        return inc_version( 2, curr_ver )
    else:
        return FIRST_VERSION # Assumed starting version

def next_minor_version(package_name):
    """Get next minor version of package_name, based on PyPI latest version"""
    curr_ver = newest_version(package_name)
    if curr_ver:
        return inc_version( 1, curr_ver )
    else:
        return FIRST_VERSION # Assumed starting version


def next_major_version(package_name):
    """Get next major version of package_name, based on PyPI latest version"""
    curr_ver = newest_version(package_name)
    if curr_ver:
        return inc_version( 0, curr_ver )
    else:
        return FIRST_VERSION # Assumed starting version


if __name__ == "__main__":

    #print "\n".join(versions("scikit-image"))
    pkg_name = "scikit-image"
    print 'Versions for',pkg_name
    verL = versions(pkg_name)
    if verL:
        print 'Newest Version =', verL[0]
    else:
        print 'No Versions Available'

    print
    print 'newest_version =',newest_version(pkg_name)
    print 'next_micro_version =',next_micro_version(pkg_name)
    print 'next_minor_version =',next_minor_version(pkg_name)
    print 'next_major_version =',next_major_version(pkg_name)


