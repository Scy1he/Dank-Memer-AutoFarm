from pynput import keyboard
import pyautogui
import random
from discord import utils
import time
import os


import picerson as fn

x= random.uniform(1,2)
y= random.uniform(13,15)

current_time = time.strftime("%H:%M:%S", time.localtime())
print('-'*33)
print(f'The time of starting is: {current_time}')
print('-'*33 + '\n\n')

z = random.uniform(0,1)
v = 0

time.sleep(10)
while x > 1:
    pyautogui.typewrite("pls fish", interval=z)
    pyautogui.hotkey('enter')

    pyautogui.PAUSE = x

    pyautogui.typewrite("Pls dig", interval=z)
    pyautogui.hotkey('enter')

    pyautogui.PAUSE = x

    pyautogui.typewrite("pls hunt",interval=z)
    pyautogui.hotkey('enter')

    pyautogui.PAUSE = x

    pyautogui.typewrite("pls beg",interval=z)
    pyautogui.hotkey('enter')

    pyautogui.PAUSE = x

    pyautogui.typewrite("pls pm", interval=z)
    pyautogui.hotkey('enter')
    fn.func_67()

    pyautogui.PAUSE= x

    pyautogui.typewrite("pls search", interval=z)
    pyautogui.hotkey("enter")
    fn.findButton()

    time.sleep(y)
