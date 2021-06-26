from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


import geocoder
g = geocoder.ip('me')
print(g.latlng)


driver = webdriver.Chrome(executable_path=r'D:\chromedriver.exe')
driver.get("https://www.naaf.no/pollenvarsel/")



# Finner riktig element jeg vil lese av, mangler dog mer.
elem = driver.find_element_by_link_text "Moderat")

str = ("spread-level-text-today")











