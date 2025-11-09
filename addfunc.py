import subprocess
from voice import Voice

v = Voice()

def addfunc(text):
    if any(k in text for k in ['打开']):
        if any(a in text for a in ['战 双', '斩 双']):
            v.speak('正在为您打开战双')
            subprocess.Popen(r"E:\Punishing Gray Raven\launcher.exe")
        if any(a in text for a in ['kk', 'KK', '开开']):
            v.speak('正在为您打开KK')
            subprocess.Popen(r"D:\RJ\kkduizhan\Platform.exe")
        if any(a in text for a in ['微信','微 信']):
            v.speak('正在为您打开微信')
            subprocess.Popen(r"D:\RJ\Weixin\Weixin.exe")
        if any(a in text for a in ['浏览器']):
            v.speak('正在为您打开浏览器')
            subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    if any(a in text for a in ['小声点']):
        v.ChandeVolume(-0.1)
    if any(a in text for a in ['大声 点']):
        v.ChandeVolume(+0.1)
    if all(a in text for a in ['你','是','谁']):
        v.speak('我是智能助手肉包')
    if any(a in text for a in ['功能']):
        v.speak('我可以帮您打开电脑中的软件')
