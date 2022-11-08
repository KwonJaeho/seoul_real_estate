import pandas as pd
import numpy as np
import requests, json
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_location(address):
  url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
  # 'KaKaoAK '는 그대로 두시고 개인키만 지우고 입력해 주세요.
  headers = {"Authorization": "KakaoAK 개인키"}
  api_json = json.loads(str(requests.get(url,headers=headers).text))
  address = api_json['documents'][0]['address']
  crd = {"lat": str(address['y']), "lng": str(address['x'])}
  address_name = address['address_name']

  return crd

def file_process(info):
    
    if '지번구분명' in info.columns:
        info.drop(info.columns[[4,13,17,18]],axis = 'columns',inplace =True)
    delet_index1 = []
    a =info['취소일'].isnull()
    for i in range(len(info)):
      if a[i] == False:
        delet_index1.append(i)

    for i in range(len(delet_index1)):
      info.drop(delet_index1[i], axis =0 ,inplace =True)

    info.drop(info.columns[12],axis = 'columns',inplace =True)

    info=info.reset_index(drop=True)

    delet_index2 = []
    b =info['본번'].isnull()
    for i in range(len(info)):
      if b[i] != False:
        delet_index2.append(i)

    for i in range(len(delet_index2)):
        info.drop(delet_index2[i], axis =0 ,inplace =True)

    info=info.reset_index(drop=True)

    address=[]
    for i in range(len(info)):
        address_text1 = info.values[i,3]
        address_text2 = info.values[i,4]
        if info.values[i,5] == 0:
            if type(address_text2) == float:
                address_text2 = math.floor(address_text2)
                address_text = ("%s %s"%(address_text1,address_text2))
                address.append(address_text)
            else:
                address_text = ("%s %s"%(address_text1,address_text2))
                address.append(address_text)
        else:
            address_text3 = info.values[i,5]
            if type(address_text2) == float:
                address_text2 = math.floor(address_text2)
                address_text3 = math.floor(address_text3)
                address_text = ("%s %s-%s"%(address_text1,address_text2,address_text3))
                address.append(address_text)
            else:
                address_text = ("%s %s-%s"%(address_text1,address_text2,address_text3))
                address.append(address_text)
    print(address)
    driver=set_chrome_driver()
    driver.implicitly_wait(5)

    driver.get('https://www.juso.go.kr/openIndexPage.do')
    driver.minimize_window()

    search_box = driver.find_element(By.NAME, value="searchKeyword")
    
    new_address_list=[]
    
    for i in range(len(address)):
        search_box.send_keys(address[i])
        search_box.send_keys(Keys.RETURN)
        count = str(driver.find_element(By.CLASS_NAME,value="count").text)
        
        if count == '0':
            info.drop([i], axis =0 ,inplace =True)
        else:
            new_address = str(driver.find_element(By.CLASS_NAME,value="roadNameText").text)
            new_address_list.append(new_address)
        driver.back()
        driver.find_element(By.XPATH,'//*[@id="AKCFrm"]/fieldset/div/div[1]/a').click()
    driver.quit()
    
    info=info.reset_index(drop=True)
    
    x,y = lat_process(info,new_address_list)
    
    info['x'] = x
    info['y'] = y
    return info
      
def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def lat_process(info,address):

    x = []
    y = []
    
    for i in range(len(address)):
        crd = get_location(address[i])
        x.append(crd['lat'])
        y.append(crd['lng'])
        
    return x,y
text = pd.read_csv("./csv모음.csv",encoding='cp949',low_memory=False)
csv = []
for i in range(len(text)):
    csv.append(text.values[i,0])
df = []
for i in range(len(csv)):
    info = pd.read_csv("./"+str(csv[i])+".csv", encoding = 'cp949',low_memory = False)
    file = file_process(info)
    df.append(file)
    

df_all = pd.concat(df, ignore_index=True)
df_all.to_csv("test1.csv", sep=',', index = False, encoding = 'utf-8')
