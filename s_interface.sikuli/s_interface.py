from sikuli import *
# -*- coding: utf-8 -*-
import os

myPath = os.environ.get("GIT_HOME") + u"sikuli-tests"
if not myPath in sys.path:
	sys.path.append(myPath)
# Импорт ------------------------------
import baseFunction as BF
import keyer

# Смоктест
# Проверка общего состояния, наличия элементов управления
#	1.	Тест
#	1.1.	Вкладки: история, карта, отчёт (попутно переключаемся междуними, туда и обратно)
#	1.2.	кнопка со списком табов
def test1():
	BF.clearData()
	keyer.editKeyAndService("404C2A00-B173-4844-BA59-9A6F296479E7", "http://services.navstat.infokinetika.net")
	# Ключ тестового клиента "Автотестхолдинг"
	BF.startNavstat()
#-----------------------
	try:
		wait(Pattern("tab_hist.png").similar(0.80),15)
		print (u"Таб История изменений на месте")
	except:
		print (u"Нет таба История изменений или соседнего!")
		type(Key.F4, KeyModifier.ALT)
		exit(1)
	click("1379425632955.png")
	try:
		wait("Kapra.png",5)
		print (u"Таб Карта на месте")
	except:
		print (u"Нет таба Карта или соседнего!")
		type(Key.F4, KeyModifier.ALT)
		exit(2)
	click("1379425704457.png")
	try:
		wait("OwT.png",5)
		print (u"Таб Отчёт на месте")
	except:
		print (u"Нет таба с Отчёт или соседнего!")
		type(Key.F4, KeyModifier.ALT)
		exit(3)
	click("1379426134745.png")
	try:
		wait(Pattern("tab_list.png").similar(0.90),5)
		print (u"Список табов на месте")
	except:
		print (u"Нет списка табов!")
		type(Key.F4, KeyModifier.ALT)
		exit(4)
	click(Pattern("tab_list.png").similar(0.90).targetOffset(-38,13))
	try:
		wait("KamaX.png")
		print (u"Перешли на таб Карта через список табов")
	except:
		print (u"Не перешли на таб Карта через список табов!")
		type(Key.F4, KeyModifier.ALT)
		exit(5)
	click("1379426134745.png")
	click(Pattern("tab_list.png").similar(0.90).targetOffset(-36,-8))
	try:
		wait("OwTX.png",5)
		print (u"Перешли на таб Отчёт через список табов")
	except:
		print (u"Не перешли на таб Отчёт через список табов!")
		type(Key.F4, KeyModifier.ALT)
		exit(6)
	click("1379426134745.png")
	click(Pattern("tab_list.png").similar(0.00).targetOffset(-34,34))
	try:
		wait("Vlcropmnameo.png")
		print (u"Перешли на таб История изменений через список табов")
	except:
		print (u"Не перешли на таб История изменений через список табов!")
		type(Key.F4, KeyModifier.ALT)
		exit(7)
	BF.closeCurTab()
	BF.closeCurTab()
	BF.closeCurTab()
	try:
		waitVanish("1379425632955.png")
		waitVanish("1379425704457.png")
		waitVanish("tab_hist_1.png")
		waitVanish("KamaX.png")
		waitVanish("OwTX.png")
		waitVanish("Vlcropmnameo.png")
		waitVanish("Kapra.png")
		waitVanish("OwT.png")
		waitVanish("tab_hist_2.png")
		print (u"Все табы закрыли")
	except:
		print (u"Не все табы закрыли!")
		type(Key.F4, KeyModifier.ALT)
		exit(8)
#	print (u"")
	type(Key.F4, KeyModifier.ALT)
#--------------------------------------------------------------------------------------------------------------------
#	2.	Тест
#	2.1.	Панель объектов: объекты, зоны, места (сворачивание разворачивание, наличие на нём объектов)
#--------------------------------------------------------------------------------------------------------------------
#	3.	Тест
#	3.1.	Панели инструментов (сворачивание, разворачивание, переключение между панелями, наличие элементов интерфейса) на табах карта и отчёт
def test3():
	BF.clearData()
	keyer.editKeyAndService("404C2A00-B173-4844-BA59-9A6F296479E7", "http://services.navstat.infokinetika.net")
	# Ключ тестового клиента "Автотестхолдинг"
	BF.firstStartNavstat()
#-----------------------
	try:
		wait("NAVSTATQ.png",15)
		click(Pattern("NAVSTATQ.png").similar(0.80).targetOffset(-31,12))
		wait("panel_hist.png")
		print (u"Панель История на месте")
	except:
		print (u"Панель История не развернулась")
		type(Key.F4, KeyModifier.ALT)
		exit(1)
	try:
		wait("MapuuprywHou.png",15)
		print (u"Кнопки переключения между панелями на месте")
	except:
		print (u"Нет кнопок переключения между панелями!")
		type(Key.F4, KeyModifier.ALT)
		exit(2)
	try:
#		wait(Pattern("180920131157.png").similar(0.60)) #так не пойдёт, надо опознавать каждый отдельно
		wait("strelki1.png")
		wait("strelki2.png")
		wait("za_den.png")
		wait("za_period.png")
		wait("zakladki.png")
		wait("pokazat_skryt.png")
		print (u"Элементы, на панели История, в порядке")
	except:
		print (u"Элементы, на панели История, в не порядке!")
		type(Key.F4, KeyModifier.ALT)
		exit(3)


#	print (u"")
#	type(Key.F4, KeyModifier.ALT)
#--------------------------------------------------------------------------------------------------------------------
#	4.	Тест
#	4.1.	Журнал (сворачивание разворачивание)
#	4.2.	миникарта
#	4.3.	панелька масштаба
#	4.4.	координаты
#	4.5.	строка статуса (надо придумать как проверить актуальность времени
#--------------------------------------------------------------------------------------------------------------------
#	5.	Тест
#	5.1.	переключение режимов
#--------------------------------------------------------------------------------------------------------------------
#	6.	Тест
#	6.1.	переключение между картами (придумать как убедиться в том, что переключился)
#	6.2.	вынос карты в отдельное окно