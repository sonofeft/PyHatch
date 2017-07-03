

TODO List
=========

* Add tox/pip setup advice from:
    - http://blog.ionelmc.ro/2015/01/02/speedup-pip-install/
        Per-user:

        On Unix the default configuration file is: $HOME/.config/pip/pip.conf which respects the XDG_CONFIG_HOME environment variable.
        On Mac OS X the configuration file is $HOME/Library/Application Support/pip/pip.conf.
        On Windows the configuration file is %APPDATA%\pip\pip.ini.
        There are also a legacy per-user configuration file which is also respected, these are located at:

        On Unix and Mac OS X the configuration file is: $HOME/.pip/pip.conf
        On Windows the configuration file is: %HOME%\pip\pip.ini    

* Make script to publish
    - update version
    - make history file
    - register with PyPI
    - upload to PyPI
    - commit to GitHub as version x.x.x

* Strip trailing spaces in all template files.

* Add option for console shortcut 
    - (i.e. entry_points/console_scripts in setup.py)

* Add tags to GitHub for version changes???
    git tag -a v1.4 -m 'my version 1.4'
    git push --tags

* On linux, tries to compile template `*.py` files.

* launch_tk_nosy script

* add tk_nosy to requirements.txt ?????

    (maybe just a recommended installs page... twinw, tk_nosy, ...)

* add "Support python 2, 3 and pypy, pypy3 options ????

* Make checklist with actual project names in it from checklist template

