# -*- coding: utf-8 -*-
import os
import unittest
import HTMLTestRunner
import datetime
import time

myPath = os.environ.get("GIT_HOME") + u"sikuli-tests"
if not myPath in sys.path:
	sys.path.append(myPath)
# Импорт тестов ------------------------------
#import s_interface
import base_report_test as BRT
#import simpl as BRT
# --------------------------------------------
# Подготовительная секция, не забыть перенести
d1 = datetime.datetime(2013, 8, 16)
d2 = datetime.datetime(2013, 8, 18)

class BDTests(unittest.TestCase):

# ------------------------------------------------ Топливные баки

	def test_9(self):
		print (u"test 9 События")
		reportName = "ReportEventsHistory"
		BRT.reportTest1(reportName,d1,d2)
		
	def test_0(self):
		print (u"test 0 Пустой ")

suite = unittest.TestLoader().loadTestsFromTestCase(BDTests)
outPath =  os.path.join(os.environ.get("GIT_HOME"),"tmp-runer.html") # Вариант с путём без кирилицы и именами без пробелов  
try:
	outfile = open(outPath, "w")
	print "open file ", outPath
	runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Tmp Report', description='This is demo' )
	runner.run(suite)
	outfile.close()
except:
	print "Don't open file ", outPath.encode("UTF-8")



