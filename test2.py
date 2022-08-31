import re
from pymongo import MongoClient
import certifi
ca = certifi.where()
# client = MongoClient('mongodb+srv://root:1860@cluster0.8fpka1h.mongodb.net/?retryWrites=true&w=majority')
client = MongoClient('mongodb+srv://test:qmzp9128@cluster0.8uddjgf.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
# client = MongoClient('mongodb+srv://test:qmzp9128@cluster0.8uddjgf.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route("/upload", methods=['POST'])
def upload():
    img = request.files['image']
    print(img)
    return jsonify({'msg':'저장에 성공했습니다.'})

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/upload", methods=['POST'])
def upload():
    ## file upload ##
    img = request.files['image']

    ## GridFs를 통해 파일을 분할하여 DB에 저장하게 된다
    fs = gridfs.GridFS(db)
    fs.put(img, filename='name')

    ## file find ##
    data = client.grid_file.fs.files.find_one({'filename': 'name'})

    ## file download ##
    my_id = data['_id']
    outputdata = fs.get(my_id).read()
    output = open('./images/' + 'back.jpeg', 'wb')
    output.write(outputdata)
    return jsonify({'msg': '저장에 성공했습니다.'})


if __name__ == '__main__':
    app.run(debug=True)