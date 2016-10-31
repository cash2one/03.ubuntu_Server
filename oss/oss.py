# -*- coding: utf-8 -*-
import oss2
import os, sys

class OssSDK():
    def __init__(self):
        pass

    def init(self):
        self.endpoint = "http://oss-cn-shanghai.aliyuncs.com"
        self.auth = oss2.Auth('LTAI4oPl28gTR8pH', 'dg3FXdjjn94p4BMKRbTpO6ryaNfrBn')
        self.bucket = oss2.Bucket(self.auth, self.endpoint, 'x2020')

    def test(self):

        #self.put('1.mp4','1.mp4')
        print(self.bucket.sign_url('GET', 'RadioInterfaceTBox.pb.cc', 60))
        for object_info in oss2.ObjectIterator(self.bucket):
            print(object_info.key)
        result = self.bucket.get_object('RadioInterfaceTBox.pb.cc')
        print dir(result)

    def percentage(consumed_bytes, total_bytes):
        if total_bytes:
            rate = int(100 * (float(consumed_bytes) / float(total_bytes)))
            print '\r{0}% '.format(rate)
            sys.stdout.flush()

    def put(self,remotefile,localfile,callback=percentage):
        return self.bucket.put_object_from_file(remotefile,localfile,progress_callback=callback)