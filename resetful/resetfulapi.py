# -*- coding:utf8 -*-
import time
from flask import Flask,g,request,render_template,request,flash,url_for,make_response,g

from database.movieDB import MovieModule

apiapp = Flask(__name__)
apiapp.secret_key = 'some_secret'

def startresetful(port):
    apiapp.run(host='0.0.0.0',port=port)



@apiapp.before_request
def before_request():
    g.db = MovieModule()

@apiapp.route('/',methods = ['GET', 'POST'])
def index():
    return make_response("test")

@apiapp.route('/movies/<name>',methods = ['GET'])
def search(name):

    result = g.db.search_name(name)
    print result
    return make_response("")
