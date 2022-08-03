from pynput import keyboard
import pyautogui
import random
from discord import utils
import time
import os

def func_1():
     pyautogui.moveTo(804, 884, duration=0.7)
     pyautogui.leftClick()

def func_2():
    pyautogui.moveTo(521, 884, duration=0.7)
    pyautogui.leftClick()

def func_3():
    pyautogui.moveTo(614, 883, duration=0.7)
    pyautogui.leftclick()

def func_4():
    pyautogui.moveTo(738, 885, duration=0.7)
    pyautogui.leftClick()

def func_5():
    pyautogui.moveTo(973, 887, duration=0.7)
    pyautogui.leftClick()

my_list = [func_1, func_2, func_3, func_4, func_5]

def func_67():
    random.choice(my_list)()
