import pyautogui
import time
import win32api
import math
import random
import win32gui
import win32process
import psutil


def get_pid(name: str):
    return next((p.info['pid'] for p in psutil.process_iter(['pid', 'name']) if p.info['name'].lower() == name.lower()), None)
def is_focus(pid: int):
	return pid == win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())[1]


pid = get_pid("javaw.exe")
Held = False
# Enabled = True

# while Enabled == True:
#     if win32api.GetKeyState(0x01) < 0:
#         print("Clicking")
#         pyautogui.click()
y = "Clicking"
n = "Not Clicking"
while True:
    if is_focus(pid):
        if win32api.GetKeyState(0x01) < 0:
            pyautogui.click(clicks=random.randint(1,2))
            pyautogui.mouseDown()
            print(y)
        else:
            print(n)
        
