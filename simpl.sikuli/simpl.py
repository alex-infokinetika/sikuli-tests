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

def saveReportAsCSV(reportName): # Отчёт должен быть уже сгенерирован. Временный файл сохраняет в папке %GITHOME%
	try:
		click("save_icon.png")
		click("data_icon.png")
		click("csv_icon.png")
		sleep(3)
		type(Key.ENTER)
		click(Pattern("addres_line-1.png").targetOffset(-24,-1))
		type(os.path.join(os.environ.get("GIT_HOME")))
		type(Key.ENTER)
		click(Pattern("name_line.png").similar(0.90).targetOffset(-12,-10))
		type(reportName + u".csv")
		type(Key.ENTER)
		try:
			find("rewrite.png")
			click("da-1.png")
		except:
			pass
	except:	
		print (u"blin")



def mergeFile(reportName):
	list1 = []
	list2 = []
	fName = reportName + ".csv" 
	shablon = os.path.join(os.environ.get("GIT_HOME"),"sikuli-tests","shablony","report_1",fName)
	testReport = os.path.join(os.environ.get("GIT_HOME"),fName)
	try:
		print (u"Файл шаблона : ",shablon)
		f1 = open(shablon, 'r')
		reader = csv.reader(f1)
		for row in reader:
			list1.append(row)
		f1.close()
	except: 
		(u"Файл шаблона не найден!")
	try:
		print (u"Тестовый фаил: ",testReport)
		f2 = open(testReport, 'r')
		reader = csv.reader(f2)
		for row in reader:
			list2.append(row)
		f2.close()
	except:
		print (u"Тестовый фаил не найден!")
	try:
		if list1 == list2:
			print (u"Тестовый файл совпадает с эталоном")
		else:
			print (u"Обнаружены отличия между файлами:")
			for i in range(len(list1)-1):
				if list1[i] == list2[i]:
					print (u"Строка %i совпадает" % i)
				else:
					print (u"Строка %i несовпадает: " % i)
					print str(list1[i]).decode('cp1251')
					print list2[i]
			raise()
	except:
		print (u"Отчёт не совпал с эталоном!")
		BF.killAllNavstat()
		exit(1)




def findReportOnPanel(pattern):
	try:
		find(pattern)
	except:
		click(Pattern("scrol_down.png").similar(0.90).targetOffset(-4,0))
		mouseDown( Button.LEFT)
		sleep(10)
		mouseUp()
		find(pattern)


def reportTest1(reportName, startDay, endDay):
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
	click(Pattern("6917gag.png").similar(0.80).targetOffset(-1,0)) # Заглушка http://idea.navstat.ru/tickets/6917
	BF.setInterval(startDay, endDay)
	try:
		findReportOnPanel(patternList[0])
		click(patternList[0])
		click("runReport.png")		
	except:
		print (u"Не нашли отчёт на панели")
		BF.killAllNavstat()
		exit(0)	
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
		BF.killAllNavstat()
		exit(0)
	saveReportAsCSV(reportName)
	mergeFile(reportName)
	sleep(3)
	print (u"Время выполнения теста: "), datetime.timedelta(seconds=time.time()-start)
	BF.killAllNavstat()