import pandas as pd
import pymysql as SQL
import numpy as np
from datetime import datetime
##csv 가져오기
def read_csv():
    csv = pd.read_csv("./test1.csv",encoding='utf_8',low_memory=False)
    csv = csv.replace({np.nan:None})
    return csv
## DB연결
def DB_connect():
    conn = SQL.connect(host='127.0.0.1',user='root',password='7976',db='seoul_real_estate',charset='utf8',port=3307)
    return conn

## 건물 테이블 데이터 삽입
def insert_data_building(conn):
    csv = read_csv()
    table1 = csv['자치구코드']
    table2 = csv['자치구명']
    table3 = csv['법정동코드']
    table4 = csv['법정동명']
    table5 = csv['본번']
    table6 = csv['부번']
    table7 = csv['건물명']
    table8 = csv['물건금액(만원)']
    table9 = csv['건물면적(㎡)']
    table10 = csv['토지면적(㎡)']
    table11 = csv['층']
    table12 = csv['건축년도']
    table13 = csv['건물용도']
    table14 = csv['도로명주소']
    
    cur = conn.cursor()
    sql = """INSERT INTO 건물 (자치구코드,자치구명,법정동코드,법정동명,본번,부번,건물명,물건금액,건물면적,토지면적,층,건축년도,건물용도,도로명주소)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    for i in range(len(csv)):
        cur.execute(sql,(table1[i],table2[i],table3[i],table4[i],table5[i],table6[i],table7[i],table8[i],table9[i],table10[i],table11[i],table12[i],table13[i],table14[i]))

    conn.commit()
## 지도 테이블 데이터 삽입
def insert_data_map(conn):
    csv = read_csv()
    table1 = csv['자치구코드']
    table2 = csv['자치구명']
    table3 = csv['법정동코드']
    table4 = csv['법정동명']
    table5 = csv['본번']
    table6 = csv['부번']
    table7 = csv['건물명']
    table8 = csv['x']
    table9 = csv['y']
    cur = conn.cursor()
    sql = """INSERT INTO 지도(자치구코드,자치구명,법정동코드,법정동명,본번,부번,건물명,위도,경도)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    for i in range(len(csv)):
        cur.execute(sql,(table1[i],table2[i],table3[i],table4[i],table5[i],table6[i],table7[i],table8[i],table9[i]))
    conn.commit()

    
## 실거래 테이블 데이터 삽입
def insert_data_deal(conn):
    csv = read_csv()
    
    csv1 = csv['접수연도']
    csv2 = csv['본번']
    csv3 = csv['부번']
    csv4 = csv['건물명']
    csv5 = csv['계약일']
    csv6 = csv['물건금액(만원)']
    cur = conn.cursor()
    sql = "INSERT INTO 실거래(접수년도,본번,부번,건물명,계약일,물건금액) VALUES(%s,%s,%s,%s,%s,%s)"
    for i in range(len(csv)):
        cur.execute(sql,(csv1[i],csv2[i],csv3[i],csv4[i],csv5[i],csv6[i]))
    conn.commit()


    
##메인코드
def main():
    conn = DB_connect()
    print('연결완료')
    insert_data_building(conn)
    insert_data_map(conn)
    insert_data_deal(conn)
    conn.close()
    print('연결해제')
    
if __name__=="__main__":
    print('start time:',str(datetime.now())[10:19])
    main()
    print('end time:',str(datetime.now())[10:19])
    
