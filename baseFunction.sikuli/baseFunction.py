from sikuli import *
# -*- coding: utf-8 -*-
import os
import sys
import shutil
import time
import datetime
import csv

def deleteFileOrFolder(directory):
	if os.path.exists(directory):
		try:
			if os.path.isdir(directory):
				# delete folder
				shutil.rmtree(directory)
			else:
				# delete file
				os.remove(directory)
		except:
			print "Ecxeption ",str(sys.exc_info())
	else:
		print "not found ",directory


def clearData():
	batPath = os.path.join(os.environ.get("GIT_HOME"), u"sikuli-tests", u"baseFunction.sikuli", u"clear.bat")

	try:
		os.system(batPath)
		print (u"Папка NavstatExpress удалена")
		return 1
	except:
		print (u"Папка NavstatExpress не удалена!")
		return 0

def killAllNavstat():
	if os.system('taskkill /f /im Infokinetika.Navstat.Express.exe'): # Почему-то возвращает true когда не смогла убить процесс
		print(u"Не закрылся Навстат!")
		exit(13)
	else:
		print(u"Закрыли Навстат")

def startNavstat(userName = u"admin", password = u"admin"):
	try:
		navstat = os.path.join(os.environ.get("GIT_HOME"),u"sikuli-tests",u"navstat.appref-ms")
		os.system(navstat)
		print (u"Запустили Навтат")
	except:
		print (u"Навтат не запустился, что-то с файлом navstat.appref-ms!")
		exit(90)
	try:
		wait("1376485054733.png",100)
		print (u"Обновлений нет")
	except:
		print (u"Похоже есть обновления")
		try:
			wait("1379065887261.png")
			print(u"Есть обновления")
			click("update_butt.png")
			click(Pattern("update_available.png").targetOffset(48,74))
			wait("error_pres_ok.png",60)
			click(Pattern("error_pres_ok.png").targetOffset(95,49))
			print (u"Обновили Навстат")
			try:
				navstat = os.path.join(os.environ.get("GIT_HOME"),u"sikuli-tests",u"navstat.appref-ms")
				os.system(navstat)
				print (u"Запустили Навтат")
			except:
				print (u"Навтат не запустился, что-то с файлом navstat.appref-ms!")
				exit(91)
			try:
				wait("1376485054733.png",100)
				print (u"Обновлений больше нет")
			except:
				print (u"Навстат не запустился после обновления")
				exit(92)
		except:
			print (u"Обновиться не удалось")
			exit(93)
		exit(94)
	try:
		type(Pattern("VnO1Tb3OBBT1.png").targetOffset(42,2), userName.encode("UTF-8"))
		type(Key.TAB)
		type(password.encode("UTF-8"))
		click("OK.png")
		print (u"Ввели логин и пароль, нажали OK")
	except:
		print (u"Вволдили логин и пароль, нажали OK - что-то пошло не так!")
		exit(95)
		try:
			wait(Pattern("NAVSTAT-1.png").similar(0.80), 1300)
			print (u"Навстат запустился")
		except:
			print (u"Навстат не запустился")
			exit(96)
		exit(97)


def firstStartNavstat(userName = u"admin", password = u"admin"):
	try:
		startNavstat(userName, password)
	except:
		exit(111)
	wait(Pattern("Vlcropvmvrsm.png").targetOffset(64,-1),300)
	try:
		click(Pattern("Vlcropvmvrsm.png").targetOffset(64,-1))
		print (u"Первичный запуск Навстат")
	except:
		print (u"Это не первичный запуск Навстат")
		exit(112)

# аналог wait принимает на вход список картинок и время ожидания в секундах, возвращает номер найденной картинки
# если не дождались - вызываем исключение
def waitList(imgList, timer=3):
	start = time.time() + timer
	while start > time.time():
		print " --- ", start, " - ", time.time(), " = ", start-time.time()
		i=0
		while i < len(imgList):
			print "Find ", i
			try:
				find(imgList[i])
				return i
			except:
				print("Don't find ")
			i+=1
	assert(false)
# аналог wait принимает на вход список картинок и время ожидания в секундах, возвращает 1 если нашёл все картинки из списка
# если не дождались - вызываем исключение
def waitAll(imgList, timer=3):
	start = time.time() + timer
	while start > time.time():
		res = 1
		for img in imgList:
			try:
				find(img)
			except:
				res = -1
		if res == 1:
			return 1
	assert(false)

# аналог waitVanish принимает на вход список картинок и время ожидания в секундах, возвращает 1 если все картинки из списка исчезли
# если за время timer хоть одна картинка не исчезла - вызываем исключение
def waitVanishAll(imgList, timer=3):
	start = time.time() + timer
	while start > time.time():
		res = -1
		for img in imgList:
			if not waitVanish(img):
				res = 1
				break
		if res == -1:
			return 1
	assert(false)
# Установка периода для отчётов и истории -----------------------------------------------------------------
def setInterval(day1, day2):
	# Навстат должен быть запущен и открыта панель с датапикером
	doubleClick(Pattern("3GlpHOJ1BDBM.png").targetOffset(-39,-4))
	paste(day1.strftime("%d.%m.%Y "))
	doubleClick(Pattern("3GlpHOJ1BDBM.png").targetOffset(-37,23))
	paste(day2.strftime("%d.%m.%Y "))
# ---------------------------------------------------------------------------------------------------------

# просто закрывает активный таб
def closeCurTab():
	try:
		wait("1379333077365-1.png")
		click("1379333077365-1.png")
		return 1
	except:
		return 0

# Открывает новый таб с картой
def newMapTab():
	wait("1379333330757.png")
	click("1379333330757.png")

# Сохранение отчёта в директорию %GIT_HOME%\
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
		sleep(3)
		waitVanish("report_export.png")
	except:	
		print (u"blin")
		exit(200)

# ---------------------------------------------------------------------------------------------------------------------
# Сравнение .csv файла расположенного в %GIT_HOME%\ с эталоном из директории %GIT_HOME%\sikuli-tests\shablony\report_1\
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
		# Фактически сюда мы не попадаем, csv.reader не отличает пустой файл от отсутствующего - это надо исправлять
		(u"Файл шаблона не найден!")
	try:
		print (u"Тестовый фаил: ",testReport)
		f2 = open(testReport, 'r')
		reader = csv.reader(f2)
		for row in reader:
			list2.append(row)
		f2.close()
	except:
		# Фактически сюда мы не попадаем, csv.reader не отличает пустой файл от отсутствующего - это надо исправлять
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
		killAllNavstat()
		exit(1)

