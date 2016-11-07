# -*- coding:utf8 -*-
import time
from flask import Flask,g,request,render_template,request,flash,url_for,make_response,g

from database.movieDB import MovieModule,connect,close,movieinfo as Movie_tb
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



@apiapp.route('/',methods = ['GET', 'POST'])
def index():
    return make_response("test")

@apiapp.route('/movies/<name>',methods = ['GET'])
def search(name):
    response = [dic for dic in Movie_tb.select(Movie_tb.id,Movie_tb.name).where(Movie_tb.name.contains(name)).dicts()]
    json_response = json.dumps(response, indent=4, sort_keys=False, ensure_ascii=False)
    return make_response(json_response)

# def export(table, sql, export_format):
#     model_class = dataset[table].model_class
#     query = model_class.raw(sql).dicts()
#     buf = StringIO()
#     if export_format == 'json':
#         kwargs = {'indent': 2}
#         filename = '%s-export.json' % table
#         mimetype = 'text/javascript'
#     else:
#         kwargs = {}
#         filename = '%s-export.csv' % table
#         mimetype = 'text/csv'
#
#     dataset.freeze(query, export_format, file_obj=buf, **kwargs)
#
#     response_data = buf.getvalue()
#     response = make_response(response_data)
#     response.headers['Content-Length'] = len(response_data)
#     response.headers['Content-Type'] = mimetype
#     response.headers['Content-Disposition'] = 'attachment; filename=%s' % (
#         filename)
#     response.headers['Expires'] = 0
#     response.headers['Pragma'] = 'public'
#     return response
