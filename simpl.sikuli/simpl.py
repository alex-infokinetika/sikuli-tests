from sikuli import *
# -*- coding: utf-8 -*-
import os
import time
import datetime


myPath = os.environ.get("GIT_HOME") + u"sikuli-tests"
if not myPath in sys.path:
	sys.path.append(myPath)
# Импорт ------------------------------
import baseFunction as BF

try:
	BF.waitVanishAll([Pattern("mini_map.png").similar(0.90),Pattern("blue_rect.png").similar(0.80),Pattern("mini_map_close_2.png").similar(0.80)])
	print "go"
except:
	exit(1)