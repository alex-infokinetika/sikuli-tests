from sikuli import *
# -*- coding: utf-8 -*-
import os
import sys
import datetime
import time



myPath = os.path.join(os.environ.get("GIT_HOME"), u"sikuli-tests")
if not myPath in sys.path:
	sys.path.append(myPath)
# Импорт ------------------------------
import baseFunction as BF

# Если отчёт в конце списка, т.е. его не видно на панели сразу, прокручиваем список отчётов до конца и смотрим ещё раз
def findReportOnPanel(pattern):
	try:
		find(pattern)
	except:
		click(Pattern("scrol_down-1.png").similar(0.90).targetOffset(-4,0))
		mouseDown( Button.LEFT)
		sleep(10)
		mouseUp()
		find(pattern)

def startReport(patternList):
	try:
		findReportOnPanel(patternList[0])
		click(patternList[0])
		click("runReport-1.png")		
	except:
		print (u"Не нашли отчёт на панели")
		BF.killAllNavstat()
		exit(0)	
	try:
		find("question-1.png")
		try:
			click("da-2.png")
		except:
			print (u"Такой файл уже есть, но не нашёл кнопку 'Да'")
			exit(0)
	except:
		print (u".")
	try:
		reportStart = time.time()
		print (u"Стартанули таймер")
		BF.waitAll(patternList,2000)
		print (u"Отчёт выполнен за "), datetime.timedelta(seconds=time.time()-reportStart)
	except:
		print (u"Отчёт не выполнен или результат не корректен")
		BF.killAllNavstat()
		exit(0)

# Общая проверка отчётов, подходит для: Общие отчёты, События и сигналы, Отраслевые 
def reportTest1(reportName, startDay, endDay):
# ------ Подготовка к тесту --------------------	
	start = time.time()
	baseDir = os.path.join(os.environ.get("GIT_HOME"), u"sikuli-tests", u"img", u"report_1")
	fList = os.listdir(os.path.join(baseDir,reportName));
	patternList = []
	for f in fList:
		patternList.append(os.path.join(baseDir,reportName,f))
	BF.clearData()
#	keyer.editKeyAndService("404C2A00-B173-4844-BA59-9A6F296479E7", "http://services.navstat.infokinetika.net")
	BF.firstStartNavstat()
# Переходим на таб отчётов (просто закрыв таб с картой)
	BF.closeCurTab()
	click(Pattern("6917gag-1.png").similar(0.80).targetOffset(-1,0)) # Заглушка http://idea.navstat.ru/tickets/6917
# ------ Тест --------------------	
	BF.setInterval(startDay, endDay) #Устанавливаем интервал отчёта
	startReport(patternList) #Выполнили отчёт
	BF.saveReportAsCSV(reportName) #Сохранили отчёт в файл
	BF.mergeFile(reportName) #Сравнили файл с эталоном
	print (u"Время выполнения теста: "), datetime.timedelta(seconds=time.time()-start)
	BF.killAllNavstat()