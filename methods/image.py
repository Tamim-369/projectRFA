import pyautogui
import time
from pynput.keyboard import Controller, Key
keyboard = Controller()

def see(path):
    try:
        location = pyautogui.locateAllOnScreen(path, confidence=0.8)
        if location is not None:
            return list(location)[0] 
        return None
    except Exception as e:
        print(f"Error finding image: {e}")
        time.sleep(1)
        return None
def click(location):
    pyautogui.moveTo(location)
    time.sleep(1)
    pyautogui.click()