import pyautogui
import pandas as pd
import time
import pyperclip
import openpyxl
import tkinter as tk
from tkinter import simpledialog


file_path = r'C:/Users/proark/Desktop/AugmentAndReleasePierce.xlsx' #saves path to file as variable

df = pd.read_excel(file_path) #panda opens file so panda can read spreadsheet

# Initialize variables
def ask_questions():
    clli_location = simpledialog.askstring("Input", "What is the clli location?")
    row_number = simpledialog.askinteger("Input", "What row number?") - 1
    how_many = simpledialog.askinteger("Input", "How many?")

    if clli_location is not None and row_number is not None and how_many is not None:
        result_label.config(text=f"CLLI Location: {clli_location}\nRow Number: {row_number}\nHow Many: {how_many}")
        if how_many > 1:

            #cell_value = str(df.at[row_number - 1, 'SPLITTER'])

            for i in range(how_many):

                time.sleep(1.25)

                cell_value = str(df.at[row_number - 1, 'SPLITTER'])

                pyperclip.copy(clli_location)

                pyautogui.moveTo(255, 398)

                pyautogui.leftClick()

                time.sleep(3)

                pyautogui.moveTo(1055, 465) #to connection format

                pyautogui.leftClick()

                time.sleep(.35)

                pyautogui.moveTo(1055, 505) #to facility freeformat

                pyautogui.leftClick()

                time.sleep(.25)

                pyautogui.moveTo(1055, 493) #to service type

                pyautogui.leftClick()

                time.sleep(.25)

                pyautogui.moveTo(1055, 510) #to unknow (the option)

                pyautogui.leftClick()

                time.sleep(.25)

                pyautogui.moveTo(1055, 730) #to location A box

                pyautogui.leftClick()

                time.sleep(.25)

                pyautogui.hotkey('ctrl', 'v')

                pyautogui.hotkey('tab')

                time.sleep(.15)

                pyautogui.hotkey('ctrl', 'v')

                pyautogui.hotkey('tab')

                time.sleep(.15)

                pyautogui.hotkey('ctrl', 'v')

                pyperclip.copy(cell_value)

                pyautogui.hotkey('space')

                pyautogui.hotkey('ctrl', 'v')

                pyautogui.moveTo(1570, 1015) #to close crkt window

                pyautogui.leftClick()

                time.sleep(3)

                row_number = row_number + 1

                print(cell_value)

        else:
            cell_value = str(df.at[row_number - 1, 'SPLITTER'])

            pyperclip.copy(clli_location)

            pyautogui.moveTo(255, 398)

            pyautogui.leftClick()

            time.sleep(3.5)

            pyautogui.moveTo(1055, 465)  # to connection format

            pyautogui.leftClick()

            time.sleep(.35)

            pyautogui.moveTo(1055, 505)  # to facility freeformat

            pyautogui.leftClick()

            time.sleep(.25)

            pyautogui.moveTo(1055, 493)  # to service type

            pyautogui.leftClick()

            time.sleep(.25)

            pyautogui.moveTo(1055, 510)  # to unknow (the option)

            pyautogui.leftClick()

            time.sleep(.25)

            pyautogui.moveTo(1055, 730)  # to location A box

            pyautogui.leftClick()

            time.sleep(.25)

            pyautogui.hotkey('ctrl', 'v')

            pyautogui.hotkey('tab')

            time.sleep(.15)

            pyautogui.hotkey('ctrl', 'v')

            pyautogui.hotkey('tab')

            time.sleep(.15)

            pyautogui.hotkey('ctrl', 'v')

            time.sleep(.15)

            pyperclip.copy(cell_value)

            pyautogui.hotkey('space')

            pyautogui.hotkey('ctrl', 'v')

            time.sleep(.15)

            pyautogui.moveTo(1570, 1015)

            pyautogui.leftClick()

            time.sleep(3)

            print(cell_value)

    else:
        result_label.config(text="Please provide valid inputs.")

# Create the main application window
root = tk.Tk()
root.title("Questionnaire")

# Create a button to trigger the questions
ask_button = tk.Button(root, text="Ask Questions", command=ask_questions)
ask_button.pack()

# Create a label to display the answers
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()




    #cell_value = str(df.at[6285, 'SPLITTER'])
    #print(cell_value)