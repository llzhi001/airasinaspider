# coding:utf-8

"""
create by swm
2018/03/01
"""

from requests_html import HTML
session = HTML()

r = session.get('https://booking.airasia.com/Flight/Select?s=False&o1=SZX&d1=KUL&ADT=1&dd1=2018-03-20&mon=true')
print r.html.links