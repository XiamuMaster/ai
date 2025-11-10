import subprocess
import pygetwindow as gw
from func.voice import Voice
v = Voice()

class Openapp:
    def __init__(self,process_name,app_path):
        self.process = process_name
        self.app_path = app_path

    def is_app_running(self):
        try:
            if gw.getWindowsWithTitle(self.process):
                v.speak(f'主人，您已开启{self.process}，正在为您展示')
                window = gw.getWindowsWithTitle(self.process)[0]
                if window.isMinimized:
                    window.restore()
                    # 激活并置前窗口
                window.activate()
                print(f"✅ {self.process}窗口已置前")
                return True
            else:
                v.speak(f'主人，您未启动{self.process}，正在为您开启')
                subprocess.Popen(self.app_path)
        except Exception as e:
            print(e)
def run(process_name,app_path):
    o = Openapp(process_name=process_name,app_path=app_path)
    o.is_app_running()

