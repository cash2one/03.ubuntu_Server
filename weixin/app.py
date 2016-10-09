# -*- coding:utf8 -*-
import time
from flask import Flask,request, make_response,render_template,request,flash,url_for
from wechatAPI import Wechat

app = Flask(__name__)
app.secret_key = 'some_secret'
api = Wechat()

@app.route('/', methods = ['GET', 'POST'] )
def wechat():
    if request.method == 'GET':
        # 用于接入微信
        return api.check_signature(request)
    if request.method == 'POST':
        return api.response_msg(request)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
