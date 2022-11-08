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

if __name__ == "__main__":
    info = pd.read_csv("./주소모음(2022).csv",encoding = 'utf-8',low_memory = False)
    roadAddress_list=[]
    x = []
    y = []
    Fail_Address = []
    Fail_index = []
    for i in range(len(info)):
        address = info.values[i,0]
        try:
             roadAddress , crd = get_location(address)
             roadAddress_list.append(roadAddress)
             x.append(crd['lat'])
             y.append(crd['lng'])
        except:
            Fail_Address.append(address)
            Fail_index.append(i)


    for i in range(len(Fail_index)):
      info.drop(Fail_index[i], axis=0 , inplace = True)

    info=info.reset_index(drop=True)

    df = pd.DataFrame({"실패한 주소":Fail_Address})
    df.to_csv("실패한 주소(2022).csv",sep=',', index = False, encoding = 'utf-8')

    info['도로명주소'] = roadAddress_list
    info['x'] = x
    info['y'] = y
    info.to_csv("주소좌표(2022).csv",sep=',', index = False, encoding = 'utf-8')
