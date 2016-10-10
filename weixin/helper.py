# -*- coding:utf8 -*-
import time
from flask import make_response
import requests
import json
import logging

LOG_FILENAME="helper.log"
logging.basicConfig(filename=LOG_FILENAME,level=logging.NOTSET)


text_reply ="""
<xml>
<ToUserName><![CDATA[{touser}]]></ToUserName>
<FromUserName><![CDATA[{fromuser}]]></FromUserName>
<CreateTime>{createtime}</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[{content}]]></Content>
<FuncFlag>0</FuncFlag>
</xml>
"""

pic_reply = """
<xml>
<ToUserName><![CDATA[{toUser}]]></ToUserName>
<FromUserName><![CDATA[{fromUser}]]></FromUserName>
<CreateTime>{createtime}</CreateTime>
<MsgType><![CDATA[image]]></MsgType>
<Image>
<MediaId><![CDATA[media_id]]></MediaId>
</Image>
</xml>
 """
music_reply = """
 <xml>
 <ToUserName><![CDATA[{to}]]></ToUserName>
 <FromUserName><![CDATA[{fromuser}]]></FromUserName>
 <CreateTime>{createtime}</CreateTime>
 <MsgType><![CDATA[music]]></MsgType>
 <Music>
 <Title><![CDATA[{title}]]></Title>
 <Description><![CDATA[{description}]]></Description>
 <MusicUrl><![CDATA[{MUSIC_Url}]]></MusicUrl>
 <HQMusicUrl><![CDATA[{HQ_MUSIC_Url}]]></HQMusicUrl>
 </Music>
 <FuncFlag>0</FuncFlag>
 </xml>
"""
pic_text="""
<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[fromUser]]></FromUserName>
<CreateTime>12345678</CreateTime>
<MsgType><![CDATA[news]]></MsgType>
<ArticleCount>2</ArticleCount>
<Articles>
<item>
<Title><![CDATA[title1]]></Title>
<Description><![CDATA[description1]]></Description>
<PicUrl><![CDATA[picurl]]></PicUrl>
<Url><![CDATA[url]]></Url>
</item>
<item>
<Title><![CDATA[title]]></Title>
<Description><![CDATA[description]]></Description>
<PicUrl><![CDATA[picurl]]></PicUrl>
<Url><![CDATA[url]]></Url>
</item>
</Articles>
</xml>
"""


def to_unicode(value):
    if isinstance(value, unicode):
        return value
    if isinstance(value, basestring):
        return value.decode('utf-8')
    if isinstance(value, int):
        return str(value)
    if isinstance(value, bytes):
        return value.decode('utf-8')
    return value

def judge_text(msg):
    # 自定义对话
    if msg['Content'] == '0':
        content = u'欢迎关注一恒~'
        response_content = dict(content = content,touser = msg['FromUserName'],fromuser = msg['ToUserName'],createtime = str(int(time.time())))
        #userinfo_add(msg)
        #print to_unicode(text_reply).format(**response_content)
        return make_response(to_unicode(text_reply).format(**response_content))
    return tuling(msg)

def judge_event(msg):
    #关注事件
    if msg['Event'] == 'subscribe':
        content = u'欢迎关注一恒~\n我应该怎么称呼您?'
        response_content = dict(content = content,touser = msg['FromUserName'],fromuser = msg['ToUserName'],createtime = str(int(time.time())))
        #userinfo_add(msg)
        #print to_unicode(text_reply).format(**response_content)
        return make_response(to_unicode(text_reply).format(**response_content))
    #上报地理位置事件
    elif msg['Event'] == 'LOCATION':
        return make_response('')
        pass
    #点击菜单拉取消息时的事件推送
    elif msg['Event'] == 'CLICK':
        return make_response('')
        pass
    #点击菜单跳转链接时的事件推送
    elif msg['Event'] == 'VIEW':
        return make_response('')
        pass
    return make_response('')

def tuling(msg):
        url='http://www.tuling123.com/openapi/api'
        data={'key':'fa78fe2fbb85c914c7126d42bc7c3ebb','info':msg['Content'],'userid':msg['FromUserName']}
        r = requests.post(url,data=data)
        ans = json.loads(r.text)
        logging.debug(r.text)

        if ans['code'] == 100000:
            content = ans['text']
            response_content = dict(content = content,touser = msg['FromUserName'],fromuser = msg['ToUserName'],createtime = str(int(time.time())))
            return make_response(to_unicode(text_reply).format(**response_content))
        elif ans['code'] == 200000:
            content = ans['text'] + "\n\n" + ans['url']
            response_content = dict(content = content,touser = msg['FromUserName'],fromuser = msg['ToUserName'],createtime = str(int(time.time())))
            return make_response(to_unicode(text_reply).format(**response_content))

        return donot_know(msg)
        # ret = ''
        # if ans['code'] == 100000:
        #      = ans['text']
        # elif ans['code'] == 200000:
        #     ret = ans['text'] + '\n' + ans['url']
        # elif ans['code'] == 302000:
        #     ret = ans['text'] + '\n'
        #     for i in  ans['list']:
        #         ret = ret + i['article'] + '\n' + i['detailurl'] + '\n\n'
        # elif ans['code'] == 308000:
        #     print ans['text']
        #
        # else:
        #     ret = 'error'

        #return ret

def donot_know(msg):
    content = u"我不明白你说什么"
    response_content = dict(content = content,touser = msg['FromUserName'],fromuser = msg['ToUserName'],createtime = str(int(time.time())))
    return make_response(to_unicode(text_reply).format(**response_content))