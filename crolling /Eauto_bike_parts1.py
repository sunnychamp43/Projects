from requests import session
from bs4 import BeautifulSoup as BS
s = session()
s.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0'
url = 'https://eauto.co.in/'
base_url = 'https://eauto.co.in{}'
r = s.get(url)
import pandas
list_1 = []
Main_links = []
List_links1 = []
list_2 =[]



def Main_cat_links (url1):
    r = s.get(url1)
    soup = BS (r.text,'html.parser')
    for i in soup.find_all('li','nav-bar__item')[:3]:
        all_links = 'https://eauto.co.in'+i.find('a','nav-bar__link link').get('href')
        # print(all_links)
        Cat_list(all_links)
        # Main_links.append(all_links)

def Cat_list(url2):
    r = s.get(url2)
    # print('Main---------------',r.url)
    soup = BS (r.text,'html.parser')
    # next = [ _next.get('href')  for _next in soup.find('div','quick-links').find_all('a','quick-links__link')]
    for i in soup.find('div','collection-list__section').find_all('a'):
        all = 'https://eauto.co.in'+i.get('href')
        # print(all)
        # List_link(all)
        List_links1.append(all)
        # print(all)


def List_link (url3):
    

    flag = True
    while flag:


        r = s.get(url3)
        # print('list-------------------',r.url)
        soup = BS (r.text,'html.parser')
        product = soup.find_all('a','product-item__title text--strong link')
        if product:
            for i in product:
                list_links = 'https://eauto.co.in/'+i.get('href')
            item = dict()
            item ['Pagination'] = list_links
            list_2.append(item)
            print(r.url)
                 

        Next = [_next for _next in soup.find_all('a','pagination__next link') if 'Next' in _next]
        if Next:
            next_1 = base_url.format(Next[0].get('href'))  
            # item = dict()
            # item ['Pagination_links'] = next_1
            # list_1.append(item)
            
            url3 = next_1
        else:
            flag = False

# def Pro_page(url4):
#     r = s.get(url4)
#     soup = BS (r.text,'html.parser')   
    image = soup.find('div','product-gallery__carousel-wrapper').find('img').get('data-src')  
    name = soup.find('h1','product-meta__title heading h1').text
    price = soup.find('span','price price--highlight').text.strip()
    reviews = soup.find('span','jdgm-prev-badge__text').text
    des = soup.find('h4').text.strip()
    for tr in soup.find('tbody').findAll("tr"):
        if len(tr.findAll("td")) == 2:
            key = tr.findAll("td")[0]
            value = tr.findAll("td")[1]
            print("{} : {}".format(key.text.strip(),value.text.strip()))
    for i in soup.find_all('ul')[47:48]:
        spec = i.text.strip()
        

    # print(next)        


Main_cat_links(url)
for links in List_links1:
    List_link(links)


df = pandas.DataFrame(list_2)  
df. to_excel('Eauto_Pagination_links.xlsx')