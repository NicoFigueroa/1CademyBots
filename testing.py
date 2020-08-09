'''
Please implement a module that iterates through each of the "Pages" in this article. 
Note that you need to click the nextPage button programmatically to go through multiple pages.

Author: Sohan Suhas Patil
Date: 8/8/2020
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

entries = {}

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Category:Epidemiology")
assert "Epidemiology" in driver.title

css_elements = driver.find_elements_by_css_selector("div.mw-category a[href*='/wiki/']")

for elem in css_elements:
    entries[elem.text] = elem.get_attribute("href")

elem = driver.find_element_by_link_text("next page").click()

css_elements = driver.find_elements_by_css_selector("div.mw-category a[href*='/wiki/']")

for elem in css_elements:
    entries[elem.text] = elem.get_attribute("href")
    print (elem.text)

assert "No results found." not in driver.page_source
driver.close()