import pandas as pd
import numpy as np
import requests, json

def get_location(address):
  url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
  # 'KaKaoAK '는 그대로 두시고 개인키만 지우고 입력해 주세요.
  headers = {"Authorization": "KakaoAK 개인키"}
  api_json = json.loads(str(requests.get(url,headers=headers).text))
  address = api_json['documents'][0]['address']
  roadAddress = api_json['documents'][0]['road_address']['address_name']
  crd = {"lat": str(address['y']), "lng": str(address['x'])}
  address_name = address['address_name']
  
  return roadAddress,crd

def data_process(data):    
    delet_index1 = []
    a =data['취소일'].isnull()
    for i in range(len(data)):
      if a[i] == False:
        delet_index1.append(i)

    for i in range(len(delet_index1)):
      data.drop(delet_index1[i], axis =0 ,inplace =True)
      
    data = data.reset_index(drop=True)

    columns = ['지번구분','지번구분명','권리구분','취소일','신고구분','신고한 개업공인중개사 시군구명']
    
    for i in range(len(columns)):
        data.drop(columns=[columns[i]],inplace=True)

    delet_index2 = []
    
    b =data['본번'].isnull()
    for i in range(len(data)):
      if b[i] != False:
        delet_index2.append(i)

    for i in range(len(delet_index2)):
      data.drop(delet_index2[i], axis =0 ,inplace =True)

    data=data.reset_index(drop=True)

    
    address=[]
    for i in range(len(data)):
        address_text1 = data.values[i,4] #법정동명
        if data.values[i,7] == type(float):
            address_text2 = int(data.values[i,5])
        else:
            address_text2 = data.values[i,5]
        address_text3 = int(data.values[i,6]) #부번
        if data.values[i,6] == 0:
            address_text = ("%s %s"%(address_text1,address_text2))
            address.append(address_text)
        else:
            address_text = ("%s %s-%s"%(address_text1,address_text2,address_text3))
            address.append(address_text)

    roadAddress_list=[]
    x = []
    y = []
    Fail_Address = []
    Fail_index = []
    for i in range(len(data)):
        try:
             roadAddress , crd = get_location(address[i])
             roadAddress_list.append(roadAddress)
             x.append(crd['lat'])
             y.append(crd['lng'])
        except:
            Fail_Address.append(address)
            Fail_index.append(i)
   
    for i in range(len(Fail_index)):
      data.drop(Fail_index[i], axis=0 , inplace = True)

    data=data.reset_index(drop=True)

    
    data['도로명주소'] = roadAddress_list
    data['x'] = x
    data['y'] = y

    return data

## 메인 코드

data = pd.read_csv("부동산 정보.csv" ,encoding = 'utf-8', low_memory=False)
df = data_process(data)
df.to_csv("부동산 정보.csv", sep=',', index = False, encoding = 'utf-8')
