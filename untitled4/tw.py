from flask import Flask, request, jsonify, make_response
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