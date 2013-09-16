# -*- coding: utf-8 -*-
import os
import unittest
import HTMLTestRunner

myPath = os.environ.get("GIT_HOME") + u"sikuli-tests"
if not myPath in sys.path:
    sys.path.append(myPath)
# Импорт тестов ------------------------------
import tmp
# --------------------------------------------
class BDTests(unittest.TestCase):
    
    def test_1(self):
        print "test 1"
        tmp.tmp()

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



