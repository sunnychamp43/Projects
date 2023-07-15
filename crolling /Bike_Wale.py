from requests import session
from bs4 import BeautifulSoup as BS

s = session()
s.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firef112.0'
url = 'https://www.bikewale.com/'
r = s.get(url)
soup = BS (r.text,'html.parser')


def Bike_wale_Main_links (Main_links):
    r = s.get(Main_links)
    soup = BS (r.text,'html.parser')
    all_links =['https://www.bikewale.com/'+i.find('a').get('href') for i in soup.find('div', attrs={'id':'brand-type-container'}).find_all('li')]
    # print(all_links)
    # Bike_Wale_List_links(all_links)
    return all_links

def Bike_Wale_List_links (cat_url):
    r = s.get(cat_url)

    # print(r.url)
    soup = BS (r.text,'html.parser')
    for i in soup.find_all('a','modelurl'):
        all_links = 'https://www.bikewale.com'+i.get('href')
        # print(all_links)

        Bike_wale_pro (all_links)

def Bike_wale_pro (Pro_det):
    r = s.get(Pro_det)
    print(r.url)
    soup = BS(r.text,'html.parser')
    star = soup.find('div','inline-block')
    if star:
        star = star.find('span').text
    else:
        star = 'Not Given'
    # print(star)

    image = soup.find('img','bw-ga')
    if image:
        image = image.get('src')
    else:
        image = 'not given'
    print(image)

    


cat_urls = Bike_wale_Main_links('https://www.bikewale.com/')

for cat_url in cat_urls:
    Bike_Wale_List_links(cat_url)