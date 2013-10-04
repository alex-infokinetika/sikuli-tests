from sikuli import *
# -*- coding: utf-8 -*-
import os


myPath = os.environ.get("GIT_HOME") + u"sikuli-tests"
if not myPath in sys.path:
	sys.path.append(myPath)
# Импорт ------------------------------
import baseFunction as BF
