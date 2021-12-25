import time
import pyttsx3
from AppletOpener import OpenApp
from AppletOpener import Maximize
import pyautogui
from AppletOpener import MinimizeCurrentScreen

if __name__ == "__main__":
    # webbrowser.open_new("chrome://dino")
    MinimizeCurrentScreen()
    OpenApp("Chrome")
    # pyautogui.moveTo(300,300)
    # pyautogui.doubleClick()
    pyautogui.moveTo(618,95)
    # time.sleep(1)
    pyautogui.click()
    time.sleep(0.5)
    # pyautogui.press("f11")
    pyautogui.typewrite("chrome://dino")
    pyautogui.press("enter")
    # time.sleep(0.5)
    # pyautogui.moveTo(1228,50)
    # pyautogui.click()

    time.sleep(0.5)

    pyautogui.press("space")
    pyttsx3.speak("Dino game has been started !")
    Maximize()