from flask import Flask, render_template, request, jsonify
import re # 정규표현식 regex import
from pymongo import MongoClient
import requests
client = MongoClient('mongodb+srv://root:1860@cluster0.8fpka1h.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# 입력값 체크 정규표현식
ch_name = re.compile('^[가-힣a-zA-Z]{2,5}$')
ch_age = re.compile('^[0-9]+$')
ch_mbti = re.compile('^[a-zA-Z]+$')
ch_blog = re.compile('^(((http(s?))\:\/\/)?)([0-9a-zA-Z\-]+\.)+[a-zA-Z]{2,6}(\:[0-9]+)?(\/\S*)?$')

app = Flask(__name__)

# Team project
@app.route('/')
def home():
   return render_template('main.html')

def input_check(doc: dict): # dict() 형식으로 받아 입력값 체크 함수 호출
    if not ch_name.match(doc['name']):
        return jsonify({'msg':'이름을 확인해 주세요'})
    if not ch_age.match(doc['age']):
        return jsonify({'msg':'나이를 확인해 주세요'})
    if not ch_mbti.match(doc['MBTI']):
        return jsonify({'msg': 'MBTI를 알파벳 네 자리로 입력해 주세요'})
    if not ch_blog.match(doc['blog']):
        return jsonify({'msg': '블로그 형식을 확인해 주세요'})

@app.route("/team")
def show_team_list():
    return render_template('team.html')

@app.route("/team/post", methods=["POST"])
def team_post(): # 팀원 등록하기
    name_receive = request.form['name_give']
    age_receive = request.form['age_give']
    address_receive = request.form['address_give']
    hobby_receive = request.form['hobby_give']
    MBTI_receive = request.form['MBTI_give']
    spec_receive = request.form['spec_give']
    style_receive = request.form['style_give']
    blog_receive = request.form['blog_give']
    # img_url_receive = request.form['img_url_give']

    doc = {
        "name": name_receive,
        "age": age_receive,
        "address": address_receive,
        "hobby": hobby_receive,
        "MBTI": MBTI_receive,
        "spec": spec_receive,
        "style": style_receive,
        "blog": blog_receive,
        # "img_url": img_url_receive
    }
    # 입력값이 정상인지 확인하는 부분
    if input_check(doc):
        return input_check(doc)

    user_check = db.minproject.find_one({'name':f'{name_receive}'})
    # 입력된 사람 이름이 존재하면 DB 업데이트, 없으면 생성

    if user_check:
        db.minproject.update_one({'name': f'{name_receive}'}, {'$set': {'age': age_receive}})
        db.minproject.update_one({'name': f'{name_receive}'}, {'$set': {'address': address_receive}})
        db.minproject.update_one({'name': f'{name_receive}'}, {'$set': {'hobby': hobby_receive}})
        db.minproject.update_one({'name': f'{name_receive}'}, {'$set': {'MBTI': MBTI_receive}})
        db.minproject.update_one({'name': f'{name_receive}'}, {'$set': {'spec': spec_receive}})
        db.minproject.update_one({'name': f'{name_receive}'}, {'$set': {'style': style_receive}})
        db.minproject.update_one({'name': f'{name_receive}'}, {'$set': {'blog': blog_receive}})

        return jsonify({'msg':'수정 완료!'})
    else:
        db.minproject.insert_one(doc)
        return jsonify({'msg':'팀원 추가 완료!'})

@app.route("/sign", methods=["GET"])
def sign_get(): # 팀원 소개
    # comment_list = list(db.minproject.find({}, {'_id': False}))
    return render_template('sign.html')

@app.route('/mem1')
def get_mem1():
    return render_template('mem1.html')

@app.route('/project')
def Project():
   return render_template('project.html')

@app.route('/team/show_one', methods=["GET"])
def team_get():

    # if request.form['team_name']:
    #     team_name = request.form['team_name']
    #     name_list = list(db.minproject.find({'name': f'{team_name}'}, {'_id': False}))
    #     return jsonify({'test': name_list})

    first_list = list(db.minproject.find({'name': '안범기'}, {'_id': False}))
    return jsonify({'test': first_list})

@app.route('/team/show_one/user', methods=["POST"])
def team_name_get():
    team_name = request.form['name_give']
    name_list = list(db.minproject.find({'name': f'{team_name}'}, {'_id': False}))
    return jsonify({'test': name_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)