from requests import session
from bs4 import BeautifulSoup as BS
s = session()
s.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0'
url = 'https://www.flipkart.com/'
r = s.get(url)
soup = BS (r.text,'html.parser')


for i in soup.find_all('div','eFQ30H'):
    b = i.find('a').get('href')
    if b:
        print(b)