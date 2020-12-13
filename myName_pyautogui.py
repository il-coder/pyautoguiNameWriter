import pyautogui as pg

distance = 0

def drawA():
    pg.moveRel(25,0)
    pg.mouseDown()
    pg.moveRel(-25,100)
    pg.moveRel(12.5,-50)
    pg.moveRel(25,0)
    pg.moveRel(-12.5,-50)
    pg.moveRel(25,100)
    pg.mouseUp()
    pg.moveRel(25,-100)
    global distance
    distance += 75
    
def drawB():
    pg.mouseDown()
    pg.moveRel(35,0)
    pg.moveRel(5,5)
    pg.moveRel(5,8)
    pg.moveRel(5,12)
    pg.moveRel(-5,12)
    pg.moveRel(-5,8)
    pg.moveRel(-5,5)
    pg.moveRel(-35,0)
    pg.moveRel(35,0)
    pg.moveRel(5,5)
    pg.moveRel(5,8)
    pg.moveRel(5,12)
    pg.moveRel(-5,12)
    pg.moveRel(-5,8)
    pg.moveRel(-5,5)
    pg.moveRel(-35,0)
    pg.moveRel(0,-100)
    pg.mouseUp()
    pg.moveRel(75,0)
    global distance
    distance += 75

def drawC():
    pg.moveRel(50,0)
    pg.mouseDown()
    pg.moveRel(-40,0)
    pg.moveRel(-10,10)
    pg.moveRel(0,80)
    pg.moveRel(10,10)
    pg.moveRel(40,0)
    pg.mouseUp()
    pg.moveRel(25,-100)
    global distance
    distance += 75

def drawD():
    pg.mouseDown()
    pg.moveRel(35,0)
    pg.moveRel(5,5)
    pg.moveRel(5,8)
    pg.moveRel(5,12)
    pg.moveRel(0,50)
    pg.moveRel(-5,12)
    pg.moveRel(-5,8)
    pg.moveRel(-5,5)
    pg.moveRel(-35,0)
    pg.moveRel(0,-100)
    pg.mouseUp()
    pg.moveRel(75,0)
    global distance
    distance += 75

def drawE():
    pg.moveRel(50,0)
    pg.mouseDown()
    pg.moveRel(-50,0)
    pg.moveRel(0,50)
    pg.moveRel(35,0)
    pg.moveRel(-35,0)
    pg.moveRel(0,50)
    pg.moveRel(50,0)
    pg.mouseUp()
    pg.moveRel(25,-100)
    global distance
    distance += 75

def drawF():
    pg.moveRel(50,0)
    pg.mouseDown()
    pg.moveRel(-50,0)
    pg.moveRel(0,50)
    pg.moveRel(35,0)
    pg.moveRel(-35,0)
    pg.moveRel(0,50)
    pg.mouseUp()
    pg.moveRel(75,-100)
    global distance
    distance += 75

def drawG():
    pg.moveRel(50,0)
    pg.mouseDown()
    pg.moveRel(-40,0)
    pg.moveRel(-10,10)
    pg.moveRel(0,80)
    pg.moveRel(10,10)
    pg.moveRel(30,0)
    pg.moveRel(10,-10)
    pg.moveRel(0,-40)
    pg.moveRel(-20,0)
    pg.mouseUp()
    pg.moveRel(45,-50)
    global distance
    distance += 75

def drawH():
    pg.mouseDown()
    pg.moveRel(0,100)
    pg.moveRel(0,-50)
    pg.moveRel(50,0)
    pg.moveRel(0,50)
    pg.moveRel(0,-100)
    pg.mouseUp()
    pg.moveRel(25,0)
    global distance
    distance += 75

def drawI():
    pg.mouseDown()
    pg.moveRel(50,0)
    pg.moveRel(-25,0)
    pg.moveRel(0,100)
    pg.moveRel(-25,0)
    pg.moveRel(50,0)
    pg.moveRel(-25,0)
    pg.mouseUp()
    pg.moveRel(50,-100)
    global distance
    distance += 75

def drawJ():
    pg.moveRel(50,0)
    pg.mouseDown()
    pg.moveRel(0,80)
    pg.moveRel(-2,5)
    pg.moveRel(-4,5)
    pg.moveRel(-8,5)
    pg.moveRel(-16,5)
    pg.moveRel(-7.5,-2)
    pg.moveRel(-7.5,-4)
    pg.moveRel(-7.5,-8)
    pg.moveRel(-7.5,-16)
    pg.mouseUp()
    pg.moveRel(75,-70)
    global distance
    distance += 75

def drawK():
    pg.mouseDown()
    pg.moveRel(0,100)
    pg.moveRel(0,-50)
    pg.moveRel(50,-50)
    pg.moveRel(-50,50)
    pg.moveRel(50,50)
    pg.mouseUp()
    pg.moveRel(25,-100)
    global distance
    distance += 75

def drawL():
    pg.mouseDown()
    pg.moveRel(0,100)
    pg.moveRel(50,0)
    pg.mouseUp()
    pg.moveRel(25,-100)
    global distance
    distance += 75

def drawM():
    pg.moveRel(0,100)
    pg.mouseDown()
    pg.moveRel(0,-100)
    pg.moveRel(25,50)
    pg.moveRel(25,-50)
    pg.moveRel(0,100)
    pg.mouseUp()
    pg.moveRel(25,-100)
    global distance
    distance += 75

def drawN():
    pg.moveRel(0,100)
    pg.mouseDown()
    pg.moveRel(0,-100)
    pg.moveRel(50,100)
    pg.moveRel(0,-100)
    pg.mouseUp()
    pg.moveRel(25,0)
    global distance
    distance += 75

def drawO():
    pg.moveRel(15,0)
    pg.mouseDown()
    pg.moveRel(20,0)
    pg.moveRel(5,5)
    pg.moveRel(5,8)
    pg.moveRel(5,12)
    pg.moveRel(0,50)
    pg.moveRel(-5,12)
    pg.moveRel(-5,8)
    pg.moveRel(-5,5)
    pg.moveRel(-20,0)
    pg.moveRel(-5,-5)
    pg.moveRel(-5,-8)
    pg.moveRel(-5,-12)
    pg.moveRel(0,-50)
    pg.moveRel(5,-12)
    pg.moveRel(5,-8)
    pg.moveRel(5,-5)    
    pg.mouseUp()
    pg.moveRel(75,0)
    global distance
    distance += 75

def drawP():
    pg.mouseDown()
    pg.moveRel(35,0)
    pg.moveRel(5,5)
    pg.moveRel(5,8)
    pg.moveRel(5,12)
    pg.moveRel(-5,12)
    pg.moveRel(-5,8)
    pg.moveRel(-5,5)
    pg.moveRel(-35,0)
    pg.moveRel(0,-50)
    pg.moveRel(0,100)
    pg.mouseUp()
    pg.moveRel(75,-100)
    global distance
    distance += 75

def drawQ():
    pg.moveRel(15,0)
    pg.mouseDown()
    pg.moveRel(20,0)
    pg.moveRel(5,5)
    pg.moveRel(5,8)
    pg.moveRel(5,12)
    pg.moveRel(0,50)
    pg.moveRel(-5,12)
    pg.moveRel(-10,-15)
    pg.moveRel(20,30)
    pg.moveRel(-10,-15)
    pg.moveRel(-5,8)
    pg.moveRel(-5,5)
    pg.moveRel(-20,0)
    pg.moveRel(-5,-5)
    pg.moveRel(-5,-8)
    pg.moveRel(-5,-12)
    pg.moveRel(0,-50)
    pg.moveRel(5,-12)
    pg.moveRel(5,-8)
    pg.moveRel(5,-5)    
    pg.mouseUp()
    pg.moveRel(75,0)
    global distance
    distance += 75

def drawR():
    pg.moveRel(0,100)
    pg.mouseDown()
    pg.moveRel(0,-100)
    pg.moveRel(35,0)
    pg.moveRel(5,5)
    pg.moveRel(5,8)
    pg.moveRel(5,12)
    pg.moveRel(-5,12)
    pg.moveRel(-5,8)
    pg.moveRel(-5,5)
    pg.moveRel(-35,0)
    pg.moveRel(15,5)
    pg.moveRel(35,50)
    pg.mouseUp()
    pg.moveRel(25,-100)
    global distance
    distance += 75
    
def drawS():
    pg.moveRel(50,0)
    pg.mouseDown()
    pg.moveRel(-40,0)
    pg.moveRel(-4,10)
    pg.moveRel(-6,15)
    pg.moveRel(6,15)
    pg.moveRel(4,10)
    pg.moveRel(30,0)
    pg.moveRel(4,10)
    pg.moveRel(6,15)
    pg.moveRel(-6,15)
    pg.moveRel(-4,10)
    pg.moveRel(-40,0)
    pg.mouseUp()
    pg.moveRel(75,-100)
    global distance
    distance += 75

def drawT():
    pg.mouseDown()
    pg.moveRel(50,0)
    pg.moveRel(-25,0)
    pg.moveRel(0,100)
    pg.mouseUp()
    pg.moveRel(50,-100)
    global distance
    distance += 75

def drawU():
    pg.mouseDown()
    pg.moveRel(0,90)
    pg.moveRel(2,4)
    pg.moveRel(3,6)
    pg.moveRel(40,0)
    pg.moveRel(3,-6)
    pg.moveRel(2,-4)
    pg.moveRel(0,-90)
    pg.mouseUp()
    pg.moveRel(25,0)
    global distance
    distance += 75

def drawV():
    pg.mouseDown()
    pg.moveRel(25,100)
    pg.moveRel(25,-100)
    pg.mouseUp()
    pg.moveRel(25,0)
    global distance
    distance += 75

def drawW():
    pg.mouseDown()
    pg.moveRel(7,100)
    pg.moveRel(18,-50)
    pg.moveRel(18,50)
    pg.moveRel(7,-100)
    pg.mouseUp()
    pg.moveRel(25,0)
    global distance
    distance += 75

def drawX():
    pg.mouseDown()
    pg.moveRel(50,100)
    pg.moveRel(-25,-50)
    pg.moveRel(-25,50)
    pg.moveRel(50,-100)
    pg.mouseUp()
    pg.moveRel(25,0)
    global distance
    distance += 75

def drawY():
    pg.mouseDown()
    pg.moveRel(25,50)
    pg.moveRel(25,-50)
    pg.moveRel(-25,50)
    pg.moveRel(0,50)
    pg.mouseUp()
    pg.moveRel(50,-100)
    global distance
    distance += 75

def drawZ():
    pg.mouseDown()
    pg.moveRel(50,0)
    pg.moveRel(-50,100)
    pg.moveRel(50,0)
    pg.mouseUp()
    pg.moveRel(25,-100)
    global distance
    distance += 75

def drawSpace():
    pg.moveRel(75,0)
    global distance
    distance += 75

def drawNextLine():
    global distance
    pg.moveRel(-distance,175)
    distance = 0

def drawExactNextLine():
    global distance
    pg.moveRel(0,175)

myFns = {
    'a' : drawA, 'b':drawB, 'c':drawC, 'd':drawD, 'e':drawE, 'f':drawF, 'g':drawG,  'h':drawH, 'i':drawI, 'j':drawJ, 'k':drawK, 'l':drawL, 'm':drawM, 'n':drawN, 'o':drawO, 'p':drawP,
    'q':drawQ, 'r':drawR, 's':drawS, 't':drawT,'u':drawU,'v':drawV, 'w':drawW, 'x':drawX, 'y':drawY, 'z':drawZ, ' ':drawSpace, 'N':drawNextLine, 'E':drawExactNextLine
    }



x,y = pg.size()

st = input("Enter string in lowercase : ")

#start paint
pg.press('win')
pg.write("paint")
pg.press('enter')
pg.sleep(0.5)
pg.hotkey('win','up')
pg.sleep(0.5)

#change paint area
pg.hotkey('ctrl','w')
pg.press('right')
pg.press('tab')
pg.write('1980')
pg.press('enter')

#change background color and fill
pg.press('alt')
pg.write('hec')
pg.press('tab',presses=7)
pg.write('0')
pg.press('tab')
pg.write('0')
pg.press('tab')
pg.write('0')
pg.press('enter')
pg.press('alt')
pg.write('hk')
pg.moveTo(x/2,y/2)
pg.click()

#choose pencil and color
pg.press('alt')
pg.write('hec')
pg.press('tab',presses=7)
pg.write('255')
pg.press('tab')
pg.write('255')
pg.press('tab')
pg.write('0')
pg.press('enter')
pg.press('alt')
pg.write('hp1')

#change pencil size
pg.keyDown('ctrl')
pg.press('add',presses=4)
pg.keyUp('ctrl')

pg.moveTo(20,20)
pg.moveRel(50,200)

#write string
for i in st:
    myFns[i]()
