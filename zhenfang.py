import random
import urllib
import urllib2
import cookielib
from BeautifulSoup import BeautifulSoup
 
_xh = '学号'
_pw = '密码'
login_url = 'http://网址/default3.aspx'
#课表的网址
timetable_url = 'http://网址/xskbcx.aspx?xh=%s'% _xh 
student_cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(student_cookie)) # Login
 
data = '__VIEWSTATE='+VIEWSTATE+'&TextBox1='+_xh+'&TextBox2='+_pw+'&ddl_js=%D1%A7%C9%FA&Button1=+%B5%C7+%C2%BC+'
login_request = urllib2.Request(login_url, data, {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Charset': 'UTF-8,*;q=0.5',
                    'User-Agent': USER_AGENT, 
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Connection': 'keep-alive',
                    'HOST': '网址',
                    'Origin':  'http://网址',
                    'Referer': 'http://网址/default3.aspx'})
opener.open(login_request, data)
 
html = opener.open(timetable_url).read()
