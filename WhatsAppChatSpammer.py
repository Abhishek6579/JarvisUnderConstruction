
from pyautogui import typewrite,keyDown
from time import sleep

def spam(text, noOFMessages=10):
    i = 1
    while i <= noOFMessages:
        typewrite(text)
        keyDown("enter")
        i += 1

if __name__ == "__main__":
    text = input("Enter the text to spam : ")
    noOFMessages = int(input("Enter the no of times you want to send the message : "))
    sleep(4)
    spam(text, noOFMessages)
