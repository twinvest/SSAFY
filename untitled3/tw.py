from flask import Flask
import request
#import requests
app = Flask(__name__)

@app.route('/query')
def index():
    return "helloworld!"

if __name__ == '__main__':
    app.run(debug = True)