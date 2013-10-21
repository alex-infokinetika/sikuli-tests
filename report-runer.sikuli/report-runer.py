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
# --------------------------------------------
# Подготовительная секция, не забыть перенести
d1 = datetime.datetime(2013, 8, 16)
d2 = datetime.datetime(2013, 8, 18)

class BDTests(unittest.TestCase):
# ------------------------------------------------Общие отчёты
	def test_1(self):
		print (u"test 1 Итоги по автопарку")
		reportName = "ReportObjectTotals"
		BRT.reportTest1(reportName,d1,d2)

	def test_2(self):
		print (u"test 2 Итоги по автопарку по дням")
		reportName = "ReportObjectTotalsByDay"
		BRT.reportTest1(reportName,d1,d2)

	def test_3(self):
		print (u"test 3 Скоростной режим")
		reportName = "ReportSpeedStatistic"
		BRT.reportTest1(reportName,d1,d2)

	def test_4(self):
		print (u"test Маршрутный лист")
		reportName = "ReportRouteList"
		BRT.reportTest1(reportName,d1,d2)

	def test_5(self):
		print (u"test 5 Путевой лист")
		reportName = "ReportPathList"
		BRT.reportTest1(reportName,d1,d2)
		
	def test_6(self):
		print (u"test 6 Стоянки")
		reportName = "ReportParkings"
		BRT.reportTest1(reportName,d1,d2)

	def test_7(self):
		print (u"test 7 Контроль прохождения зон интереса")
		reportName = "ReportInterestPointsHistory"
		BRT.reportTest1(reportName,d1,d2)

	def test_8(self):
		print (u"test 8 Отчёт по моточасам")
		reportName = "ReportIceMotoHistory"
		BRT.reportTest1(reportName,d1,d2)
# ------------------------------------------------ События и сигналы
	def test_9(self):
		print (u"test 9 События")
		reportName = "ReportEventsHistory"
		BRT.reportTest1(reportName,d1,d2)

	def test_10(self):
		print (u"test 10 Тревожные сигналы")
		reportName = "ReportAlarmStatistic"
		BRT.reportTest1(reportName,d1,d2)
# ------------------------------------------------ Топливные баки
	def test_10(self):
		print (u"test 11 Топливо и смены (Топливные баки)")
		reportName = "ReportFuelAndShiftwork"
		BRT.reportTest1(reportName,d1,d2,'Fuel')
	def test_11(self):
		print (u"test 12 Статистика по топливу (Топливные баки)")
		reportName = "ReportFuelStatistics"
		BRT.reportTest1(reportName,d1,d2,'Fuel')
	def test_12(self):
		print (u"test 13 Детализация погазаний датчиков (Топливные баки)")
		reportName = "ReportFuelLevel"
		BRT.reportTest1(reportName,d1,d2,'Fuel')
	def test_13(self):
		print (u"test 14 Заправки и возможные сливы (Топливные баки)")
		reportName = "ReportFuelRecharge"
		BRT.reportTest1(reportName,d1,d2,'Fuel')
# ------------------------------------------------ Топливозаправщик
	def test_14(self):
		print (u"test 14 Статистика по топливу")
		reportName = "ReportFuelStatisticsBig"
		BRT.reportTest1(reportName,d1,d2,'bigFuel')
	def test_15(self):
		print (u"test 15 Детализация погазаний датчиков")
		reportName = "ReportFuelLevelBig"
		BRT.reportTest1(reportName,d1,d2,'bigFuel')
	def test_16(self):
		print (u"test 16 Заправки и возможные сливы")
		reportName = "ReportFuelRechargeBig"
		BRT.reportTest1(reportName,d1,d2,'bigFuel')
# ------------------------------------------------ Топливные карты
	def test_17(self):
		print (u"test 15 Итоги (Топливные карты)")
		reportName = "ReportFuelLevel"
		BRT.reportTest1(reportName,d1,d2,'Fc')
	def test_18(self):
		print (u"test 16 Заправки")
		reportName = "ReportFuelRecharge"
		BRT.reportTest1(reportName,d1,d2,'Fc')
# ------------------------------------------------ Отраслевые
	def test_19(self):
		print (u"test 19 Уборка мусора")
		reportName = "ReportGarbage"
		BRT.reportTest1(reportName,d1,d2,'Spec')
	def test_20(self):
		print (u"test 20 Уборка мусора")
		reportName = "ReportGarbage"
		BRT.reportTest1(reportName,d1,d2,'Spec')



	def test_0(self):
		print (u"test 0 Пустой ")


suite = unittest.TestLoader().loadTestsFromTestCase(BDTests)
outPath =  os.path.join(os.environ.get("GIT_HOME"),"report-runer.html") # Вариант с путём без кирилицы и именами без пробелов  
try:
	outfile = open(outPath, "w")
	print "open file ", outPath
	runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Report Report', description='This is demo' )
	runner.run(suite)
	outfile.close()
except:
	print "Don't open file ", outPath.encode("UTF-8")



