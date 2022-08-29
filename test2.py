import re
from pymongo import MongoClient
client = MongoClient('mongodb+srv://root:1860@cluster0.8fpka1h.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

ch_name = re.compile('^[가-힣a-zA-Z]{2,5}$')
ch_age = re.compile('^[0-9]+$')
ch_mbti = re.compile('^[a-zA-Z]+$')
ch_blog = re.compile('^(((http(s?))\:\/\/)?)([0-9a-zA-Z\-]+\.)+[a-zA-Z]{2,6}(\:[0-9]+)?(\/\S*)?$')

doc = {
    "name": '유형석',
    "age": 27,
    "address": '일산',
    "hobby": '축구',
    "MBTI": 'E',
    "spec": '??',
    "sytle": '??',
    "blog": '??',
    "img_url": '??'
}

test = ch_name.match('유형석sdf')

if not ch_name.match('유형석sdfsf'):
    print('XX')
else:
    print('OO')