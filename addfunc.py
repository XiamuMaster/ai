import subprocess
from openweb import OpenWeb
from openapp import run
from func.voice import Voice
v = Voice()
def addfunc(text):
    if any(k in text for k in ['打开']):
        if any(a in text for a in ['战 双', '斩 双']):
            run('战双帕弥什', r"E:\Punishing Gray Raven\launcher.exe")
        if any(a in text for a in ['kk', 'KK', '开开']):
            run('KK对战平台', r"D:\RJ\kkduizhan\Platform.exe")
        if any(a in text for a in ['微信','微 信']):
            run('微信',r"D:\RJ\Weixin\Weixin.exe")
        if any(a in text for a in ['浏览器']):
            v.speak('正在为您打开浏览器')
            subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
        if any(a in text for a in ['百度','百 度']):
            o = OpenWeb()

    if any(a in text for a in ['小声点']):
        v.ChandeVolume(-0.1)
    if any(a in text for a in ['大声 点']):
        v.ChandeVolume(+0.1)
    if all(a in text for a in ['你','是','谁']):
        v.speak('我是智能助手肉包')
    if any(a in text for a in ['功能']):
        v.speak('我可以帮您打开电脑中的软件')
