"""
IDEA:
create application/script that can download mp3 format songs from soundcloud to a usb

tools:

Python backend
    Problems:
    - how will python find the song?
    - what websites can be used?
    - api?
    - how will I download the song?

Maybe javascript frontend
    Problems:
    - learn javascript lol
    - simple ui
        > simple title and directions
        > enter the song
        > push the button to download
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome()

driver.get("https://downloadsound.cloud/")

time.sleep(5)

driver.quit()