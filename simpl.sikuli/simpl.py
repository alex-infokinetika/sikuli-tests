from sikuli import *
# -*- coding: utf-8 -*-
import os
import sys
import datetime
import time
import csv



myPath = os.path.join(os.environ.get("GIT_HOME"), u"sikuli-tests")
if not myPath in sys.path:
	sys.path.append(myPath)
# Импорт ------------------------------
import baseFunction as BF

def starttimer():
	try:
		start = time.time()
		BF.startNavstat()
		print ("Стар выполнен за"), datetime.timedelta(seconds=time.time()-start)
		BF.killAllNavstat()
	except:
		print ("Старт не выполнен за 200 секунд")
		BF.killAllNavstat()

