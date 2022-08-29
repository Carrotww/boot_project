import re
from pymongo import MongoClient
import certifi
ca = certifi.where()
# client = MongoClient('mongodb+srv://root:1860@cluster0.8fpka1h.mongodb.net/?retryWrites=true&w=majority')
client = MongoClient('mongodb+srv://test:qmzp9128@cluster0.8uddjgf.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
# client = MongoClient('mongodb+srv://test:qmzp9128@cluster0.8uddjgf.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

ch_name = re.compile('^[가-힣a-zA-Z]{2,5}$')
ch_age = re.compile('^[0-9]+$')
ch_mbti = re.compile('^[a-zA-Z]+$')
ch_blog = re.compile('^(((http(s?))\:\/\/)?)([0-9a-zA-Z\-]+\.)+[a-zA-Z]{2,6}(\:[0-9]+)?(\/\S*)?$')

name_re = '유형석'
doc = {
    "name": 'hyeongseok',
    "age": 27,
    "address": '일산',
    "hobby": '축구',
    "MBTI": 'E',
    "spec": '??',
    "sytle": '??',
    "blog": '??',
    "img_url": '??'
}

db.minproject.insert_one(doc)

if not ch_name.match('유형석'):
    print('XX')
else:
    print('OO')

print(doc['name'])