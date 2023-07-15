from requests import session
from bs4 import BeautifulSoup as BS
s = session()
s.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0'
url = 'https://www.rottentomatoes.com/browse/movies_in_theaters/'
r = s.get(url)
soup = BS (r.text,'html.parser')


def Catogery_list_links(list_links,page):
    r = s.get('{}?page={}'.format(list_links,page))
    print(r.url)
    soup = BS (r.text,'html.parser')


    page+=1
    Catogery_list_links(url,page)

Catogery_list_links(url,page=1)
