# -*- coding:utf8 -*-
import time
from flask import Flask,g,request,render_template,request,flash,url_for
from wechatAPI import Wechat

from helper import *
app = Flask(__name__)
app.secret_key = 'some_secret'
api = Wechat()


@app.before_request
def before_request():
    pass


@app.teardown_request
def teardown_request(exception):
    pass

@app.route('/photolist/')
def getphotolist():
    return get_photolist()

@app.route('/', methods = ['GET', 'POST'] )
def wechat():
    if request.method == 'GET':
        # 用于接入微信
        return api.check_signature(request)
    if request.method == 'POST':
        return api.response_msg(request)
@app.route('/test/')
def test():
    return make_response('hello')

def startweixin(port):
    print "启动微信服务"
    app.run(host='0.0.0.0',port=port)


