import pyautogui
import win32api
import random
import win32gui
import win32process
import psutil
import keyboard
import time


def get_pid(name: str):
    return next((p.info['pid'] for p in psutil.process_iter(['pid', 'name']) if p.info['name'].lower() == name.lower()), None)
def is_focus(pid: int):
	return pid == win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())[1]


pid = get_pid("javaw.exe")
Held = False

y = "Clicking"
n = "Not Clicking"
Choice = input("What type of clicks do you want(Double, Jitter, Butterfly)")
print("Started!")

if Choice.lower() == "butterfly":
    while True: #Butterfly!
        if is_focus(pid):
            if win32api.GetKeyState(0x01) < 0:
                pyautogui.click(clicks=random.randint(1,2))
                time.sleep(0.01)
                pyautogui.mouseDown()
                print(y)
            else:
                print(n)
elif Choice.lower() == "jitter":
    while True: #Jitter! (Buggy)
        if is_focus(pid):
            if win32api.GetKeyState(0x01) < 0:
                pyautogui.click(clicks=random.randint(1,2))
                time.sleep(0.05)
                pyautogui.mouseDown()
                print(y)
            else:
                print(n)
elif Choice.lower() == "double":
    while True: #Double Clicker!
        if is_focus(pid):
            if win32api.GetKeyState(0x01) < 0:
                time.sleep(0.1)
                pyautogui.click()
else:
    print("Not a valid choice")



#Scrapped
# Key = "g"
# Enabled = False

# while Enabled == True:
#      if is_focus(pid): 
#         pyautogui.click(clicks=random.randint(1,2))

# while True: #Butterfly!
#     if is_focus(pid):
#         if keyboard.wait(Key):
#             if Enabled == False:
#                  Enabled = True
#                  print(Enabled)
#             else:
#                  Enabled = False
#                  print(Enabled)


