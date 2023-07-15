from requests import session
from bs4 import BeautifulSoup as BS
s = session()
s.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firef112.0'
url = 'https://www.lenovo.com/in/en/dg/LAPTOPS?from=splitter&visibleDatas=facet_Type%3AUltra-Slim&sort=sortBy&resultsLayoutType=grid'
r = s.get(url)
soup = BS(r.text,'html.parser')
all_data = []
import pandas

def Lenovo_list_page(url):
    r =s.get(url)
    soup = BS (r.text,'html.parser')
    for i in soup.find_all('a','py-0 px-6 font-weight-bold custom-tertiary v-btn v-btn--outlined theme--light v-size--default'):
        all_links = i.get('href')
        # print(all_links)
        Lenovo_pro(all_links)

def Lenovo_pro (url2):
    r = s.get(url2)
    soup = BS (r.text,'html.parser')

    name = soup.find('h1','desktopHeader')
    if name:
        name = name.text
    else:
        name = 'Not given'

    image =soup.find('img','subSeries-Hero rollovercartItemImg')
    if image:
        image = image.get('src')
    else:
        image = 'Not given'

    price = soup.find('div','cta-group-price')
    if price:
        price = price.find('dd').text
    else:
        price = 'Not given'

    details = soup.find('div','hero-productDescription-body mediaGallery-productDescription-body')
    if details:
        details = details.text.strip()
    else:
        details = 'Not given'
    list1=[]
    for i in soup.find_all('div', attrs = {'id':'configuratorItem-mtmTable-text'}):
        des = i.find('h4').text
        des1 = i.find('p','configuratorItem-mtmTable-description').text.strip()
        list1.append({des : des1})
    # print(list1)
    item = dict()
    item ['Name'] = name
    item ['image'] = image
    item ['price'] = price
    item ["Details"] = details
    item ['Description'] = list1
    all_data.append(item)
    print(all_data)


    
    
        

        
        
Lenovo_list_page(url)

df = pandas.DataFrame(all_data)
df.to_excel('Lenovo_Cat.xlsx')