# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 09:39:54 2021

@author: user
"""

#excel套件
import xlwings as xw
from selenium import  webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome('C:\\Users\\User\\Google 雲端硬碟\\chromedriver.exe')
url = "https://buy.housefun.com.tw/?pg=120"
driver.get(url)
wb = xw.Book(r'C:\Users\user\Desktop\sampleHOUSE.xlsx')
sht = wb.sheets['Sheet']
#從第幾頁開始爬
t = 1
#欲爬取的頁數
for i in range(50):     
    for i in range(1,31):
        driver.implicitly_wait(2)
        
        address = driver.find_element_by_xpath(f"/html/body/div[1]/div/div[1]/div/div[2]/div[2]/section[{i}]/div/div[1]/address").text 
        square_feet = driver.find_element_by_xpath(f"/html/body/div[1]/div/div[1]/div/div[2]/div[2]/section[{i}]/div/div[2]/span[1]/em[1]").text
        pattern = driver.find_element_by_xpath(f"/html/body/div[1]/div/div[1]/div/div[2]/div[2]/section[{i}]/div/div[2]/em").text 
        price = driver.find_element_by_xpath(f"/html/body/div[1]/div/div[1]/div/div[2]/div[2]/section[{i}]/div/div[4]/a/em[1]").text 
        # original_price = int(price)/int(square_feet)
        floor = driver.find_element_by_xpath(f"/html/body/div[1]/div/div[1]/div/div[2]/div[2]/section[{i}]/div/div[2]/span[2]").text 
        s = driver.find_elements_by_xpath(f'/html/body/div[1]/div/div[1]/div/div[2]/div[2]/section[{i}]/div/div[1]/a')
        for each in s:
            latitude = each.get_attribute('data-latitude')
            longitude = each.get_attribute('data-longitude')
        
        k = driver.find_elements_by_xpath(f'/html/body/div[1]/div/div[1]/div/div[2]/div[2]/section[{i}]/div/h1/a')
        for each in k:
            internet = each.get_attribute('href')
        num = t*30+i+1
        sht.range(f'A{num}').value = address
        sht.range(f'B{num}').value = square_feet
        sht.range(f'C{num}').value = longitude
        sht.range(f'D{num}').value = latitude
        sht.range(f'E{num}').value = price
        sht.range(f'F{num}').value = pattern
        sht.range(f'G{num}').value = internet
        sht.range(f'H{num}').value = floor           
    t +=1
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[3]/ul/li[13]/a").click()
driver.quit()


 
