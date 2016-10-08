# -*- coding:utf8 -*-
import time
from flask import Flask,request, make_response,render_template,request,flash,url_for

from wechatAPI import WechatBase

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/', methods = ['GET', 'POST'] )
def wechat():
    resp = make_response('')
    baseopt = WechatBase()
    try:
        if request.method == 'GET':
            # 用于接入微信
            resp = make_response(baseopt.wechat_auth(request))
        else:
            # 取的access token
            # api.get_token();

            # 被动回复用户消息
            # replydata = api.recv_reply(request.data)

            # resp = make_response(replydata)
            # resp.content_type = 'application/xml'
            pass
    except Exception,X:
        resp =  make_response(X)
    finally:
        return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
