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
homepage = "http://emart.ssg.com/"
loginpage = "https://member.ssg.com/member/popup/popupLogin.ssg?originSite=http%3A//emart.ssg.com&t=&gnb=login"
itempage = "http://emart.ssg.com/item/itemView.ssg?itemId=1000042290732&ckwhere=linkprice"

userid = ""
userpassword = ""
SLEEPSEC = 2


#%%
def login_button(driver):
    driver.get(loginpage)
    driver.find_element_by_xpath("//*[@id='mem_id']").send_keys(userid)
    driver.find_element_by_xpath("//*[@id='mem_pw']").send_keys(userpassword)    
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[1]/form/div[5]/button/span").click()
    time.sleep(1)
    print('login done. emart_dong')
    
def search_site(driver):
    global itempage
    while(True):
        cu = driver.current_url
        if cu.find("http://emart.ssg.com/item/itemView.ssg?itemId=1000042290732&ckwhere=linkprice") != -1:
            itempage = cu
            print(cu)
            break

def search_button(driver):
    i=1
    driver.get(itempage)
    while(True):
        try:
            #driver.find_element_by_xpath("//*[@id='_ordOpt_area']/dl/dd/div").click()
            #driver.find_element_by_xpath("//*[@id='_ordOpt_area']/dl/dd/div/div/ul/li[2]").click()
            driver.find_element_by_xpath("//*[@id='actionPayment']").click()
            print('go to payment.')
            break
        except:
            time.sleep(15)
            print('do emart_dong', i)
            i=i+1
            driver.get(itempage)
            

def check_payment(driver):
    #time.sleep(SLEEPSEC)
    while(True):
        try:
            driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/form[1]/div[4]/div[1]/div/div/div/div[3]/div/span/label/span[1]").click()
            driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/form[1]/div[4]/div[1]/div/div/div/div[3]/button").click()
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
