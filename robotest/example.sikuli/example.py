from __future__ import with_statement
# -*- coding: utf-8 -*-
import os
import sys
import csv
import logging, logging.handlers

myPath = os.path.join(os.environ.get("GIT_HOME"), u"sikuli-tests",u"robotest",u"example.sikuli")
if not myPath in sys.path:
	sys.path.append(myPath)
from sikuliwrapper import *





#add custom image library
addImagePath(common.cfgImageLibrary)

class NavstatReport(BaseLogger):
	
	ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
	
	def __init__(self):
		self.appCoordinates = (0, 0, 1024, 768)

	def startApp(self):
		batPath = os.path.join(os.environ.get("GIT_HOME"), u"sikuli-tests", u"clear.bat")
		os.system(batPath)
		navstat = os.path.join(os.environ.get("GIT_HOME"),u"sikuli-tests",u"navstat.appref-ms")
		os.system(navstat)
		try:
			wait("1376485054733.png",100)
			self.log.passed(u"Обновлений нет")
		except:
			self.log.passed(u"Похоже есть обновления")

	def readCsv(self):
		fName = 'test.csv'
		list = []
		shablon = os.path.join(os.environ.get("GIT_HOME"),"sikuli-tests","shablony",fName)
		#self.log.passed("Файл шаблона : ",shablon)
		f1 = open(shablon, 'r')
		reader = csv.reader(f1, delimiter='\t')
		for row in reader:
			list.append(row)
		f1.close()
		self.writeLog(list)

	def writeLog(self, list):
		str1 = u"Текст файла:"
		self.log.passed(str1)
		for row in list:
			str = '\t'.join(row)
#			print str.decode("windows-1251", "ignore") #.decode('windows-1251').encode('utf-8')
			self.log.info(str.decode("windows-1251", "ignore")) #.decode('windows-1251').encode('utf-8')

	def sendEmail(self):
		try:
			h2 = logging.handlers.SMTPHandler(mailhost='smtp.timeweb.ru',fromaddr='alex@khfam.ru',toaddrs=['alex@infokinetika.ru'],subject='The log',credentials=('user','pass'))
			#	,secure=None)
			
			h2.setLevel(logging.DEBUG)
			self.log.addHandler(h2)			
			self.log.debug("asdsdklfjsak;ld")
		except:
			self.log.info('no mail') #.decode('windows-1251').encode('utf-8')
			print sys.exc_info()


	def runTest(self):
		self.startApp()
#		self.readCsv()
#		self.writeLog(self)
#		self.sendEmail()
#self.verifyApp()
		
		#actions = '2+2'
		#self.performAction(*actions)
		#self.verifyResult(*actions)

#calc = NavstatReport()
#calc.runTest()
