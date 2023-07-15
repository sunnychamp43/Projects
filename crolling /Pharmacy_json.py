

from requests import session
import json
s = session()
import pandas
# from bs4 import BeautifulSoup as BS
s.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0'


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'Origin': 'https://in.sugarcosmetics.com',
    'Connection': 'keep-alive',
    'Referer': 'https://in.sugarcosmetics.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

s.headers.update(headers)

url = "https://pharmeasy.in/api/otc/getCategoryProducts?categoryId=11315&page={}"

r = s.get(url)

js = r.json()

all_data_list = []


def prodcut_page (url1):
    flag = True
    page = 1
    while flag:
        r = s.get(url.format(page))
        js = r.json()
        if js.get("data").get("products"):
            count = (js["data"]["products"].__len__())
            print('---------------------------------',count)
            for prod in js["data"]["products"]:
                name = prod.get('name')
                image = prod.get('images')
                price = prod.get('salePriceDecimal')
                # print(name)
            data = {
                'Name' : name,
                "Images" : image,
                "Price" : price,

            }
            all_data_list.append(data)
            print(all_data_list)
            

                # print(image)
        else:
            flag = False
        page+=1
        


        # print(image)


prodcut_page(url)

df = pandas.DataFrame(all_data_list)
df.to_excel('Pharmacy_cat_page.xlsx')

