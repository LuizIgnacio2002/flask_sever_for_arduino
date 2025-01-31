# save this as app.py
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/send_data', methods=['POST'])
def send_data():
    # check if request has json data
    if request.is_json:
        data = request.get_json()
        print(data + "123456789")
        return 'JSON received!'
    else:
        return 'Request is not JSON!'

