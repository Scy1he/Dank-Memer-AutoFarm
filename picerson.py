from pynput import keyboard
import pyautogui
import random
from discord import utils
import time
import os

def func_1():
    buttonFreshlocation= pyautogui.locateOnScreen('fresh.PNG', confidence=0.9)
    print(buttonFreshlocation)
    pyautogui.click(buttonFreshlocation)

def func_2():
    button_intel_location= pyautogui.locateOnScreen('intel.PNG', confidence=0.9)
    print(button_intel_location)
    pyautogui.click(button_intel_location)

def func_3():
    buttonKindLocation=pyautogui.locateOnScreen('kind.PNG', confidence=0.9)
    print(buttonKindLocation)
    pyautogui.click(buttonKindLocation)

def func_4():
    buttonRepoLocation=pyautogui.locateOnScreen('repost.PNG', confidence=0.9)
    print(buttonRepoLocation)
    pyautogui.click(buttonRepoLocation)

def func_5():
    buttonCPLocation=pyautogui.locateOnScreen('cppasta.PNG', confidence=0.9)
    print(buttonCPLocation)
    pyautogui.click(buttonCPLocation)


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

my_list = [func_1, func_2, func_3, func_4, func_5]

def func_67():
    random.choice(my_list)()
