import pyautogui
import time
import random
pyautogui.FAILSAFE = True #Slam mouse into top left to abort
#XY coordinates have 0, 0 origin at top left corner of the screen.


for outbid in pyautogui.locateAllOnScreen('red1.png', confidence=0.9) :
    #JEveAssets
    pyautogui.moveTo(outbid, duration=0.3)
    pyautogui.moveRel(-50, 2, duration=0.1)
    pyautogui.click()
    time.sleep(random.uniform(1, 1.5))

    #Eve Client
    if pyautogui.locateCenterOnScreen('buy.png', confidence=0.9) == None :
        time.sleep(random.uniform(0.8, 1.2))

    elif pyautogui.locateCenterOnScreen('buy.png', confidence=0.9) != None :
        buylocation = pyautogui.locateCenterOnScreen('buy.png', confidence=0.9)
        x1 = buylocation[0]
        y1 = buylocation[1]
        x2 = x1 + random.randint(-2, 2)
        y2 = y1 + random.randint(-2, 2)
        buylocationrandom = x2, y2
        pyautogui.moveTo(buylocationrandom, duration=random.uniform(0.7, 1.5))
        time.sleep(random.uniform(0.05, 0.15))
        pyautogui.rightClick()
        time.sleep(random.uniform(0.05, 0.15))
        pyautogui.moveRel(random.randint(15, 30), random.randint(3, 15), duration=random.uniform(0.05, 0.15))
        time.sleep(random.uniform(0.01, 0.05))
        pyautogui.click()
        time.sleep(random.uniform(0.5, 1))
        pyautogui.keyDown('ctrl')
        pyautogui.press('v')
        pyautogui.keyUp('ctrl')
        time.sleep(random.uniform(0.1, 0.3))

        if pyautogui.locateCenterOnScreen('firstconf.png', confidence=0.9) == None :
            time.sleep(random.uniform(0.8, 1.2))

        elif pyautogui.locateCenterOnScreen('firstconf.png', confidence=0.9) != None :
            firstconfirmation = pyautogui.locateCenterOnScreen('firstconf.png', confidence=0.9)
            x3 = firstconfirmation[0]
            y3 = firstconfirmation[1]
            x4 = x3 + random.randint(-2, 2)
            y4 = y3 + random.randint(-2, 2)
            firstconfirmationrandom = x4, y4
            pyautogui.moveTo(firstconfirmationrandom, duration=random.uniform(0.1, 0.2))
            pyautogui.click()
    
            #Second Confirmation for high margin
            if pyautogui.locateCenterOnScreen('secondconf.png', confidence=0.9) == None :
                time.sleep(random.uniform(0.8, 1.2))

            elif pyautogui.locateCenterOnScreen('secondconf.png', confidence=0.9) != None :
                secondconfirmation = pyautogui.locateCenterOnScreen('secondconf.png', confidence=0.9)
                x5 = secondconfirmation[0]
                y5 = secondconfirmation[1]
                x6 = x5 + random.randint(-1, 1)
                y6 = y5 + random.randint(-1, 1)
                secondconfirmationrandom = x6, y6
                pyautogui.moveTo(secondconfirmationrandom, duration=random.uniform(0.2, 0.5))
                pyautogui.click()
                time.sleep(random.uniform(0.8, 1.2))
print('Done!')