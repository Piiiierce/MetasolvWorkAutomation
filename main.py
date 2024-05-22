import pyautogui
import time

for i in range(8):

    time.sleep(3)

    pyautogui.moveTo(400,195) #moves to first 1x4

    time.sleep(.25)
    
    pyautogui.rightClick()   #right clicks first 1x4

    pyautogui.moveTo(500,600)    #moves to cross connect option

    time.sleep(.25)

    pyautogui.leftClick()       #left clicks cross connect

    pyautogui.moveTo(1385,800)   #moves to no option

    time.sleep(.25)

    pyautogui.leftClick()       #left clicks no

    pyautogui.moveTo(1660,195)   #moves to pon port

    time.sleep(.25)

    pyautogui.rightClick()       #right clicks pon port

    pyautogui.moveTo(1760,210)   #moves to 2nd cross connect option

    time.sleep(.25)

    pyautogui.leftClick()       #clicks 2nd cross connect option

    pyautogui.moveTo(850,450)   #moves to feed 1 in 1x4

    time.sleep(.45)

    pyautogui.leftClick()      #left clicks feed 1 in 1x4

    pyautogui.keyDown('shift')

    pyautogui.moveTo(850,495)   #moves to bottom feed 1 in 1x4 to select all ports

    time.sleep(.25)

    pyautogui.leftClick()     #selects all port in feed 1

    pyautogui.keyUp('Shift')

    pyautogui.moveTo(1450,450)    #goes to first port in card port

    time.sleep(.25)

    pyautogui.leftClick()       #selects first port in card port

    pyautogui.moveTo(1810,1100)  #moves to close button

    time.sleep(.35)

    pyautogui.leftClick()      #selects close button

    time.sleep(.2)


    pyautogui.moveTo(1360,1300)    #moves to scroll down button

    pyautogui.leftClick()       #selects scroll down



print(pyautogui.__version__)
