import pyttsx3

class Voice:
    def __init__(self):
        self.volume= 1.5

    def speak(self,text):
        engine = pyttsx3.init()
        engine.setProperty('volume',self.volume)
        engine.say(text)
        engine.runAndWait()

    def ChandeVolume(self,changenum):
        self.volume += changenum
        self.speak('已按照主人要求修改音量')


