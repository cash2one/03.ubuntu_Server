# -*- coding:utf8 -*-
import time
from flask import make_response


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
    <ToUserName><![CDATA[{to}]]></ToUserName>
    <FromUserName><![CDATA[{fromuser}]]></FromUserName>
    <CreateTime>{createtime}</CreateTime>
    <MsgType><![CDATA[news]]></MsgType>
    {article}
    <FuncFlag>1</FuncFlag>
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
    if msg['Content'] == 'Hello2BizUser'or msg['Content'] == '0':
        content = u'欢迎关注【乐影客】，我们将为你提供最新而且实用的观影信息!\n1.先看看最火的影片。\n2.找个影院去看电影。\n3.有优惠吗？\n4.很无聊不知道干什么。\n0.任何时候回复0，都将回到这里。'
        response_content = dict(content = content,touser = msg['FromUserName'],fromuser = msg['ToUserName'],createtime = str(int(time.time())))
        #userinfo_add(msg)
        #print to_unicode(text_reply).format(**response_content)
        return make_response(to_unicode(text_reply).format(**response_content))