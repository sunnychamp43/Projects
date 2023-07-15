from requests import session
from bs4 import BeautifulSoup as BS
s = session()
s.headers ['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0'
url = 'https://www.homethangs.com/bathroom-320.html{}'
r = s.get(url)
soup = BS (r.text,'html.parser')
list1 = []
import pandas





def crawl_all_category (url):
    r=s.get(url)
    soup=BS(r.text,'html.parser')
    for i in soup.find_all('div','category-list'):
        sub='https://www.homethangs.com/'+i.find('a').get('href')
        # print('main-----',sub)
        sub_catogery_(sub)
    



def sub_catogery_(url2):
    # print('main---',url2)
    r = s.get(url2)
    soup = BS (r.text,'html.parser')
    
    products = soup.find_all('table','categoryitem')
    if products:
        listpage_urls.append(url2)

    sub_catogery = soup.find_all('div','category-list')
    if sub_catogery:
        for i in sub_catogery:
            sub_main = 'https://www.homethangs.com/'+i.find('a').get('href')
            sub_catogery_(sub_main)
        
            # print('sub cat',sub_main)

    # sub2_catogery = soup.find_all('div','category-list')
    # if sub2_catogery:
    #     for j in sub2_catogery:
    #         sub2_main = 'https://www.homethangs.com/'+j.find('a').get('href')

    #         sub_catogery_(sub2_main)
        


def listpage(url3,page):
    # print(url3)

    
    r = s.get("{}&page={}".format(url3,page))
    print(r.url)
    soup = BS (r.text,'html.parser')
    product2 = soup.find_all('table','categoryitem')
    for j in product2:
        name = j.find('td','cat-item-name')
        
        if name:
            name = name.text
        else:
            name = "Not given"
        details = j.find('td','pother')

        if details:
            details = details.text
        else:
            details = "Not given"

        price = j.find('b').find('span')
        
        if price:
            price = price.text
        else:
            price= 'Not given'

        image = j.find('a').find('img').get('src')

        if image:
            image = image.strip()
        else:
            image = 'Not given'
        # page = j.find('div','hql-total-page')
        # if page:
        #     page = page.text
        # else:
        #     page = 'not given'
        # print(page)

        
        item = dict()
        item ['title'] = name
        item ['detials'] = details
        item ['price'] = price
        item ['image'] = image
        list1.append(item)
    # print(item)
    # next_page_url = "{}&page={}".format(url3,page)
    # for i in soup.find_all('div','hql-total-page'):
    #     page = i.text.strip()
    #     print(page)

    page+=1
    # print(r.url)
    # print(list1)
    if int(soup.find('div','hql-total-page').text.split(' 1 of ')[1])>=page:
        listpage(url3,page)

    
    # print(list1,page)

listpage_urls = []

crawl_all_category('https://www.homethangs.com/bathroom-320.html')
# urls = ["https://www.homethangs.com/soaking-bath-tubs-380.html","https://www.homethangs.com/victorian-bath-tubs-385.html","https://www.homethangs.com/walk-in-tubs-877.html"]

# print(listpage_urls)

for url in listpage_urls:
    listpage(url,page=1)
    print(listpage)
    

df = pandas.DataFrame(listpage_urls)
df.to_excel('home thangs.xlsx')
