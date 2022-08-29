import re
from pymongo import MongoClient
client = MongoClient('mongodb+srv://root:1860@cluster0.8fpka1h.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# 입력값 체크
ch_name = re.compile('^[가-힣a-zA-Z]{2,5}$')
ch_age = re.compile('^[0-9]+$')
ch_mbti = re.compile('^[a-zA-Z]+$')
ch_blog = re.compile('^(((http(s?))\:\/\/)?)([0-9a-zA-Z\-]+\.)+[a-zA-Z]{2,6}(\:[0-9]+)?(\/\S*)?$')

# Team project
@app.route('/')
def home():
   return render_template('index.html')

def input_check(doc: dict):
    if not ch_name.match(doc['name']):
        return jsonify({'msg':'이름을 확인해 주세요'})
    if not ch_age.match(doc['age']):
        return jsonify({'msg':'나이를 확인해 주세요'})
    if not ch_mbti.match(doc['mbti']):
        jsonify({'msg': '알파벳 네 자리로 입력해 주세요'})
    if not ch_blog.match(doc['blog']):
        jsonify({'msg': '블로그 형식을 확인해 주세요'})

@app.route("/index/sign", methods=["POST"])
def team_post():
    name_receive = request.form['name']
    comment_receive = request.form['comment_give']

    doc = {
        "name": name_receive,
        "age": age_receive,
        "address": address_receive,
        "hobby": hobby_receive,
        "MBTI": MBTI_receive,
        "spec": spec_receive,
        "sytle": style_receive,
        "blog": blog_receive,
        "img_url": img_url_receive
    }
    # 입력값이 정상인지 확인하는 부분
    input_check(doc)

    user_check = db.users.find_one({'name':f'{name_receive}'})
    # 입력된 사람 이름이 존재하면 DB 업데이트, 없으면 생성

    if user_check:

        return jsonify({'msg':'수정 완료!'})
    else:
        db.minproject.insert_one(doc)
        return jsonify({'msg':'팀원 추가 완료!'})

@app.route("/index/sign", methods=["GET"])
def team_get():
    comment_list = list(db.homework.find({}, {'_id': False}))
    return jsonify({'comments':comment_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)