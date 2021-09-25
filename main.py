import webbrowser
import time
import os

url = ("https://gamehag.com/tv-zone")
duration = ("20")

while True:
    for i in range(40): # Kolko Taba da otvori
        webbrowser.open(url)
        time.sleep(int(duration))


    time.sleep(90) # Kolko vreme sled kogato e prikluchilo
    os.system("taskkill /im chrome.exe /f") # Kills Chrome


