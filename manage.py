#!/usr/bin/env python
import site 
import os

try:
    import settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings.development module.\n(If the file settings.development.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if settings.DEBUG == True:
    activate_this = "/var/lib/virtualenvs/twyck/bin/activate_this.py"
else:
    if os.path.exists('/home/powellc'):
        activate_this = "/home/powellc/.virtualenvs/twyck/bin/activate_this.py"
    else:
        activate_this = "/Users/powellc/.virtualenvs/twyck/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))


if settings.VIRTUALENV:
    site.addsitedir(settings.VIRTUALENV)

from django.core.management import execute_manager
if __name__ == "__main__":
    execute_manager(settings)
