from pyautogui import typewrite, press, hotkey
from webbrowser import open
from time import sleep
# import pyttsx3

"""
--------------------------------------------------------------------------
Functions
--------------------------------------------------------------------------
"""
def refreshWindow():
    hotkey("ctrl", "R")
    return

def clickOnStart():
    press("win")
    sleep(0.5)
    return

def OpenApp(appName):
    MinimizeCurrentScreen()
    clickOnStart()
    typewrite(appName)
    press("enter")
    sleep(1)
    # engine = pyttsx3.init('sapi5')
    # voices = engine.getProperty('voices')
    # # print(voices[1].id)
    # engine.setProperty('voice', voices[0].id)
    # pyttsx3.speak((appName+" has been opened"))
    Maximize()
    sleep(1) # Time to perform other background tasks 
    return

def openChrome():
    textToSearch = input("Enter the text to serch : ")                
    open(textToSearch) 
    return

def openYouTube():
    textToSearch = input("Enter the text to search : ")
    open("https://www.youtube.com/results?search_query="+textToSearch)
    return 

def openWikipedia():
    articleToSearch = input("Enter the article to serch in Wikipedia: ")
    open("https://en.m.wikipedia.org/wiki/"+articleToSearch)
    return

def openAndExecuteCommand():
    cmd = input("Enter the command you want execute :")
    OpenApp(app_name)
    typewrite(cmd)
    press("enter")
    return

# @deprecated
def MinimizeCurrentScreen():
    hotkey("win", "m")
    return    

def Maximize():
    sleep(0.5)
    hotkey("win", "up")
    return

if __name__ == "__main__":
    app_name = (input("Enter the app name: ")).lower()

    if "command" in app_name or "power" in app_name:
        openAndExecuteCommand()
    elif "chrome" in app_name or "google" in app_name:
        openChrome()
    elif "youtube" in app_name or "you tube" in app_name:
        openYouTube()
    elif "wiki" in app_name:
        openWikipedia()
    else:
        OpenApp(app_name)
