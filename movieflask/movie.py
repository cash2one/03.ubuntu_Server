# -*- coding:utf8 -*-
import time
from flask import Flask,g,request,render_template,request,flash,url_for,make_response,g,redirect

from database.datamodule import before_request_handler,after_request_handler,tb_movies,tb_links,tb_doubans
from resetfulutils import *
import json
from common import getmovie_port

movie_app = Flask(__name__)
movie_app.secret_key = 'some_secret'

MAX_NUM = 60
def startresetful(port=getmovie_port()):
    print "启动电影的api %s 进程:%s" %(port,os.getpid())
    movie_app.run(host='0.0.0.0', port=port)

@movie_app.before_request
def before_request():
    before_request_handler()


@movie_app.teardown_request
def teardown_request(exception):
    after_request_handler()


def get_args(args):

    page_limit = int(args.get('page_limit')) if args.get('page_limit') else 20
    page_start = int(args.get('page_start')) if args.get('page_start') else 0

    return {
        'page_limit':page_limit,
        'page_start':page_start,
    }

# 查找最近更新的电影
@movie_app.route('/movies/new_update_movies/', methods= ['GET'])
def new_update_movies_count():
    if request.method == "GET":
        opt = get_args(request.args)
        data = [dic for dic in tb_movies.select().order_by(tb_movies.updatetime.desc()).paginate(opt['page_start'],opt['page_limit']).dicts()]
        page = tb_movies.select().count() / opt['page_limit'] + (1 if len(data) % opt['page_limit'] >0 else 0)
        current = opt['page_start']
        d = {'data':data,'page':page,'current':current}

        return make_jsonresponse(d)

# 查找某年的电影
@movie_app.route('/movies/year/<year>', methods= ['GET'])
def new_movies(year):
    if request.method == "GET":
        opt = get_args(request.args)
        data = [dic for dic in tb_movies.select().where(tb_movies.year == year).order_by(tb_movies.rating.desc()).paginate(opt['page_start'],opt['page_limit']).dicts()]
        page = tb_movies.select().where(tb_movies.year == year).count() / opt['page_limit']
        current = opt['page_start']
        d = {'data':data,'page':page,'current':current}

        return make_jsonresponse(d)

# 查找所有年份
@movie_app.route('/movies/years/', methods = ['GET'])
def get_years():
    if request.method == "GET":
        data = [dic for dic in tb_movies.select().group_by(tb_movies.year).order_by(tb_movies.year.desc()).dicts()]

        return make_jsonresponse(data)

# 查找种类
@movie_app.route('/movies/cate/<cate>', methods = ['GET'])
def cate_movies(cate):
    if request.method == "GET":
        if cate == 'science':
            opt = get_args(request.args)
            data = [dic for dic in tb_movies.select().where(tb_movies.cate.contains('科幻')).order_by(tb_movies.rating.desc()).paginate(opt['page_start'],opt['page_limit']).dicts()]

            page = tb_movies.select().where(tb_movies.cate.contains('科幻')).count() / opt['page_limit']
            current = opt['page_start']
            d = {'data':data,'page':page,'current':current}

            return make_jsonresponse(d)

# 查找某个名字的电影
@movie_app.route('/movies/name/<name>', methods = ['GET', 'POST'])
def search(name):
    if request.method == "GET":
        opt = get_args(request.args)
        data = [dic for dic in tb_movies.select().where(tb_movies.name.contains(name)).paginate(opt['page_start'],opt['page_limit']).dicts()]
        page = tb_movies.select().where(tb_movies.name.contains(name)).count() / opt['page_limit']
        current = opt['page_start']
        d = {'data':data,'page':page,'current':current}

        return make_jsonresponse(d)
    else:
        pass

# 通过id查找link信息
@movie_app.route('/movies/link/<id>')
def links(id):
    if request.method == "GET":

        data = [dic for dic in tb_links.select().where(tb_links.movie == id).dicts()]
        return make_jsonresponse(data)
    else:
        pass

# 通过id查找详细信息
@movie_app.route('/movies/detail/<id>')
def detial(id):
    if request.method == "GET":
        data = [dic for dic in tb_doubans.select(tb_movies,tb_doubans).join(tb_movies).where(tb_doubans.movie == id).dicts()]
        return make_jsonresponse(data)
    else:
        pass

@movie_app.route('/movies/', methods = ['GET'])
def searchall():
    if request.method == "GET":
        data = [dic for dic in tb_movies.select().join(tb_doubans).dicts()]
        return make_jsonresponse(data)



@movie_app.route('/movies/<linkid>/download/', methods = ['GET', 'POST'])
def localpaths(linkid):
    if request.method == "GET":
        download_task(linkid)
        return make_jsonresponse("")
    else:
        pass

@movie_app.route('/movies/download/', methods = ['GET'])
def remotepaths():
    if request.method == "GET":
        data = [dic for dic in tb_links.select().where(tb_links.gid != "").dicts()]
        return make_jsonresponse(data)
    else:
        pass
    pass

@movie_app.route('/test/', methods = ['GET'])
def test():
    if request.method == "GET":
        print request.args
        data = [dic for dic in tb_movies.select().dicts()]
        return make_jsonresponse(data)
    else:
        pass
    pass

def make_jsonresponse(data):
    json_response = json.dumps(data, indent=4, sort_keys=False, ensure_ascii=False)
    response = make_response(json_response)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET'
    response.headers['Access-Control-Max-Age'] = '60'
    response.headers['Access-Control-Allow-Headers']='x-requested-with,content-type'
    return response