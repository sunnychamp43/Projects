from requests import session

from bs4 import BeautifulSoup as BS

s = session()
s.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0'
All_data_list = []
import pandas


def Product_details(url1):

    r = s.get(url1)
    soup = BS (r.text,'html.parser')
    image = soup.find('div','product-gallery__carousel-wrapper')  
    if image:
        image = image.find('img').get('data-src')
    else:
        image = 'Not given'


    name = soup.find('h1','product-meta__title heading h1')
    if name:
        name = name.text
    else:
        name = 'Not given'


    price = soup.find('span','price price--highlight')
    if price:
        price = price.text.strip()
    else:
        price = 'Not given'


    reviews = soup.find('span','jdgm-prev-badge__text')
    if reviews:
        reviews = reviews.text
    else:
        reviews = 'Not given'


    des = soup.find('h4')
    if des:
        des = des.text.strip()
    else:
        des = 'Not given'


    for tr in soup.find('tbody').findAll("tr"):
        if len(tr.findAll("td")) == 2:
            key = tr.findAll("td")[0]
            value = tr.findAll("td")[1]
            Main = ("{} : {}".format(key.text.strip(),value.text.strip()))

            
    for i in soup.find_all('ul')[47:48]:
        spec = i.text.strip()
        

    data  = {
        'Image' : image,
        'Title' : name,
        'Price' : price,
        'Reviews' : reviews,
        'Description' : des,
        'Product_Info' : Main,
        'Special_Info' : spec,
         
    }

    All_data_list.append(data)
    print(url1)
df = pandas.read_excel ('Eauto_Pagination_links.xlsx')
for count in range (len(df)):
    url1 = df.iloc[count] ['Pagination']
    Product_details(url1)
df = pandas.DataFrame(All_data_list)
df.to_excel ('Eauto_Product_all_Data.xlsx')

        

    



