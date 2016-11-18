# -*- coding:utf8 -*-
import time
from flask import Flask,g,request,render_template,request,flash,url_for,make_response,g

from database.movieDB import MovieModule,connect,close,movieinfo as Movie_tb,links as Links_tb
from resetfulutils import *
import json

apiapp = Flask(__name__)
apiapp.secret_key = 'some_secret'

def startresetful(port):
    apiapp.run(host='0.0.0.0',port=port)


@apiapp.before_request
def before_request():
    connect()

# @apiapp.teardown_request
# def teardown_request():
#     close()

@apiapp.route('/movies/',methods = ['GET'])
def searchall():
    if request.method == "GET":
        data = [dic for dic in Movie_tb.select(Movie_tb.title,Movie_tb.name,Movie_tb.cate,Movie_tb.img,Links_tb.id,Links_tb.sourceurl,Links_tb.downloadpath,Links_tb.playpath).join(Links_tb,on=(Links_tb.movieinfoid ==Movie_tb.id)).dicts()]
        return make_jsonresponse(data)

@apiapp.route('/movies/<name>',methods = ['GET','POST'])
def search(name):
    if request.method == "GET":
        data = [dic for dic in Movie_tb.select(Movie_tb.title,Movie_tb.name,Movie_tb.cate,Movie_tb.img,Links_tb.id,Links_tb.sourceurl,Links_tb.downloadpath,Links_tb.playpath).join(Links_tb,on=(Links_tb.movieinfoid ==Movie_tb.id)).where(Movie_tb.name.contains(name)).dicts()]
        return make_jsonresponse(data)
    else:
        pass

@apiapp.route('/localpaths/<id>',methods = ['GET','POST'])
def localpaths(id):
    if request.method == "GET":
        data = download(id)
        return make_jsonresponse(data)
    else:
        pass

@apiapp.route('/remotepaths/<id>',methods = ['GET'])
def remotepaths(id):
    pass






def make_jsonresponse(data):
    json_response = json.dumps(data, indent=4, sort_keys=False, ensure_ascii=False)
    response = make_response(json_response)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response