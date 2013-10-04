from sikuli import *
# -*- coding: utf-8 -*-
import os
import time
import datetime

myPath = os.environ.get("GIT_HOME") + u"sikuli-tests"
if not myPath in sys.path:
	sys.path.append(myPath)
# Импорт ------------------------------
import baseFunction
import keyer

def closeCurTab():
	try:
		click("1379333077365-1.png")
		return 1
	except:
		return 0

def newMapTab():
	wait("1379336670320.png")
	click("1379333330757.png")	

# Проверака боботы дерева объектов
def tmp():
	baseFunction.clearData()
	keyer.editKeyAndService("404C2A00-B173-4844-BA59-9A6F296479E7", "http://services.navstat.infokinetika.net")	 # Ключ тестового клиента "Автотестхолдинг"
	baseFunction.firstStartNavstat()
#-----------------------
#-----------------------
	try:
		find(Pattern("Var10VIHQOne.png").similar(0.80))
		print(u"Дерево объектов на месте на месте")
	except:
		print(u"Дерево объектов сломали")
		exit(1)
#-----------------------
	newMapTab()
	click(Pattern("Var10VIHQOne-1.png").similar(0.80).targetOffset(-32,12))
	try:
		find(Pattern("Var10VIHOuex.png").similar(0.80))
		click(Pattern("Var10VIHOuex-2.png").targetOffset(-61,-22))
		click(Pattern("P.png").similar(0.80).targetOffset(-9,0))
		find(Pattern("Var10VIHQOne-3.png").similar(0.80).targetOffset(-32,12))
		print(u"Группы сворачиваются и разворачиваются")
	except:
		print(u"Группы не сворачиваются или не разворачиваются!")
		exit(2)
	closeCurTab() 
#-----------------------
	newMapTab()
	click(Pattern("O6cTVar10VIH.png").similar(0.80).targetOffset(-59,-8))
	try:
		click(Pattern("O6neTVlnanon.png").similar(0.80).targetOffset(-44,0))
		click(Pattern("P.png").similar(0.80).targetOffset(-9,0))
		find(Pattern("O6neTVar10VI.png").similar(0.80))
		print(u"Абоненты сворачиваются и разворачиваются")
	except:
		print(u"Абоненты не сворачиваются или не разворачиваются!")
		exit(2)
	closeCurTab()
#--------------заготовки:
	newMapTab()
	doubleClick(Pattern("ncrpuh.png").similar(0.80).targetOffset(2,1))
	try:
		wait(Pattern("1379080119801.png").similar(0.80))
		print(u"Переместились к объекту по даблклику")
	except:
		print(u"Не переместились к объекту по даблклику")
		exit(3)
	click(Pattern("Eucmwi.png").similar(0.80).targetOffset(-72,0))
	try:
		waitVanish("1379080119801.png", 5)
		wait("1379080342892.png")
		print(u"Скрыли объект")
		wait("EcsmvVar10QO.png")
		print(u"И галочка в дереве исчезла")
	except:
		print(u"Не скрылся объект или галочка в дереве не исчезла")
		exit(4)
	click(Pattern("Eucmwi.png").similar(0.80).targetOffset(-72,0))
	try:
		wait(Pattern("1379080119801.png").similar(0.80),5)
		print(u"Вернули видимость объекта")
	except:
		print(u"Видимость объекта не восстановилась")
		exit(5)
	click(Pattern("OncxmMoumopm.png").similar(0.80).targetOffset(-55,31))
	try:
		wait(Pattern("IIO61eVluani.png").similar(0.90))
		print(u"Сняли галочки со всего дерева объектов")
	except:
		print(u"Галочки, со всего дерева объектов, не снялись")
		exit(6)
	try:
		waitVanish("1379080119801.png",30)# Уменьшить время ожидания после починки бага http://idea.navstat.ru/tickets/7971
		wait("1379080342892.png")
		print(u"Объект сурылся")
	except:
		print(u"Не скрылся объект")
		exit(7)
	click(Pattern("OncxmMoumopm.png").similar(0.80).targetOffset(-55,31))
	try:
		wait(Pattern("1379080789295.png").similar(0.90))
		print(u"Вернули галочки видимости всем объектам")
		waitVanish("1379080342892.png",30)
		wait(Pattern("1379080119801.png").similar(0.80)) # Найден баг, не сразу исчезает и появляется машинка при установке снятии галок со всех объектов, уточнить причины задержки
		print(u"Вернулась видимость объекта")
	except:
		print(u"Видимость объекта не восстановилась")
		exit(8)
#-----------------------
	type(Key.F4, KeyModifier.ALT)

def timer():
	start = time.time()
	sleep(5)
	print (u"Время выполнения теста: "), datetime.timedelta(seconds=time.time()-start)
