from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test",methods=['POST'])
def print_message():
    print(request.data)
    return 'Received alert!'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
