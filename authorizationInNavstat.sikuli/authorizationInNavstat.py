from sikuli import *
# -*- coding: utf-8 -*-
import os
import sys
import shutil
# get the directory containing your running .sikuli
myPath = os.environ.get("GIT_HOME") + u"sikuli-tests"
if not myPath in sys.path:
    sys.path.append(myPath)
import baseFunction
# -------------- Вспомогательные функции -------------------------------
# просто кликаем иконку Навстат на пенели быстрого запуска
def runNavstat():
    Region(2,1012,1735,67).click("1376562365600.png")
    Region(478,149,897,631).wait(Pattern("1376562536766.png").similar(0.60),15)
# эту функцию надо будет переписать, чтоб она вызывала Навстат как приложение, а не зависила от иконки
def closeAuthorizationForm():
    Region(478,149,897,631).click("Onaena-1.png")

# ------------- набот тестов формы авторизации -----------------------------------------------------------------------------------------    

# проверка коректности переходов табами с ключём демо
def tabGo():
    try:
         baseFunction.clearData()
    except:
        er = u"Ошибка! не удалились конфиги" 
        print(er.encode("utf-8"))
        #exit()
    runNavstat()
    text = u"1 ----"
    type(text.encode("utf-8"))
    try:
        Region(717,299,500,376).find(Pattern("QnO1Tb3OBBT1.png").similar(0.90))
    except:
        er = u"Ошибка! Не ввелось имя пользователя" 
        print(er.encode("utf-8"))
        exit()
    type(Key.TAB)  # перешли в поле пароль
    type(text.encode("utf-8"))
    try:
        Region(717,299,500,376).find(Pattern("Qap0m.png").similar(0.90))
    except:
        er = u"Ошибка! Не ввёлся пароль" 
        print(er.encode("utf-8"))
        exit()
    type(Key.TAB) # перешли в чекбокс
    try:
        Region(770,328,377,313).find(Pattern("III.png").similar(0.90))
        type(Key.SPACE)
        Region(770,328,377,313).find(Pattern("1376565096984.png").similar(0.90))
    except:
        er = u"Ошибка! Не установилась/снялась галка 'Запомнить пароль...'" 
        print(er.encode("utf-8"))
        exit()
    type(Key.TAB) # перешли на ОК
    try:
        Region(770,328,377,313).find("1376568260292.png")
    except:
        er = u"Ошибка! Не не перешли на кнопку ОК" 
        print(er.encode("utf-8"))
        exit()
    type(Key.TAB) # перешли в Отмена
    try:
        Region(770,328,377,313).find("1376568318636.png")
    except:
        er = u"Ошибка! Не не перешли на кнопку Отмена" 
        print(er.encode("utf-8"))
        exit()
    type(Key.TAB)
    n=10
    while n > 0:
        if n == 0:
            break
        else:
            type(Key.BACKSPACE)
            n -= 1
    try:
        Region(717,299,500,376).find(Pattern("K.png").similar(0.90))
    except:
        er = u"Ошибка! Не вернулись в поле 'Пользователь'" 
        print(er.encode("utf-8"))
        exit()
    type(Key.TAB) # перешли в поле пароль
    type(Key.TAB) # перешли в чекбокс
    type(Key.TAB) # перешли на ОК
    type(Key.TAB) # перешли в Отмена
    type(Key.ENTER) # закрыли прогу

# ----------------------------------------------------------------------------------------
# Проверка работы выпадающего списка абонентов с ключём Холдинга
# для проверки используется тестовый сервер
# Автохолдинг Холдинг 404C2A00-B173-4844-BA59-9A6F296479E7
# Петров ИП   Клиент  54131713-78BC-4E1A-8EA2-A59E79A5B4A2
# Иванов ИП   Клиент  AE33FC55-4D71-45B7-A919-FD242F0EFA07
# Исаев ООО   Клиент  2AA51F34-8D4E-438E-9A39-64E6FE3E8C5A

import keyer

def abonentList():
    # меняем ключ на Автохолдинг на тестовом сервере
    k = u"404C2A00-B173-4844-BA59-9A6F296479E7" 
    u = u"http://services.navstat.infokinetika.net"
    keyer.editKeyAndService(k,u)
    runNavstat()
    click(Pattern("A50HerrrIIII.png").targetOffset(149,0))
    try:
        Region(717,299,500,376).find(Pattern("abonentList.png").targetOffset(144,-6))
    except:
        er = u"Ошибка! Неn списка абонентов" 
        print(er.encode("utf-8"))
        return 0
    click(Pattern("A50Herrr.png").targetOffset(271,1))
    closeAuthorizationForm()
    return 1

# Движение по списку абонентов мышкой
def moovWithAbonentList():
    mess = u"Выполнять только после успешного прохода abonentList" 
    print(mess.encode("utf-8"))
    runNavstat()
    click(Pattern("A50HerrrIIII.png").targetOffset(52,1))    
    mouseMove(Pattern("list0.png").targetOffset(21,-16))
    try:
        Region(717,299,500,376).find("list1.png")
        mouseMove(find(Pattern("list1.png").targetOffset(0,36)))
    except:
        er = u"Ошибка! Не идём по списку абонентов" 
        print(er.encode("utf-8"))
        return 0
    try:
        Region(717,299,500,376).find("list4.png")
    except:
        er = u"Ошибка! Не идём по списку абонентов" 
        print(er.encode("utf-8"))
        return 0
    mouseDown(Button.LEFT)
    mouseUp()
    try:
        Region(717,299,500,376).find(Pattern("OODVlcaes.png").similar(0.90).targetOffset(-76,-28))
    except:
        er = u"Ошибка! Выбрали абонента" 
        print(er.encode("utf-8"))
        return 0
    popup("End")
# дальше надо подвигаться по списку клавишами "вверх" "вниз"

# Поиск по выпадающему списку абонентов
def findAbonentInList():
    mess = u"Выполнять только после успешного прохода abonentList" 
    print(mess.encode("utf-8"))



