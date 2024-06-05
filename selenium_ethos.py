import web_scraping_selenium_functions as funcs

import time
import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

search_key = "Gello"

def search_page(driver):   
    funcs.scroll_to_bottom(driver, 1)
        
    #check for element
    items = driver.find_elements(By.CSS_SELECTOR, '[class="desktop-product-list-item__ProductName-sc-8wto4u-7 kjymBK"]')


    print("Searching %s items" % len(items))
    for i in items:
        ele = i.get_attribute("innerHTML")
        if(ele.find(search_key) != -1):
            print("Found")
            return True
        else:
           # print("Not Found")
           pass
    return False

def next_page(driver):
    driver.find_element(By.CSS_SELECTOR, '[class="pagination-controls__NavButton-sc-1436mnk-1 hjQwsb"]').click()
    time.sleep(1)

#selenium bypass age check
try:
    print("Accessing Webpage Via Selenium...")
    driver = webdriver.Chrome()
    driver.get("https://wilkesbarre.ethoscannabis.com/stores/ethos-wilkes-barre/products/flower")
    print("Success")
except:
	print("Failed")
    
try:
    print("Bypassing Age Check...")
    #"//button[@data-testid='age-restriction-yes'
    driver.find_element(By.CSS_SELECTOR, '[data-testid="age-restriction-yes"]').click()
    print("Success")
except:
    print("Failed")

found = False
page_number = 1
while(found == False):
    found = search_page(driver)
    next_page(driver)
    page_number += 1
    if page_number > 5:
        break

if(found == False):
    print("Not Found")
    

