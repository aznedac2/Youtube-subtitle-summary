# -- coding: utf-8 --
import json
import pymysql

def getConnection():
    return pymysql.connect(host='test.cu4sue7kfpkm.ap-northeast-2.rds.amazonaws.com', user='widim', password='kiwoom2020',
                           db='first', charset='utf8')

# datetime을 포함한 데이터를 json으로 바로 바꿀 수 있도록 추가한 함수
def user_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

# url을 parameter로 받아 history 테이블에 추가
def createURL(url):
    conn = getConnection()
    curs = conn.cursor()
    ok = curs.execute("INSERT INTO history(url, create_datetime) VALUES (%s, now())", url)
    conn.commit()
    conn.close()

    return json.dumps({'rows': ok})