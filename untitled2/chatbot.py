from flask import Flask
import request
import requests
app = Flask(__name__)

@app.route('/query')
def index():
    args = request.args
    id = args.get('id')
    print(id)
    return "Query String"

if __name__ == '__main__':
    app.run(debug = True)