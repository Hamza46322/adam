# applications.py

import threading
import subprocess
import webbrowser

# Websites
def open_google():
    x = lambda: webbrowser.open_new_tab('http://google.com')
    t = threading.Thread(target=x)
    t.start()

def open_facebook():
    x = lambda: webbrowser.open_new_tab('https://www.facebook.com/')
    t = threading.Thread(target=x)
    t.start()

def open_youtube():
    x = lambda: webbrowser.open_new_tab('https://www.youtube.com/')
    t = threading.Thread(target=x)
    t.start()

def open_instagrams():
    x = lambda: webbrowser.open_new_tab('https://www.instagram.com/')
    t = threading.Thread(target=x)
    t.start()

# Applications
def open_calculator():
    x = lambda: subprocess.Popen(['calc.exe'])
    t = threading.Thread(target=x)
    t.start()

def open_notepad():
    x = lambda: subprocess.Popen(['notepad.exe'])
    t = threading.Thread(target=x)
    t.start()
