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
import s_interface
import simpl
# --------------------------------------------
# Подготовительная секция, не забыть перенести
d1 = datetime.datetime(2013, 8, 1)
d2 = datetime.datetime(2013, 8, 31)

class BDTests(unittest.TestCase):

	def test_1(self):
		print (u"test 1 Итоги по автопарку")
		reportName = "ObjectTotals"
		simpl.reportTest1(reportName,d1,d2)

	def test_2(self):
		print (u"test 2 Итоги по автопарку по дням")
		reportName = "ObjectTotalsByDay"
		simpl.reportTest1(reportName,d1,d2)

		
	def test_0(self):
		print "test 0"
		#tmp.timer()

suite = unittest.TestLoader().loadTestsFromTestCase(BDTests)
outPath =  os.path.join(os.environ.get("GIT_HOME"),"tmp-report.html") # Вариант с путём без кирилицы и именами без пробелов  
try:
	outfile = open(outPath, "w")
	print "open file ", outPath
	runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Tmp Report', description='This is demo' )
	runner.run(suite)
	outfile.close()
except:
	print "Don't open file ", outPath.encode("UTF-8")



