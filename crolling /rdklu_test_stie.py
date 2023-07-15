from requests import session
from bs4 import BeautifulSoup as BS
s = session()
import pandas
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.rdklu.com/',
    'Alt-Used': 'www.rdklu.com',
    'Connection': 'keep-alive',
    # 'Cookie': 'keep_alive=226bb41b-e414-4d9f-8c1f-9fd3420243b3; secure_customer_sig=; localization=IN; _cmp_a=%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22merchant_geo%22%3A%22IN%22%2C%22sale_of_data_region%22%3Afalse%7D; _y=e9814777-78b5-430a-b9da-c5c05825f7a7; _s=7ea453ac-09ab-47d9-8c7f-9dea40730cc3; _shopify_y=e9814777-78b5-430a-b9da-c5c05825f7a7; _shopify_s=7ea453ac-09ab-47d9-8c7f-9dea40730cc3; _orig_referrer=https%3A%2F%2Fwww.google.com%2F; _landing_page=%2F; _shopify_sa_t=2023-07-13T11%3A49%3A06.729Z; _shopify_sa_p=; optiMonkClientId=52dbdf30-5757-8946-37af-cc5d1108519e; ex_id=FQKOXwsCso; OT_FBPLID=fb.1.1689248947143.1689249034561; _gcl_au=1.1.1188094964.1689248947; _ga_4BGZP0YD4S=GS1.1.1689248947.1.1.1689249256.0.0.0; _ga=GA1.2.803469147.1689248948; _gid=GA1.2.2002134461.1689248949; optiMonkSession=1689248950; distinct_id=7448_1689248951086_4981; cbox_new_visitor={%22status%22:true%2C%22created_at%22:1689248951212}; cbox_first_page_popup_was_closed=1; cbox_second_page_popup_was_closed=0; cbox_condition_popup_status=1; bk_cart={%22t%22:%22fake_cart_token_7448_1689248951073_3928%22%2C%22s%22:[]%2C%22a%22:[]%2C%22i%22:[]}; optiMonkEmbedded119228=N4IgFghgzgMglgWzgFwEoFMIGMzoCYgBcAZhADZToC+QA===; optiMonkClient=N4IgjGCcBM0BwgFygMYEMmgMyZGlALkgAwA0eADhUmAGxwwAskUk5KATkiLY8XNGIBWACYiAptBHpixaFiyi4QnOQB2AexE1yBAM7c9ACw0B3cdvIHEIY2YsgAvo/IAzAG416TBkOjkAG09EOgZoRl9/EE0KYLBnIA==; _fbp=fb.1.1689249048131.1555792904; _scid=03ba46ac-15cb-48b3-bc09-3c303584123c; _scid_r=03ba46ac-15cb-48b3-bc09-3c303584123c; _scsrid=; _scsrid_r=; po_visitor=_x6JyAnwBtH9; _sctr=1%7C1689186600000',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}
base_url = 'https://www.rdklu.com{}'
s.headers.update(headers)

url = 'https://www.rdklu.com/'

Main_list = []
Cat_list = []
List_list = []

pro_des_1 = []

All_data_list =[]

r = s.get(url)
soup = BS (r.text,'html.parser')


def Main_cat (url1):
    r = s.get(url1)
    soup = BS (r.text,'html.parser')
    for i in soup.find('ul','mobile-nav mobile-nav--heading-style').find_all('div','mobile-nav__has-sublist'):
        links = i.find('a').get('href')
        if links.startswith('/c'):


            print('main----------------------------------------------',links)
            Main_list.append(links)
            # List_page(links)





def List_page (url3):
    if 'https://' not in url3:
        url = 'https://www.rdklu.com{}'.format(url3)
    else:
        url = url3
    r = s.get(url)
    print(r.url)
    soup = BS (r.text,'html.parser')
    for i in soup.find_all('a','grid-product__link'):
        list_pro_links = 'https://www.rdklu.com'+i.get('href')
        List_list.append(list_pro_links)
        
    next = soup.find('span','next')
    if next:
        next_1 = base_url.format(next.find('a').get('href'))
        List_page(next_1)
    else:
        1




def Pro_page (url4):
    r = s.get(url4)
    soup = BS (r.text,'html.parser')

    name = soup.find('h1','h2 product-single__title')
    if name:
        name = name.text.strip()
    else:
        name ='Not given'
    
    image = soup.find('img','photoswipe__image image-element')
    if image:
        image = image.get('src')
    else:
        image = 'Not given'

    price = soup.find('span','product__price on-sale')
    if price:
        price = price.text.strip()
    else:
        price = 'Not given'

    for i in soup.find('div','rte').find_all('li'):
        pro_des = i.text
        pro_des_1.append(pro_des)

    data = {
        'Image' : image,
        'Name' : name,
        'Price' : price,
        'Product_description' : pro_des_1
    }
    All_data_list.append(data)
    # print(r.url)
    


Main_cat(url)

for Main in Main_list:
    List_page(Main)

for Catogery in List_list:
    Pro_page(Catogery)


df = pandas.DataFrame(All_data_list)
df.to_excel('RDKLU_ALL_DATA.xlsx')
