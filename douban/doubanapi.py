# -*- coding: utf-8 -*-
import requests

from lxml import etree

class DoubanMovie():
    SEARCH_RUL = u"https://movie.douban.com/subject_search?search_text=%s"

    def __init__(self):
        pass
    def searchMovie(self,key):
        r = requests.get(self.SEARCH_RUL%key)
        if r.status_code == 200:
            tree = etree.HTML(r.text)
            search_nodes = tree.xpath('//div[@class="article"]/div/table')
            if len(search_nodes) > 0:
                for item in search_nodes:
                    nodes =  item.xpath('tr/td[1]/a')
                    for node in nodes:
                        name =  u''.join(node.xpath('img/@alt'))
                        if name.find(key) >= 0:
                            return { 'name': name,
                                     'url' :  u''.join(node.xpath('@href'))
                                    }
                pass
            else:
                print "=======> no result"
                return {}

        else:
            print "=====> status_code is not 200"
            return {}


d = DoubanMovie()

print d.searchMovie(u'战地报道')
