from DrissionPage import Chromium
from voice import Voice
import speech_recognition as sr
from main import RealTimeSpeechRecognizer
import time

class OpenWeb:
    def __init__(self):
        self.chrome = Chromium().latest_tab
        self.v = Voice()
        self.recognizer = sr.Recognizer()

    def baidu(self,text):
        self.chrome.get(url='https://www.baidu.com')
        time.sleep(2)
        self.v.speak('已帮主人打开百度，请继续下一步指示')





p = OpenWeb()
p.baidu()