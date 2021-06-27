from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


import geocoder
g = geocoder.ip('me')
print(g.latlng)


driver = webdriver.Chrome(executable_path=r'D:\chromedriver.exe')
driver.get("https://www.naaf.no/pollenvarsel/")


el=driver.find_element_by_class_name('text-spread-level')
val=el.text
    

print(val)
















