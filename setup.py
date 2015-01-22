#!/usr/bin/env python

import sys
from PyQt4 import uic

if len(sys.argv) < 1:
    print "You must supply a command (build, install, etc.) to this program"
    sys.exit()

command = sys.argv[0]

