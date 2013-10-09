from sikuli import *
# -*- coding: utf-8 -*-
import os
import datetime
import time

myPath = os.path.join(os.environ.get("GIT_HOME"), u"sikuli-tests")
if not myPath in sys.path:
	sys.path.append(myPath)
# Импорт ------------------------------
import baseFunction as BF

def fff():
	d1 = datetime.datetime(2013, 8, 1)
	d2 = datetime.datetime(2013, 8, 31)
	BF.setInterval(d1,d2)

	
#fff()


def reportTest1(reportName, startDay, endDay):
	start = time.time()
	baseDir = os.path.join(os.environ.get("GIT_HOME"), u"sikuli-tests", u"img", u"report_1")
	fList = os.listdir(os.path.join(baseDir,reportName));
	patternList = []
	for f in fList:
		patternList.append(os.path.join(baseDir,reportName,f))
	print patternList
	BF.clearData()
#	keyer.editKeyAndService("404C2A00-B173-4844-BA59-9A6F296479E7", "http://services.navstat.infokinetika.net")
	BF.firstStartNavstat()
# Переходим на таб отчётов (просто закрыв таб с картой)
	BF.closeCurTab()
	click(Pattern("6917gag.png").similar(0.80).targetOffset(-1,0)) # Заглушка http://idea.navstat.ru/tickets/6917
	BF.setInterval(startDay, endDay)
	type(Key.TAB) #затычка чтобы снять фокус с отчёта Итоги по автопарку, т.е. сделать его похожим на остальные
	click(patternList[0])
	click("runReport.png")
	try:
		find("question.png")
		click("da.png")
	except:
		print (u".")
	try:
		reportStart = time.time()
		BF.waitAll(patternList,2000)
		print (u"Отчёт выполнен за "), datetime.timedelta(seconds=time.time()-reportStart)
	except:
		print (u"Отчёт не выполнен или результат не корректен")
		type(Key.F4, KeyModifier.ALT)
		exit(0)
	print (u"Время выполнения теста: "), datetime.timedelta(seconds=time.time()-start)
	type(Key.F4, KeyModifier.ALT)