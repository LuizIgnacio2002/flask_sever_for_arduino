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
        print(data)
        return 'JSON received!'
    else:
        return 'Request is not JSON!'

@app.route('/test_server', methods=['GET'])
def test_server():
    for i in range(1_000_001):
        # Aquí puedes hacer algo con 'i' si quieres
        pass
    return 'Loop completed from 0 to 1,000,000!'

