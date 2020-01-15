from flask import Flask, request, jsonify, make_response
"""
@app.route('/')
def index():
    return "Hello World!~!!~~~tw"

@app.route('/user')
def get_user():
    return "Hello User"

@app.route('/post')
def get_post():
    return "Hello Post"

@app.route('/user/list')
def get_user_list():
    return "Hello User List!!"

@app.route('/uset')
def get_uset():
    return "kimtaewoo"
"""

"""
@app.route('/user', methods=['GET'])
def get_user():
    return "GET /user called!!"

@app.route('/user', methods=['POST'])
def post_user():
    return "POST /user called!!"

@app.route('/user', methods=['PUT'])
def put_user():
    return "PUT /user called!!"

@app.route('/user', methods=['DELETE'])
def delete_user():
    return "DELETE /user called!!"
"""

"""

@app.route('/query')
def index():
    args = request.args
    id = args.get('id')
    date = args.get('date')
    print(id)
    print(date)
    return "Query String!!"

"""


"""
#get으로 요청 후 리스폰스가 json형태로 돌아온다.
@app.route('/json/object')
def get_json_object():
    response = {"id" : 1}
    return response
"""

"""
from flask import Flask, request

app = Flask(__name__)

@app.route('/json/list')
def get_json_list():
    list=[1,2,3,4,5]
    response ={"list" : list}
    return response

if __name__ == '__main__':
    app.run(debug = True)
"""

"""
from flask import Flask, request
app = Flask(__name__)

@app.route('/sensor/data/list')
def get_json_list():
    data1 = {"device_id" : "LED01", "data": "on", "datetime":"20190731"}
    data2 = {"device_id": "LED02", "data": "off", "datetime": "20190729"}
    list = [data1, data2]
    response ={"data_list" : list}
    return response

if __name__ == '__main__':
    app.run(debug = True)
"""
app = Flask(__name__)
@app.route('/', methods= ['GET', 'POST'])
def webhook():
    return make_response(jsonify(results()))

def results():
    req = request.get_json(force = True)
    print(req)
    print('----------------------------')
    queryText = req.get('queryResult').get('queryText')
    print(queryText)
    return {'fulfillmentText' : 'This is a response from webhook.'}


if __name__ == '__main__':
    app.run(debug = True)