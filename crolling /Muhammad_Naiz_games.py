from requests import session
from bs4 import BeautifulSoup as BS
s = session()
s.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0'
url = 'https://www.muhammadniaz.net/{}'
r = s.get(url)
soup = BS (r.text,'html.parser')
import pandas
all_links_mohd = []


def Mohd_Naiz_Main_Links (Main_links):
    r = s.get(Main_links)
    soup = BS (r.text,'html.parser')
    for i in soup.find_all('li'):
        all_links = i.find('a').get('href')
        if all_links and all_links.startswith('https://www.muhammadniaz.net/category'):
            # print('main=====',all_links)
            Mohd_Naiz_List_links(all_links,page=1)       


def Mohd_Naiz_List_links (List_links,page):
    r = s.get('{}page/{}'.format(List_links,page))
    # print(r.url)
    soup = BS (r.text,'html.parser')
    for i in soup.find_all('h2','post-box-title'):
        link = i.find('a').get('href')
        # print(link)
    # print(f"ListPage Url crawlerd {r.url}")
    item = dict()
    item ['all_links'] = link
    all_links_mohd.append(item)
    Mohammad_naiz_Product(link)


        # print(r.url)
    page+=1
    pagination = soup.find('div','pagination')
    
    if pagination:
        if int(pagination.find('span').text.split('of')[1].strip())>=page:
            Mohd_Naiz_List_links(List_links,page)
    else:
        pass

details1 = []
screen_shot = []
def Mohammad_naiz_Product (All_pro_details):
    r = s.get(All_pro_details)
    soup = BS (r.text,'html.parser')
    image = soup.find('img','aligncenter size-full wp-image-8303')
    if image:
        image = image.get('data-src')
    else:
        image = 'Not Given'

    name = soup.find('h1','name post-title entry-title')
    if name:
        name = name.text
    else:
        name = 'Not Given'

    comments = soup.find('span','post-comments')
    if comments:
        comments = comments.text
    else:
        comments = 'Not Given'

    views = soup.find('span','post-views')
    if views:
        views = views.text
    else:
        views = 'Not Given'

    for i in soup.find_all('p'):
            details = i.find('span')
            if details:
                details = details.text
                if details.startswith('Cyberpunk'):
                    details1.append(details)

    for i in soup.find_all('img'):
            ss = i.get('data-src')
            if ss and '/i.pinimg.com' in ss:
                screen_shot.append(ss)
    data = {
        'iamge' : image,
        'name' : name,
        'Comments' : comments,
        'views' : views,
        'Details' : details1,
        'Screen_shot' : screen_shot

        
    }
    print(r.url,data)
    

Mohd_Naiz_Main_Links('https://www.muhammadniaz.net/')

df = pandas.DataFrame(all_links_mohd)
df.to_excel('Mohd_Naiz_List_links.xlsx')