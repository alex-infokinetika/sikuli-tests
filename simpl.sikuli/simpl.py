from sikuli import *
# -*- coding: utf-8 -*-
import shutil
import os


myPath = os.environ.get("GIT_HOME") + u"sikuli-tests"
if not myPath in sys.path:
	sys.path.append(myPath)
# Импорт ------------------------------
import baseFunction as BF



#	4.4	панелька масштаба
def zoom():
	BF.closeCurTab()
	BF.newMapTab() # перешли в свежий таб. В текущей версии при этом программа смещается в какуюто опред точку, не зависимо от того куда был сфокусирован текущий таб.
	try:
		BF.waitAll(["zoom_line_14000.png","mashtab.png"],10)
		print (u"1")
	except:
		print (u"2!")
#		type(Key.F4, KeyModifier.ALT)
		exit(3)
	try:
		for i in xrange(1,12):
			click(Pattern("zoom_minus.png").similar(0.90))
		BF.waitAll(["min_zoom.png","zoom_111000000.png","afrika.png","australia.png"],20)
		print (u"Максимально удалились")
	except:
		print (u"Не отработало максимальное удаление!")
#		type(Key.F4, KeyModifier.ALT)
		exit(4)
	try:
		for i in xrange(1,5):
			click(Pattern("zppm_plus.png").similar(0.90))
		BF.waitAll(["zoom_7000000.png","zoom_line_7000000.png","mini_car.png","sao_tome.png","libreville.png"],20)
		print (u"Масштаб 7 000 000")
	except:
		print (u"Не перешли на масштаб 7 000 000!")
#		type(Key.F4, KeyModifier.ALT)
		exit(5)





def moveMap():
	click("point_on_map.png")
	try:
		mouseDown(Button.LEFT)
		mouseMove("care.png")
		mouseUp(Button.LEFT)
	except:
		exit(1)

#moveMap()



def readF():
	fn = os.path.join(os.environ.get("GIT_HOME"), u"f1.txt")
	print (u"File name: "), fn
	try:
		f = open(fn)
		points = f.read()
		f.close()
		return points
	except:
		exit(1)

def writeF():
	f1 = open(os.path.join(os.environ.get("GIT_HOME"), u"f2.txt"), 'w')
	a = f1.write(readF())
	print a

def screenF():
	img = capture(App.focusedWindow())
	shutil.move(img, os.path.join(os.environ.get("GIT_HOME"), u"f3.png"))

#screenF()
#writeF()
#readF()











def coordinates():
	BF.closeCurTab()
	BF.newMapTab() # перешли в свежий таб. В текущей версии при этом программа смещается в какуюто опред точку, не зависимо от того куда был сфокусирован текущий таб.
	try:
		img = capture(Region(find(Pattern("position-2.png").similar(0.60))))# нашли регион в котором нахобятся координаты
		shutil.move(img, os.path.join(os.environ.get("GIT_HOME"), u"sikuli-tests", u"img", u"f3.png"))
		print (u"Сохранил патерн с текущими координатами")
	except:
		print (u"Не сохранился патерн с текущими координатами")
		exit(2)
	try:
		img = os.path.join(os.environ.get("GIT_HOME"), u"sikuli-tests", u"img", u"f3.png")
		click(img)
		waitVanish(Pattern(img).similar(0.80))
		doubleClick("speeddy-1.png")
		click("car_in_sea-1.png")
		wait(Pattern("position_0_0.png").similar(0.90))
		print (u"Координаты меняются нормально")	
	except:
		print (u"Что-то не так с изменением координат!")
#		type(Key.F4, KeyModifier.ALT)
		exit(3)

#coordinates()







"""
BF.closeCurTab()
BF.newMapTab()
pos = Region(find(Pattern("position.png").similar(0.60)))
try:
	some_region = pos #App.focusedWindow() # for the frontmost window
	screenshotsDir = os.environ.get("GIT_HOME") + u"sikuli-tests/img"
	img = capture(some_region)
	shutil.move(img, os.path.join(screenshotsDir, "position2.png"))
except:
	exit(2)
try:
	click(Pattern("../img/position2.png").similar(0.70))
	print "12"
	waitVanish(Pattern("../img/position2.png") .similar(0.70))
	print "13"
	doubleClick("speeddy.png")
	click(Pattern("car_in_sea.png").targetOffset(-1,0))
	print "14"
	wait(Pattern("position_0_0.png") .similar(0.90))
	print "15"
except:
	exit(3)
"""