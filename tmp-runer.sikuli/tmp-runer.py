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
#import base_report_test 
import simpl as BRT
# --------------------------------------------
# Подготовительная секция, не забыть перенести
d1 = datetime.datetime(2013, 8, 1)
d2 = datetime.datetime(2013, 8, 3)

class BDTests(unittest.TestCase):

	def test_1(self):
		print (u"test 1 Итоги по автопарку")
		reportName = "ObjectTotals"
		BRT.reportTest1(reportName,d1,d2)

	def test_2(self):
		print (u"test 2 Топливные баки, Статистика по топливу")
		reportName = "ReportFuelStatistics"
		BRT.reportTest1(reportName,d1,d2,'fuel')

	def test_3(self):
		print (u"test 3 Топливозаправщик, Детализация показаний датчиков")
		reportName = "ReportFuelRecharge"
		BRT.reportTest1(reportName,d1,d2, 'bigFuel')

	def test_4(self):
		print (u"test Топливные карты, Итоги")
		reportName = "ReportFcTotal"
		BRT.reportTest1(reportName,d1,d2, 'Fc')

	def test_5(self):
		print (u"test 5 Путевой лист")
		reportName = "RouteList"
		#BRT.reportTest1(reportName,d1,d2)
		
	def test_6(self):
		print (u"test 6 Стоянки")
		reportName = "Parkings"
		#BRT.reportTest1(reportName,d1,d2)

	def test_7(self):
		print (u"test 7 Контроль прохождения зон интереса")
		reportName = "HistoryGet"
		#BRT.reportTest1(reportName,d1,d2)

	def test_8(self):
		print (u"test 8 Отчёт по моточасам")
		reportName = "MotoHistory"
		#BRT.reportTest1(reportName,d1,d2)

	def test_20(self):
		print (u"test 20 Уборка мусора ")
		reportName = "GarbageHistory"
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



