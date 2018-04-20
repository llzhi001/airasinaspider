# coding:utf-8
"""
create by swm
2018/03/01
"""
import requests
from bs4 import BeautifulSoup
import re
import pymongo
import datetime
import random

class AAPAC:

    def get_header(self):
        headers = {
            "X-Forwarded-For": '%s.%s.%s.%s' % (
            random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
            'Host': "https://www.airasia.com",
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate'}
        return headers

    def getinfo(self, departure, destination, datetime):
        url = 'https://booking.airasia.com/Flight/Select?s=False&o1={}&d1={}&ADT=1&dd1={}&mon=true'.format(departure, destination, datetime)
        print url
        # htmlinfo = requests.get(url, headers=self.get_header())
        htmlinfo = requests.get(url)
        Soup = BeautifulSoup(htmlinfo.text, 'lxml')
        print Soup


if __name__ == '__main__':
    flight = [('DMK', 'HKT'), ('HKT', 'DMK'), ('HKT', 'CNX'), ('KUL', 'PEK'), ('BKI', 'TWU')]
    date = ['2018-03-07', '2018-03-08', '2018-03-09', '2018-03-10', '2018-03-11']
    testdata = ['SZX', 'KUL', '2018-03-20']
    aapac = AAPAC()
    res = aapac.getinfo(testdata[0], testdata[1], testdata[2])

