# -*- coding:utf8 -*-
import time
from flask import Flask,g,request,render_template,request,flash,url_for,make_response,g,redirect

from database.datamodule import before_request_handler,after_request_handler,tb_movies,tb_links
from resetfulutils import *
import json

apiapp = Flask(__name__)
apiapp.secret_key = 'some_secret'

def startresetful(port):
    apiapp.run(host='0.0.0.0',port=port)


@apiapp.before_request
def before_request():
    before_request_handler()


@apiapp.teardown_request
def teardown_request(exception):
    after_request_handler()


@apiapp.route('/movies/new_update_movies/',methods= ['GET'])
def new_update_movies_count():
    if request.method == "GET":
        data = [dic for dic in tb_movies.select(tb_movies,tb_links).join(tb_links).order_by(tb_movies.updatetime.desc()).limit(100).dicts()]
        return make_jsonresponse(data)

@apiapp.route('/movies/new_update_movies/<count>',methods= ['GET'])
def new_update_movies(count):
    if request.method == "GET":
        data = [dic for dic in tb_movies.select(tb_movies,tb_links).join(tb_links).order_by(tb_movies.updatetime.desc()).limit(count).dicts()]
        return make_jsonresponse(data)

@apiapp.route('/movies/',methods = ['GET'])
def searchall():
    if request.method == "GET":
        data = [dic for dic in tb_movies.select(tb_movies,tb_links).join(tb_links).dicts()]
        return make_jsonresponse(data)

@apiapp.route('/movies/<name>',methods = ['GET','POST'])
def search(name):
    if request.method == "GET":
        data = [dic for dic in tb_movies.select(tb_movies,tb_links).join(tb_links).where(tb_movies.name.contains(name)).dicts()]
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