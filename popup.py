import pyautogui
import time
import tkinter as tk
from tkinter import simpledialog

#create the main application window
root = tk.Tk()
root.withdraw() #hide the main window

user_input = simpledialog.askinteger("Input", "Is this splitter 1 or 2?", parent=root)

if user_input is not None:

    if user_input == 1:
        time.sleep(3)
        for i in range(8):

            pyautogui.moveTo(400, 195)  # moves to first 1x4

            time.sleep(.8)

            pyautogui.rightClick()  # right clicks first 1x4

            time.sleep(.8)

            pyautogui.moveTo(500, 600)  # moves to cross connect option

            time.sleep(.85)

            pyautogui.leftClick()  # left clicks cross connect

            pyautogui.moveTo(1385, 800)  # moves to no option

            time.sleep(1)

            pyautogui.leftClick()  # left clicks no

            pyautogui.moveTo(1660, 195)  # moves to pon port

            time.sleep(1)

            pyautogui.rightClick()  # right clicks pon port

            pyautogui.moveTo(1760, 210)  # moves to 2nd cross connect option (right side)

            time.sleep(1)

            pyautogui.leftClick()  # clicks 2nd cross connect option (right side)

            pyautogui.moveTo(850, 450)  # moves to feed 1 in 1x4

            time.sleep(1)

            pyautogui.leftClick()  # left clicks feed 1 in 1x4

            pyautogui.keyDown('shift')

            pyautogui.moveTo(850, 495)  # moves to bottom feed 1 in 1x4 to select all ports

            #time.sleep(.25)

            pyautogui.leftClick()  # selects all port in feed 1

            pyautogui.keyUp('Shift')

            pyautogui.moveTo(1450, 450)  # goes to first port in card port

            #time.sleep(.25)

            pyautogui.leftClick()  # selects first port in card port

            pyautogui.moveTo(1810, 1100)  # moves to close button

            time.sleep(1)

            pyautogui.leftClick()  # selects close button

            time.sleep(1)

            pyautogui.moveTo(1360, 1300)  # moves to scroll down button

            pyautogui.leftClick()  # selects scroll down

    elif user_input == 2:
        time.sleep(3)
        for i in range(8):

            pyautogui.moveTo(400, 195)  # moves to 1st 1x4

            time.sleep(.8)

            pyautogui.rightClick()  # right clicks first 1x4

            time.sleep(.8)

            pyautogui.moveTo(500, 600)  # moves to cross connect option

            time.sleep(.85)

            pyautogui.leftClick()  # left clicks cross connect

            pyautogui.moveTo(1385, 800)  # moves to no option

            time.sleep(1)

            pyautogui.leftClick()  # left clicks no

            pyautogui.moveTo(1660, 195)  # moves to pon port

            time.sleep(1)

            pyautogui.rightClick()  # right clicks pon port

            pyautogui.moveTo(1760, 210)  # moves to 2nd cross connect option

            time.sleep(1)

            pyautogui.leftClick()  # clicks 2nd cross connect option

            pyautogui.moveTo(850, 525)  # moves to feed 2 in 1x4

            time.sleep(1)

            pyautogui.leftClick()  # left clicks feed 2 in 1x4

            pyautogui.keyDown('shift')

            pyautogui.moveTo(850, 570)  # moves to bottom feed 2 in 1x4 to select all ports

            time.sleep(1)

            pyautogui.leftClick()  # selects all port in feed 2

            pyautogui.keyUp('Shift')

            pyautogui.moveTo(1450, 450)  # goes to first port in card port

            time.sleep(1)

            pyautogui.leftClick()  # selects first port in card port

            pyautogui.moveTo(1810, 1100)  # moves to close button

            time.sleep(1)

            pyautogui.leftClick()  # selects close button

            time.sleep(1)

            pyautogui.moveTo(1360, 1300)  # moves to scroll down button

            pyautogui.leftClick()  # selects scroll down
else:
    print("You canceled the input!")

time.sleep(3)

root.destroy()