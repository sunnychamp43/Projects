from requests import session
from bs4 import BeautifulSoup as BS
s = session()
s.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firef112.0'
url = 'https://www.myntra.com/'
r = s.get(url)
soup = BS (r.text,'html.parser')

def Catogery_page (url1):
    r = s.get(url1)
    soup = BS (r.text,'html.parser')
    for i in soup.find_all('a','desktop-categoryName'):
         all_links ='https://www.myntra.com'+i.get('href')

def List_page(url2):
    r = s.get(url)
    soup = BS (r.text,'html.parser')
    
         


Catogery_page(url)