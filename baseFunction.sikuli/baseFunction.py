from sikuli import *
# -*- coding: utf-8 -*-
import os
import sys
import shutil
import time
import datetime

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
		

def startNavstat(userName = u"admin", password = u"admin"):
	try:
		click("1376484163733.png")
		print (u"Кликнули ярлык Навтат")
	except:
		print (u"Не нашёл ярлык Навтат!")
		exit()
	try:
		wait("1376485054733.png",10)
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
				click("1376484163733.png")
				print (u"Кликнули ярлык Навтат")
			except:
				print (u"Не нашёл ярлык Навтат!")
				exit()
			try:
				wait("1376485054733.png",10)
				print (u"Обновлений больше нет")
			except:
				print (u"Навстат не запустился после обновления")
				exit()
		except:
			print (u"Обновиться не удалось")
			exit()
		exit()
	try:
		type(Pattern("VnO1Tb3OBBT1.png").targetOffset(42,2), userName.encode("UTF-8"))
		type(Key.TAB)
		type(password.encode("UTF-8"))
		click("OK.png")
		print (u"Ввели логин и пароль, нажали OK")
	except:
		print (u"Вволдили логин и пароль, нажали OK - сто-то пошло не так!")
		exit()
		try:
			wait(Pattern("NAVSTAT-1.png").similar(0.80), 300)
			print (u"Навстат запустился")
		except:
			print (u"Навстат не запустился")
			exit()
		exit()


def firstStartNavstat(userName = u"admin", password = u"admin"):
	try:
		startNavstat(userName, password)
	except:
		exit()
	wait(Pattern("Vlcropvmvrsm.png").targetOffset(64,-1),30)
	try:
		click(Pattern("Vlcropvmvrsm.png").targetOffset(64,-1))
		print (u"Первичный запуск Навстат")
	except:
		print (u"Это не первичный запуск Навстат")
		exit()

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
