import pandas as pd
import numpy as np

def address_is(data):
    columns_name=['법정동명','본번','부번']
    columns_2 = []
    
    for i in range(len(data.columns)):
        if data.columns[i] not in columns_name:
            columns_2.append(data.columns[i])
    for i in range(len(columns_2)):
        data.drop(columns=[columns_2[i]],inplace=True)

    delet_index2 = []
    
    b =data['본번'].isnull()
    for i in range(len(data)):
      if b[i] != False:
        delet_index2.append(i)

    for i in range(len(delet_index2)):
      data.drop(delet_index2[i], axis =0 ,inplace =True)

    data=data.reset_index(drop=True)
    print(data.info())
    address=[]
    for i in range(len(data)):
        address_text1 = data.values[i,0] #법정동명
        if data.values[i,1] == type(float):
            address_text2 = int(data.values[i,1])
        else:
            address_text2 = data.values[i,1]
        address_text3 = int(data.values[i,2]) #부번
        if data.values[i,2] == 0:
            address_text = ("%s %s"%(address_text1,address_text2))
            address.append(address_text)
        else:
            address_text = ("%s %s-%s"%(address_text1,address_text2,address_text3))
            address.append(address_text)
    address_df = pd.DataFrame(address,columns=['지번 주소'])
    return address_df

## 메인코드
year = ['2015','2016','2017','2018','2019','2020','2021','2022']
csv = pd.read_csv("C:/Users/wogh2/OneDrive/바탕 화면/seoul_real-estate/csv모음.csv",encoding = 'cp949',low_memory=False)

for i in range(len(csv)):
    data = pd.read_csv("C:/Users/wogh2/OneDrive/바탕 화면/seoul_real-estate/csv 모음/서울시 부동산 실거래가 정보 ("+str(year[i])+").csv" ,encoding = 'cp949', low_memory=False)
    df = address_is(data)
    df.to_csv("주소모음("+str(year[i])+").csv", sep=',', index = False, encoding = 'utf-8')


