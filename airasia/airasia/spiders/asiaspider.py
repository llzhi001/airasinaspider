# coding:utf-8

"""
create by swm
2018/03/01
"""

from scrapy import Spider
from scrapy import Request
from scrapy.utils.python import to_native_str
from six.moves.urllib.parse import urljoin

class AASP(Spider):
    name = "airasiaspider"
    host = "https://www.airasia.com"
    # meta = {
    #     "dont_redirect": True, "handle_httpstatus_list": [302]
    # }
    handle_httpstatus_list = [301, 302]
    def start_requests(self):
        url = 'https://booking.airasia.com/Flight/Select?o1=SZX&d1=KUL&culture=zh-CN&dd1=2018-03-01&dd2=2018-03-01&r=true&ADT=1&s=true&mon=true&cc=CNY&c=false'
        yield Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status >=300 and response.status < 400:
            location = to_native_str(response.headers['location'].decode('latin1'))
            request = response.request
            redirected_url = urljoin(request.url, location)
            if response.status in (301, 307) or request.method == 'HEAD':
                redirected = request.replace(url=redirected_url)
                yield redirected
            else:
                redirected = request.replace(url=redirected_url, method='GET', body='')
                redirected.headers.pop('Content-Type', None)
                redirected.headers.pop('Content-Length', None)
                yield redirected
        print response.body
        # yield Request(url=infohtml, headers=response.headers, meta=self.meta, callback=self.getres)

    def getres(self, response):
        print response.body
