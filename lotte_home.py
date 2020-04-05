# -*- coding: cp949 -*-
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
homepage = "http://www.lotteimall.com/goods/viewGoodsDetail.lotte?goods_no=1534830498&chl_dtl_no=000100&chl_no=87#"
loginpage = "https://secure.lotteimall.com/member/login/forward.LCLoginMem.lotte?sty=logout#"
itempage = "http://www.lotteimall.com/goods/viewGoodsDetail.lotte?goods_no=1534830498&chl_dtl_no=000100&chl_no=87#"

userid = ""
userpassword = ""
SLEEPSEC = 2


#%%
def login_button(driver):
    driver.get(loginpage)
    driver.find_element_by_xpath("//*[@id='login_id']").send_keys(userid)
    driver.find_element_by_xpath("//*[@id='password']").send_keys(userpassword)    
    driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/form[1]/div/div/div[2]/div/div[1]/div/a").click()
    time.sleep(1)
    print('login done. lotte')
    
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
            driver.find_element_by_xpath("//*[@id='immOrder-btn']").click()
            print('go to payment.')
            break
        except:
            time.sleep(1)
            print(i,'lotte')
            i=i+1
            driver.get(itempage)

def check_payment(driver):
    #time.sleep(SLEEPSEC)
    while(True):
        try:
            if driver.find_element_by_xpath("//*[@id='assent']").is_selected()==False:
                driver.find_element_by_xpath("//*[@id='assent']").click()
            driver.find_element_by_xpath("//select[@name='vir_acct_bank']/option[@value='011']").click()
            driver.find_element_by_xpath("//*[@id='cr_issu_type_0']").click()
            
            driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/form[1]/div/div[1]/div[3]/div[3]/div[2]/div/div[2]/p[1]/a/img").click()
           
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
