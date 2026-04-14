# lets do selenium task - automate youtube

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

webdriver = webdriver.Chrome() 
webdriver.get('https://www.youtube.com')

time.sleep(5)

webdriver.quit()




# # lets do windows actions

webdriver.maximize_window() # maximize the window
time.sleep(2)