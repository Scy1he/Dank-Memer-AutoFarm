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

def findButton():
    color = (88, 101, 242)
    clicked = False
    s = pyautogui.screenshot()
    for x in range(s.width):
        for y in range(s.height):
            if s.getpixel((x, y)) == color:
                pyautogui.click(x, y)
                clicked = True
                break
        if clicked == True:
            break
    keyboard2 = KeyboardController()
    keyboard2.press(Key.tab)
    keyboard2.release(Key.tab)
z = random.uniform(0,1)
v = 0

time.sleep(10)
while x > 1:
    pyautogui.typewrite("pls fish", interval=z)
    v=z
    print(v)
    pyautogui.hotkey('enter')
    pyautogui.PAUSE = x
    pyautogui.typewrite("Pls dig", interval=z)
    v=z
    print(v)
    pyautogui.hotkey('enter')
    pyautogui.PAUSE = x
    pyautogui.typewrite("pls hunt",interval=z)
    v=z
    print(v)
    pyautogui.hotkey('enter')
    pyautogui.PAUSE = x
    pyautogui.typewrite("pls beg",interval=z)
    v=z
    print(v)
    pyautogui.hotkey('enter')
    pyautogui.PAUSE = x

    pyautogui.typewrite("pls pm", interval=0.23)
    pyautogui.hotkey('enter')
    fn.func_67()
    time.sleep(y)
