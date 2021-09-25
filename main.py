import webbrowser
import time
import os

url = ("https://gamehag.com/tv-zone")
duration = ("20")

while True:
    for i in range(40): # How many tabs to open
        webbrowser.open(url)
        time.sleep(int(duration))


    time.sleep(90) # How much time after the last tab is opened to kill chrome
    os.system("taskkill /im chrome.exe /f") # Kills Chrome


