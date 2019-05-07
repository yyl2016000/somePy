# coding: UTF-8
#the ak is qx5ipuQdtGPqjawwSUGmMPtmNVv53vSk

import requests
import json
import MySQLdb

con = MySQLdb.connect(host='localhost', user='root', passwd='8421', db='baidumap', charset='utf8')
cur = con.cursor()

def get_json(loc, page_num=0):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                              '73.0.3683.103 Safari/537.36'}
    pa = {'q' : '公园',
          'region' : loc,
          'page_size' : 20,
          'page_num' : page_num,
          'output' : 'json',
          'ak' : 'qx5ipuQdtGPqjawwSUGmMPtmNVv53vSk'
    }

    r = requests.get("http://api.map.baidu.com/place/v2/search", params=pa, headers=headers)
    decode_json = json.loads(r.text)
    return  decode_json
'''
f1 = open("全国各省市公园数量.json", 'r' , encoding='utf-8')
decode_json = json.load(f1)
f1.close()
f2 = open("北京市公园数据.json", 'a', encoding='utf-8')
park_num = decode_json['results'][0]['num']
page_num = 0
while park_num >= 0:
    park_num -= 20
    f2.write(json.dumps(get_json("北京市",page_num), ensure_ascii=False, indent=4) + "\n")
    page_num += 1
if park_num < 0:
    f2.write(json.dumps(get_json("北京市", page_num), ensure_ascii=False, indent=4) + "\n")
f2.close()
'''
not_last_page = True
page_num = 0
f = open("北京市公园数据.json", 'r', encoding='utf-8')
decode_json = json.load(f)
while not_last_page:
    print('第' + str(page_num) + '页')
    if decode_json['results']:
        for each_one in decode_json['results']:
            try:
                park = each_one['name']
            except:
                park = None
            try:
                location_lat = each_one['location']['lat']
            except:
                location_lat = None
            try:
                location_lng = each_one['location']['lng']
            except:
                location_lng = None
            try:
                address = each_one['address']
            except:
                address = None
            try:
                street_id = each_one['street_id']
            except:
                street_id = None
            try:
                uid = each_one['uid']
            except:
                uid = None
            sql = """INSERT INTO baidumap.city
            (city, park, location_lat, location_lng, address, street_id, uid)
            VALUES (%s, %s, %s, %s, %s, %s, %s);"""
            cur.execute(sql, ("北京市", park, location_lat, location_lng, address, street_id, uid))
            con.commit()
        page_num += 1
    else:
        not_last_page = False
    cur.close()
    con.close()
f.close()