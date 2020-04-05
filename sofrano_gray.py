#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import sys
import os
from multiprocessing import Process
#reload(sys)
#sys.setdefaultencoding('utf-8')

#%%
homepage = "https://sofrano.com/"
loginpage = "https://sofrano.com/member/login.html"
itempage = "https://sofrano.com/product/detail.html?product_no=555&cate_no=55&display_group=1"

userid = ""
userpassword = ""
SLEEPSEC = 2

pcflag = False

#%%
def login_button(driver):
    driver.get(loginpage)
    driver.find_element_by_xpath("//input[@id='member_id']").send_keys(userid)
    driver.find_element_by_xpath("//input[@id='member_passwd']").send_keys(userpassword)    
    driver.find_element_by_xpath("//a[@class='loginBtn -mov']").click()
    print('login done.')
    
def search_site(driver):
    """
    global itempage
    while(True):
        cu = driver.current_url
        if cu.find("detail") != -1:
            itempage = cu
            print(cu)
            break
    """
    driver.get(itempage)

def search_button(driver):
    global pcflag
    i = 1
    driver.get(itempage)
    while(True):
        try:
            driver.find_element_by_xpath("//div/a[@id='btnBuy']").click()
            print('go to payment.')
            break
        except:
            try:
                driver.find_element_by_xpath("//div/a[@onclick='add_wishlist(this, true);']")
                driver.get(itempage)
                if pcflag:
                    print('pc2', i, ' no item. retry soon.')
                else:
                    print('pc1', i, ' no item. retry soon.')
                
            except:
                print('loading...')
                cu = driver.current_url
                print(cu)
                
            time.sleep(0.5)
            i = i + 1
            if i % 50 == 0:
                os.system('cls')
            if i == 145:
                if pcflag:
                    pc1.start()
                else:
                    pc2.start()
            if i > 150:
                driver.quit()
                os.system('cls')
                if pcflag:
                    pc2.terminate()
                else:
                    pc1.terminate()

def check_payment(driver):
    #time.sleep(SLEEPSEC)
    while(True):
        try:
            if driver.find_element_by_xpath("//input[@id='chk_purchase_agreement0']").is_selected()==False:
                driver.find_element_by_xpath("//input[@id='chk_purchase_agreement0']").click()
            driver.find_element_by_xpath("//img[@id='btn_payment']").click()
        except:
            print('checking fail. retry soon.')
            time.sleep(0.1)

def work(pcflag):
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 2)

    login_button(driver)    
    search_site(driver)
    search_button(driver)
    check_payment(driver)

pc1 = Process(target=work, args=(pcflag,))
pc2 = Process(target=work, args=(~pcflag,))
#%%
if __name__ == "__main__":
    pc1.start()
# %%
