import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)



if __name__ == "__main__":
    pyttsx3.speak("Hello, Peter!!")
    print("The program spoke!!")