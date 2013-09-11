# -*- coding: utf-8 -*-
import os
import unittest
import HTMLTestRunner

myPath = os.environ.get("GIT_HOME") + u"sikuli-tests"
if not myPath in sys.path:
    sys.path.append(myPath)
# Импорт тестов ------------------------------
import authorizationInNavstat


# --------------------------------------------
class BDTests(unittest.TestCase):
    
    def test_1(self):
        print(u"Тесты формы авторизации")
#        authorizationInNavstat.tabGo()
#        if authorizationInNavstat.abonentList():
#            print( u"Продолжаем")
    def test_2(self):
        print("test_2")
    def test_3(self):
        print("test_3")
    def test_4(self):        
        print("test_4")


suite = unittest.TestLoader().loadTestsFromTestCase(BDTests)
outPath =  os.environ.get("GIT_HOME").split("\"")[1] + "report.html" # Вариант с путём без кирилицы и именами без пробелов
try:
    outfile = open(outPath, "w")
    print "open file ", outPath
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Test Report', description='This is demo' )
    runner.run(suite)
    outfile.close()
except:
    print "Don't open file ", outPath.encode("UTF-8")



