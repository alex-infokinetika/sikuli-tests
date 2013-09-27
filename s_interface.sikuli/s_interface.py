from sikuli import *
# -*- coding: utf-8 -*-
import os
import time
import datetime


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
	start = time.time()
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
	click(Pattern("tab_list.png").targetOffset(-34,34))
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
		BF.waitVanishAll(["1379425632955.png","1379425704457.png","tab_hist_1.png","KamaX.png","OwTX.png","Vlcropmnameo.png","Kapra.png","OwT.png","tab_hist_2.png"])
		print (u"Все табы закрыли")
	except:
		print (u"Не все табы закрыли!")
		type(Key.F4, KeyModifier.ALT)
		exit(8)
#	print (u"")
	print (u"Время выполнения теста: "), datetime.timedelta(seconds=time.time()-start)
	type(Key.F4, KeyModifier.ALT)
#--------------------------------------------------------------------------------------------------------------------
#	2.	Тест
#	2.1.	Панель объектов: объекты, зоны, места (сворачивание разворачивание, наличие на нём объектов)
#--------------------------------------------------------------------------------------------------------------------
#	3.	Тест
#	3.1.	Панели инструментов (сворачивание, разворачивание, переключение между панелями, наличие элементов интерфейса) на табах карта и отчёт
def test3():
	start = time.time()
	BF.clearData()
	keyer.editKeyAndService("404C2A00-B173-4844-BA59-9A6F296479E7", "http://services.navstat.infokinetika.net")
	# Ключ тестового клиента "Автотестхолдинг"
	BF.firstStartNavstat()
#-----------------------
	try:
		wait("NAVSTATQ.png",15)
		click(Pattern("NAVSTATQ.png").similar(0.80).targetOffset(-31,12))
		wait("MapuuprywHou.png",15)
		print (u"Кнопки переключения между панелями на месте")
	except:
		print (u"Нет кнопок переключения между панелями!")
		type(Key.F4, KeyModifier.ALT)
		exit(1)
	try:
		wait("panel_hist.png")
		print (u"Панель История на месте")
	except:
		print (u"Панель История не развернулась")
		type(Key.F4, KeyModifier.ALT)
		exit(2)
	try:
		BF.waitAll(["strelki1.png","strelki2.png","za_den.png","za_period.png","zakladki.png","pokazat_skryt.png",Pattern("190920131017.png").similar(0.90)],5)
		print (u"Элементы, на панели История, в порядке")
	except:
		print (u"Элементы, на панели История, не в порядке!")
		type(Key.F4, KeyModifier.ALT)
		exit(3)
	try:
		click(Pattern("MapuuprywHou.png").targetOffset(-19,1),15)
		wait("MapuWT.png")
		wait("VlcropmHoucx.png")
		print (u"Панель Маршрут на месте")
	except:
		print (u"Панель Маршрут не открылась")
		type(Key.F4, KeyModifier.ALT)
		exit(4)
	try:
		BF.waitAll(["1379567058042.png","1379567072814.png","1379567083379.png","1379567092595.png","0wT.png","IOwncmm.png",Pattern("IOwncmm0wT.png").similar(0.90)])
		print (u"Элементы, на панели Маршрут, в порядке")
	except:
		print (u"Элементы, на панели Маршрут, не в порядке!")
		type(Key.F4, KeyModifier.ALT)
		exit(5)
	try:
		click(Pattern("VlcropmHoucx.png").targetOffset(28,1),15)
		BF.waitAll(["Honcx.png","1379570862855.png"])
		print (u"Панель Поиск на месте")
	except:
		print (u"Панель Поиск не открылась")
		type(Key.F4, KeyModifier.ALT)
		exit(6)
	try:
		BF.waitAll(["CrpanaPacman.png","P.png","Ymua.png","Hou.png","EOrpanmwmtmm.png","1Cnv.png","1379571017771.png","Hoxaaam.png","Cxpum.png",Pattern("HoncxCrpanaP.png").similar(0.90)])
		print (u"Элементы, на панели Поиск, в порядке")
	except:
		print (u"Элементы, на панели Поиск, не в порядке!")
		type(Key.F4, KeyModifier.ALT)
		exit(7)
	try:
		click(Pattern("1379570862855.png").targetOffset(76,0),15)
		BF.waitAll(["IlaaTap.png",Pattern("VlcrapmMapuu.png").similar(0.80)])
		print (u"Панель Локатор на месте")
	except:
		print (u"Панель Локатор не открылась")
		type(Key.F4, KeyModifier.ALT)
		exit(8)
	try:
		BF.waitAll(["TmTONKMmncpe.png","Pawycnocxa20.png","Flopuwlrauno.png","Cpm.png",Pattern("TmTONKMmncpe-1.png").similar(0.90)])
		print (u"Элементы, на панели Локатор, в порядке")
	except:
		print (u"Элементы, на панели Локатор, не в порядке!")
		type(Key.F4, KeyModifier.ALT)
		exit(9)
	BF.closeCurTab()
	print (u"Закрыли таб Карта") 
	try:
		BF.waitAll(["OwTX.png","Owm.png"])
		print (u"Переключились на таб Отчёт")
	except:
		print (u"Не переключились на таб Отчёт!")
		type(Key.F4, KeyModifier.ALT)
		exit(10)
	click(Pattern("lfEHF.png").similar(0.80).targetOffset(27,0)) # Временная заглушка, убрать её после починки http://idea.navstat.ru/tickets/6917
	try:
		BF.waitAll(["strelki1.png","strelki2.png","za_den.png","za_period.png","1aasuanamec.png","EYraecmrnTcc.png","Hoxaaam-1.png","O6uueowmMTOT.png",Pattern("Owm190920131.png").similar(0.90)])
		print (u"Элементы, на панели Отчёт, в порядке")
	except:
		print (u"Элементы, на панели Отчёт, не в порядке!")
		type(Key.F4, KeyModifier.ALT)
		exit(11)

#	print (u"")
	print (u"Время выполнения теста: "), datetime.timedelta(seconds=time.time()-start)
	type(Key.F4, KeyModifier.ALT)
#--------------------------------------------------------------------------------------------------------------------
#	4.	Тест
#	4.1.	Журнал - сворачивание разворачивание, заголовки, фильтрики (наличие данных в журнале и работа фильтров не проверяется)
#	4.2.	миникарта
#	4.3.	панелька масштаба
#	4.4.	координаты
#	4.5.	строка статуса (надо придумать как проверить актуальность времени
def test4():
	start = time.time()
	BF.clearData()
	keyer.editKeyAndService("404C2A00-B173-4844-BA59-9A6F296479E7", "http://services.navstat.infokinetika.net")
	# Ключ тестового клиента "Автотестхолдинг"
	BF.firstStartNavstat()
#-----------------------
	try:
		BF.waitAll(["HaraMunewm.png","Aonem.png","O61cTMoumopm.png","Onncarme.png"])
		print (u"Элементы, журнала событий, в порядке")
	except:
		print (u"Элементы, журнала событий, не в порядке!")
		type(Key.F4, KeyModifier.ALT)
		exit(1)
	try:
		if len( list( findAll("filtr_icon.png") ) ) == 4:
			print (u"Иконки фильтров, журнала событий, в порядке")
		else:
			print (u"Иконки фильтров, журнала событий, не в порядке!")
			type(Key.F4, KeyModifier.ALT)
			exit(2)	
	except:
		print (u"Иконки фильтров, журнала событий, не в порядке!")
		type(Key.F4, KeyModifier.ALT)
		exit(3)
	try:
		click("jornal_close_icon.png")
		BF.waitAll(["jornal_open_icon_blue.png",Pattern("jornal_close_1.png").similar(0.80),Pattern("jornal_close_2.png").similar(0.90),Pattern("jornal_close_3.png").similar(0.90)])
		print (u"Журнал свернулся")
	except:
		print (u"Журнал не свернулся!")
		type(Key.F4, KeyModifier.ALT)
		exit(4)
	try:
		click("jornal_open_icon_blue.png")
		BF.waitAll(["HaraMunewm.png","Aonem.png","O61cTMoumopm.png","Onncarme.png"])
		if len( list( findAll("filtr_icon.png") ) ) != 4:
			print (u"Журнал не развернулся!")
			type(Key.F4, KeyModifier.ALT)
			exit(5)
		print (u"Журнал развернулся")
	except:
		print (u"Журнал не развернулся!")
		type(Key.F4, KeyModifier.ALT)
		exit(6)
# 4.2 Миникарта
	try:
		doubleClick("speeddy.png")
		click("mini_map_open_1.png") # comment
		BF.waitAll(["car_in_sea.png",Pattern("mini_map.png").similar(0.90),Pattern("blue_rect.png").similar(0.80),"mini_map_close_2.png"])
		print (u"Миникарта развернулась")
	except:
		print (u"Миникарта не развернулась!")
		type(Key.F4, KeyModifier.ALT)
		exit(7)
	try:
		click("mini_map_close_2.png")
		BF.waitVanishAll([Pattern("mini_map-1.png").similar(0.90),Pattern("blue_rect-1.png").similar(0.80),Pattern("mini_map_close_2-1.png").similar(0.80)])
		BF.waitAll(["mini_map_open_2.png","no_mini_map.png"])
		print (u"Миникарта cвернулась")
	except:
		print (u"Миникарта не cвернулась!")
		type(Key.F4, KeyModifier.ALT)
		exit(8)
#	4.3.	панелька масштаба

#	4.4.	координаты

#	4.5.	строка статуса (надо придумать как проверить актуальность времени


#	print (u"")
	print (u"Время выполнения теста: "), datetime.timedelta(seconds=time.time()-start)
#	type(Key.F4, KeyModifier.ALT)
#--------------------------------------------------------------------------------------------------------------------
#	5.	Тест
#	5.1.	переключение режимов
#--------------------------------------------------------------------------------------------------------------------
#	6.	Тест
#	6.1.	переключение между картами (придумать как убедиться в том, что переключился)
#	6.2.	вынос карты в отдельное окно