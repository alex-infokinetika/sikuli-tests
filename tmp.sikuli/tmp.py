from sikuli import *
# -*- coding: utf-8 -*-
import os

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
    keyer.editKeyAndService("404C2A00-B173-4844-BA59-9A6F296479E7", "http://services.navstat.infokinetika.net")     # Ключ тестового клиента "Автотестхолдинг"
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
    wait(Pattern("1379080119801.png").similar(0.80))
    click(Pattern("Eucmwi.png").similar(0.80).targetOffset(-72,0))
    waitVanish("1379080119801.png")
    wait("1379080342892.png")
    wait("EcsmvVar10QO.png")
    click(Pattern("Eucmwi.png").similar(0.80).targetOffset(-72,0))
    wait(Pattern("1379080119801.png").similar(0.80))
    click(Pattern("OncxmMoumopm.png").similar(0.80).targetOffset(-55,31))
    wait(Pattern("IIO61eVluani.png").similar(0.90))
    waitVanish("1379080119801.png")
    click(Pattern("OncxmMoumopm.png").similar(0.80).targetOffset(-55,31))
    wait(Pattern("1379080789295.png").similar(0.90))
    wait(Pattern("1379080119801.png").similar(0.80)) # Найден баг, не сразу исчезает и появляется машинка при установке снятии галок со всех объектов, уточнить причины задержки

#-----------------------
    type(Key.F4, KeyModifier.ALT)


