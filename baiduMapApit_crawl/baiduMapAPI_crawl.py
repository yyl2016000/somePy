# coding: UTF-8
#the ak is qx5ipuQdtGPqjawwSUGmMPtmNVv53vSk

import requests
import json

def get_json(loc, page_num=1):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                              '73.0.3683.103 Safari/537.36'}
    pa = {'q' : '公园',
          'region' : 'loc',
          'page_size' : 20,
          'page_num' : page_num,
          'output' : 'json',
          'ak' : 'qx5ipuQdtGPqjawwSUGmMPtmNVv53vSk'
    }

    r = requests.get("http://api.map.baidu.com/place/v2/search", params=pa, headers=headers)
    decode_json = json.loads(r.text)
    return  decode_json

f = open("全国各省市公园数量.json", 'a' , encoding='utf-8')
f.write(json.dumps(get_json("北京市"), ensure_ascii=False, indent=4) + "\n")
f.close()