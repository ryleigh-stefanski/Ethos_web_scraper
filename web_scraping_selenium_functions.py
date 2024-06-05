import time
import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

#scrolls to the bottom of the webpage using the END key
def scroll_to_bottom(driver, wait_for_load_time):
	elem = driver.find_element(By.TAG_NAME, "html")
	elem.send_keys(Keys.END)
	time.sleep(wait_for_load_time)
   
#return i = -1 if element found
def check_for_element(driver, search_key, max_elements_checked):
    i = 1
    while(i < max_elements_checked):	
        xpath =  "/html/body/div[6]/div/div[2]/div[3]/a[%s]/div/div/div[2]/div[2]" % i #xpath of elements we want to check
        print("Checking Element #%s..." % i)
        try:
            ele = driver.find_element(By.XPATH, xpath).get_attribute("innerHTML") #gets element that contains text
            if (ele.find(search_key) != -1):
                print("\nElement Found at Position #%s" % i)
                return -1
                break
            else:
                i += 1
        except:
            print("XPATH failed on element #%s" % i)
            return i