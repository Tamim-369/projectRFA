from .methods.image import see, click
import pyautogui
import time
while True:
        location = see('images/facebook.png')
        shortLocation = see('images/short.png')
        print(location)
        if location is not None:
           pyautogui.hotkey('ctrl', 'w')
           time.sleep(2)
        if shortLocation is not None:
           pyautogui.hotkey('ctrl', 'w')
           time.sleep(2)
        else: 
             print("Trying again...")
    