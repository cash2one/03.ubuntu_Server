# -*- coding:utf8 -*-
import time
from flask import make_response
import requests
import json

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
    if msg['Content'] == '0':
        content = u'欢迎关注【乐影客】，我们将为你提供最新而且实用的观影信息!\n1.先看看最火的影片。\n2.找个影院去看电影。\n3.有优惠吗？\n4.很无聊不知道干什么。\n0.任何时候回复0，都将回到这里。'
        response_content = dict(content = content,touser = msg['FromUserName'],fromuser = msg['ToUserName'],createtime = str(int(time.time())))
        #userinfo_add(msg)
        #print to_unicode(text_reply).format(**response_content)
        return make_response(to_unicode(text_reply).format(**response_content))
    else:
        return tuling(msg)


def tuling(msg):
        url='http://www.tuling123.com/openapi/api'
        data={'key':'fa78fe2fbb85c914c7126d42bc7c3ebb','info':msg['Content'],'userid':msg['FromUserName']}
        r = requests.post(url,data=data)
        ans = json.loads(r.text)

        if ans['code'] == 100000:
            content = ans['text']
            response_content = dict(content = content,touser = msg['FromUserName'],fromuser = msg['ToUserName'],createtime = str(int(time.time())))
            return make_response(to_unicode(text_reply).format(**response_content))
        elif ans['code'] == 200000:
            content = ans['text'] + "\n\n" + ans['url']
            response_content = dict(content = content,touser = msg['FromUserName'],fromuser = msg['ToUserName'],createtime = str(int(time.time())))
            return make_response(to_unicode(text_reply).format(**response_content))

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