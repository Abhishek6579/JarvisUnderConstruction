import time
import pyautogui
# import pyttsx3
# from deprecated import deprecated
pyautogui.FAILSAFE = False

"""
-------------------------------------------------------------------------
Functions
--------------------------------------------------------------------------
"""
def refreshWindow():
    pyautogui.hotkey("ctrl", "R")
    # pyautogui.moveTo(900,900)
    # pyautogui.rightClick()
    # pyautogui.press("down")
    # pyautogui.press("down")
    # pyautogui.press("down")
    # pyautogui.press("enter")

def clickOnStart():
    pyautogui.press("win")
    time.sleep(0.5)

def OpenApp(appName):
    # refreshWindow()
    clickOnStart()
    pyautogui.typewrite(appName)
    pyautogui.press("enter")
    time.sleep(1)
    # engine = pyttsx3.init('sapi5')
    # voices = engine.getProperty('voices')
    # # print(voices[1].id)
    # engine.setProperty('voice', voices[0].id)
    # pyttsx3.speak((appName+" has been opened"))
    Maximize()
    return

def executeChrome(textToSearch):
    # MinimizeCurrentScreen()
    OpenApp("Chrome")    
    pyautogui.typewrite(textToSearch)
    pyautogui.press("enter")

def executeYouTube():
    textToSearch = input("Enter the text to serch in Youtube: ")
    MinimizeCurrentScreen()
    executeChrome("https://www.youtube.com/results?search_query="+textToSearch)

def executeWikipedia():
    articleToSearch = input("Enter the article to serch in Wikipedia: ")
    MinimizeCurrentScreen()
    executeChrome("https://en.m.wikipedia.org/wiki/"+articleToSearch)



def openAndExecuteCommand():
    cmd = input("Enter the command you want execute :")
    # MinimizeCurrentScreen()
    OpenApp(app_name)
    pyautogui.typewrite(cmd)
    pyautogui.press("enter")

# @deprecated
def MinimizeCurrentScreen():
    pyautogui.hotkey("win", "M")
    # pyautogui.moveTo(1777,27)
    # # pyautogui.hotkey("win", "down")
    # pyautogui.click()
    

def Maximize():
    time.sleep(0.5)
    pyautogui.hotkey("win", "up")
    return

if __name__ == "__main__":
    app_name = input("Enter the app name: ")

    if "command" in app_name or "power" in app_name:
        openAndExecuteCommand()
    elif "chrome" in app_name:
        textToSearch = input("Enter the text to serch : ")                
        executeChrome(textToSearch)
    elif "youtube" in app_name or "you tube" in app_name:
        executeYouTube()
    elif "wiki" in app_name:
        executeWikipedia()
    else:
        # MinimizeCurrentScreen()
        OpenApp(app_name)
