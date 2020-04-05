#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

#%%
homepage = "http://www.yes24.com/Product/Goods/89493471?scode=032&OzSrank=2"
loginpage = "https://www.yes24.com/Templates/FTLogin.aspx"
itempage = "http://www.yes24.com/Product/Goods/89493471?scode=032&OzSrank=2"

userid = ""
userpassword = ""
SLEEPSEC = 2


#%%
def login_button(driver):
    driver.get(loginpage)
    driver.find_element_by_xpath("//*[@id='SMemberID']").send_keys(userid)
    driver.find_element_by_xpath("//*[@id='SMemberPassword']").send_keys(userpassword)    
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div[2]/form/fieldset/button/span/em").click()
    time.sleep(1)
    print('login done. yes24')
    
def search_site(driver):
    global itempage
    while(True):
        cu = driver.current_url
        if cu.find("http://emart.ssg.com/item/itemView.ssg?itemId=1000035476219&siteNo=6001&salestrNo=6005") != -1:
            itempage = cu
            print(cu)
            break

def search_button(driver):
    i=1
    driver.get(itempage)
    while(True):
        try:
            driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[2]/div[2]/div[2]/div/div[1]/div[2]/a[2]/span/em").click()
            print('go to payment.')
            break
        except:
            time.sleep(1)
            print(i, 'yes24')
            i = i+1
            driver.get(itempage)

def check_payment(driver):
    #time.sleep(SLEEPSEC)
    while(True):
        try:
            if driver.find_element_by_xpath("//*[@id='chkSubscribeAgree']").is_selected()==False:
                driver.find_element_by_xpath("//*[@id='chkSubscribeAgree']").click()
            if driver.find_element_by_xpath("//*[@id='chkPayAgree']").is_selected()==False:
                driver.find_element_by_xpath("//*[@id='chkPayAgree']").click()
            driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[5]/div[3]/div/div[1]/div[8]/a/img").click()
           
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
