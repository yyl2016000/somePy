#coding=UTF-8
import MySQLdb

con = MySQLdb.connect(host='localhost', user='root', passwd='8421', db='baidumap', charset='utf8')
cur = con.cursor()

sql = """CREATE TABLE city(
    id INT NOT NULL AUTO_INCREMENT,
    city VARCHAR(200) NOT NULL,
    park VARCHAR(200) NOT NULL,
    location_lat FLOAT,
    location_lng FLOAT,
    address VARCHAR(200),
    street_id VARCHAR(200),
    uid VARCHAR(200),
    created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);"""

cur.execute(sql)
cur.close()
con.commit()
con.close()