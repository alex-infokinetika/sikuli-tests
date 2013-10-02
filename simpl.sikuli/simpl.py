from sikuli import *
# -*- coding: utf-8 -*-
import shutil
import os


myPath = os.environ.get("GIT_HOME") + u"sikuli-tests"
if not myPath in sys.path:
	sys.path.append(myPath)
# Импорт ------------------------------
import baseFunction as BF

def coordinates():
	BF.closeCurTab()
	BF.newMapTab() # перешли в свежий таб. В текущей версии при этом программа смещается в какуюто опред точку, не зависимо от того куда был сфокусирован текущий таб.
	fileName = "position_cur.png"
	try:
		print ("1")
		some_region = Region(find(Pattern("position-2.png").similar(0.60))) # нашли регион в котором нахобятся координаты
		print ("2")
		screenshotsDir = os.path.join(os.environ.get("GIT_HOME"),"sikuli-tests","img")
		print screenshotsDir
		img = capture(some_region)
		print ("4")
		shutil.move(img, os.path.join(screenshotsDir, fileName))
		print ("Сохранил патерн с текущими координатами")
	except:
		print ("Не сохранился патерн с текущими координатами")
		exit(2)

coordinates()







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