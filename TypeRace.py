# Imports
import time
from selenium import webdriver
import keyboard
import pyautogui


# Defining Chrom Drivers Path
driver = webdriver.Chrome('Your Chrome Driver Path Goes Here')


# Opening Website
driver.get("https://play.typeracer.com/")
time.sleep(5)

# Playing Game
keyboard.press_and_release('ctrl+alt+i')
time.sleep(2)

# Getting Text
text = driver.find_element_by_class_name("gameView").text
text = text.split("\n")
print(type(text))
print(text[-3])

# Sleeps Before Typing
time.sleep(15)

# Types Text
pyautogui.typewrite(text[-3],0.01)

# Sleeps For Sometime And Quits
time.sleep(15)
driver.quit()






