from sikuli import *
# -*- coding: utf-8 -*-
	
def editKey(newKey):
	click("1376472023054.png")
	wait(Pattern("YCTGHOBHCHGI.png").similar(0.50),30)
	type(Pattern("nO1Tb3OBBT1T-1.png").targetOffset(-63,-1), "**")
	type(Pattern("ap0m-1.png").targetOffset(-60,-3), "**")
	click(Pattern("OK-1.png").similar(0.80))
	wait("1376472195857.png",5)
	click("VCIpBBVTbKII.png")
	doubleClick(Pattern(Pattern("Llemo0cW.png").targetOffset(-47,-2)).targetOffset(-47,-1))
	type(Key.DELETE)
	paste(Pattern("PIWCTpBLLHOH.png").targetOffset(-219,5), newKey)
	click("OK-2.png")
	wait(Pattern("YCTGHOBHCHGI.png").similar(0.50),30)
	click("Onaena.png")


def editKeyAndService(newKey, newURL):
	click("1376472023054.png")
	wait(Pattern("YCTGHOBHCHGI.png").similar(0.50),30)
	type(Pattern("nO1Tb3OBBT1T-1.png").targetOffset(-63,-1), "**")
	type(Pattern("ap0m-1.png").targetOffset(-60,-3), "**")
	click(Pattern("OK-1.png").similar(0.80))
	wait("1376472195857.png",5)
	click("VCIpBBVTbKII.png")
	doubleClick(Pattern(Pattern("Llemo0cW.png").targetOffset(-47,-2)).targetOffset(-47,-1))
	type(Key.DELETE)
	paste(Pattern("PIWCTpBLLHOH.png").targetOffset(-219,5), newKey)
	click(Pattern("Pacu1vrpermu.png").targetOffset(-27,1))
	click(Pattern("IIOKB3BTbPBC.png").targetOffset(-92,-1))
	doubleClick(Pattern("Ccbmxa.png").targetOffset(157,0))
	paste(newURL)
	click("OK-2.png")
	wait(Pattern("YCTGHOBHCHGI.png").similar(0.50),30)
	click("Onaena.png")
	print "curent key: " + newKey
	print "curent url: " + newURL
	

