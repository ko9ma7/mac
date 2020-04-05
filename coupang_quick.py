#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

import winsound
frequency = 2500 # Set Frequency To 2500 Hertz
duration = 1000 # Set Duration To 1000 ms == 1 second

#%%
homepage = "https://www.coupang.com/vp/products/1384804427?vendorItemId=70413795361&isAddedCart="
loginpage = "https://login.coupang.com/login/login.pang?rtnUrl=https%3A%2F%2Fwww.coupang.com%2Fnp%2Fpost%2Flogin%3Fr%3Dhttps%253A%252F%252Fwww.coupang.com%252F"
itempage = "https://cart.coupang.com/cartView.pang"

userid = ""
userpassword = ""
SLEEPSEC = 2


#%%
def login_button(driver):
    driver.get(loginpage)
    driver.find_element_by_xpath("//*[@id='login-email-input']").send_keys(userid)
    driver.find_element_by_xpath("//*[@id='login-password-input']").send_keys(userpassword)    
    driver.find_element_by_xpath("/html/body/div[1]/div/div/form/div[5]/button").click()
    print('login done.')
    
def search_site(driver):
    global itempage
    while(True):
        cu = driver.current_url
        if cu.find("https://www.coupang.com/np/search") != -1:
            itempage = cu
            #winsound.Beep(frequency, duration)
            print(cu)
            break

def search_button(driver):
    i=1
    driver.get(itempage)
    time.sleep(1)
    while(True):
        try:
            if i%100 == 0:
                driver.quit()
                driver = webdriver.Firefox()
                driver.wait = WebDriverWait(driver, 2)
                login_button(driver)
                i=1
                os.system('cls')
                driver.get(itempage)
                time.sleep(1)
            cu = driver.current_url
            if cu.find("checkout") != -1:
                print('go to payment.')
                break
            if driver.find_element_by_xpath("/html/body/div[2]/section/div/table/thead/tr/th[1]/label/input").is_selected()==False:
                driver.find_element_by_xpath("/html/body/div[2]/section/div/table/thead/tr/th[1]/label/input").click()
                time.sleep(0.5)
            if driver.find_element_by_xpath("/html/body/div[2]/section/div/table/thead/tr/th[1]/label/input").is_selected()==True:
                driver.find_element_by_xpath("//*[@id='btnPay']").click()
            else:
                print(i,'loading...')
                i = i+1
                driver.get(itempage)
        except:
            print('loading...')
            driver.get(itempage)
            time.sleep(0.5)

def check_payment(driver):
    #time.sleep(SLEEPSEC)
    while(True):
        try:
            winsound.Beep(frequency, duration)
            driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[9]/div[3]/button[2]/img").click()
        except:
            print('checking fail. retry soon.')
            time.sleep(0.1)         

#%%
if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 2)

    login_button(driver)
    driver.get(homepage)
    #search_site(driver) 
    search_button(driver)
    check_payment(driver)

    """
    while(checkStock(driver, i)):
        i += 1
        time.sleep(SLEEPSEC)
        if (i > LOOP and LOOP != -1):
            break
        driver.get(ITEMURL)
    """
# %%
