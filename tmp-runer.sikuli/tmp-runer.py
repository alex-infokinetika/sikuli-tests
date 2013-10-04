# -*- coding: utf-8 -*-
import os
import unittest
import HTMLTestRunner

myPath = os.environ.get("GIT_HOME") + u"sikuli-tests"
if not myPath in sys.path:
	sys.path.append(myPath)
# Импорт тестов ------------------------------
import tmp
import s_interface
import simpl
# --------------------------------------------
class BDTests(unittest.TestCase):

	def test_1(self):
		print "test 1"
		#s_interface.test1()
	def test_2(self):
		print "test 2"
		#s_interface.test2()
	def test_3(self):
		print "test 3"
		#s_interface.test3()
	def test_4(self):
		print "test 4"
		s_interface.test4()
		#s_interface.coordinates()
	def test_5(self):
		print "test 5"
		simpl.zoom()
		#simpl.coordinates()
		#s_interface.coordinates()
		
	def test_0(self):
		print "test 0"
		#tmp.timer()

suite = unittest.TestLoader().loadTestsFromTestCase(BDTests)
outPath =  os.environ.get("GIT_HOME") + "tmp-report.html" # Вариант с путём без кирилицы и именами без пробелов  
try:
	outfile = open(outPath, "w")
	print "open file ", outPath
	runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Tmp Report', description='This is demo' )
	runner.run(suite)
	outfile.close()
except:
	print "Don't open file ", outPath.encode("UTF-8")



