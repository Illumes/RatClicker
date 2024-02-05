import pyautogui
import win32api
import random
import win32gui
import win32process
import psutil
import pyfiglet
import time
import os


def get_pid(name: str):
    return next((p.info['pid'] for p in psutil.process_iter(['pid', 'name']) if p.info['name'].lower() == name.lower()), None)
def is_focus(pid: int):
	return pid == win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())[1]


pid = get_pid("javaw.exe")

y = "Clicking"
n = "Not Clicking"
os.system("cls")
os.system("title RatClicker V1.0 - Made by Illumes")
choice = input("What type of clicks do you want(Double, Jitter, Butterfly) ")
os.system("cls")
print(pyfiglet.figlet_format("RatClicker V1.0", font="Ogre"))
print(f"Started!\n\nMode: {choice}")

if choice.lower() == "butterfly":
    print("Butterfly flags on sparky currently")
    while True: #Butterfly! (Can flag)
        if is_focus(pid):
            if win32api.GetKeyState(0x01) < 0:
                pyautogui.click(clicks=random.randint(1,2))
                pyautogui.mouseDown()
                time.sleep(0.01)
elif choice.lower() == "jitter":
    while True: #Jitter!
        if is_focus(pid):
            if win32api.GetKeyState(0x01) < 0:
                pyautogui.click(clicks=random.randint(1,2))
                pyautogui.mouseDown()
                time.sleep(0.05)
elif choice.lower() == "double":
    while True: #Double Clicker!
        if is_focus(pid):
            if win32api.GetKeyState(0x01) < 0:
                time.sleep(0.1)
                pyautogui.click()
else:
    print("Not a valid choice")

