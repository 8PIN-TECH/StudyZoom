from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/main')
def main_page():
    return "This is main page!!"

if __name__ == '__main__':
    app.run(host='자신의 IP',port=5000)