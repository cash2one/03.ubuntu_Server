# -*- coding: utf-8 -*-

import os
import time

import oss2


# 以下代码展示了视频直播相关接口的用法。


# 首先初始化AccessKeyId、AccessKeySecret、Endpoint等信息。
# 通过环境变量获取，或者把诸如“<您的AccessKeyId>”替换成真实的AccessKeyId等。
#
# 以杭州区域为例，Endpoint是：
#   http://oss-cn-shenzhen.aliyuncs.com 或
#   https://oss-cn-shenzhen.aliyuncs.com
access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', 'LTAI4oPl28gTR8pH')
access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', 'dg3FXdjjn94p4BMKRbTpO6ryaNfrBn')
bucket_name = os.getenv('OSS_TEST_BUCKET', 'live-move')
endpoint = os.getenv('OSS_TEST_ENDPOINT', 'http://oss-cn-shanghai.aliyuncs.com')


# 确认上面的参数都填写正确了
for param in (access_key_id, access_key_secret, bucket_name, endpoint):
    assert '<' not in param, '请设置参数：' + param


# 创建Bucket对象，所有直播相关的接口都可以通过Bucket对象来进行
bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)


# 创建一个直播频道。
# 频道的名称是test_rtmp_live。直播生成的m3u8文件叫做test.m3u8，该索引文件包含3片ts文件，每片ts文件的时长为5秒（这只是一个建议值，具体的时长取决于关键帧）。
channel_name = 'test_rtmp_live'
playlist_name = 'test.m3u8'
create_result = bucket.create_live_channel(
        channel_name,
        oss2.models.LiveChannelInfo(
            status = 'enabled',
            description = '测试使用的直播频道',
            target = oss2.models.LiveChannelInfoTarget(
                playlist_name = playlist_name,
                frag_count = 3,
                frag_duration = 5)))

# 创建直播频道之后拿到推流用的play_url（rtmp推流的url，如果Bucket不是公共读写权限那么还需要带上签名，见下文示例）和观流用的publish_url（推流产生的m3u8文件的url）。
publish_url = create_result.publish_url
play_url = create_result.play_url

print publish_url
print play_url

# 创建好直播频道之后调用get_live_channel可以得到频道相关的信息。
get_result = bucket.get_live_channel(channel_name)
print(get_result.description)
print(get_result.status)
print(get_result.target.type)
print(get_result.target.frag_count)
print(get_result.target.frag_duration)
print(get_result.target.playlist_name)