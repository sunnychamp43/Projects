from requests import session
import pandas
from bs4 import BeautifulSoup as BS

s = session()
s.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0'
All_data_list = []

def Product_details(url):
    r = s.get(url)
    soup = BS (r.text,'html.parser')
    # image = soup.find('img','aligncenter size-full wp-image-8303')
    # if image:
    #     image = image.get('data-src')
    # else:
    #     image = 'Not Given'
    Image1 = []
    details1 = []
    screen_shot = []
    for i in soup.find_all('p'):
        
        image = i.find('img')
        if image:
            image = image.get('data-src')
            if 'Cover' in image:
                Image1.append(image)
                

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
                if 'Windows' in details:
                    details1.append(details)

    for i in soup.find_all('img'):
            ss = i.get('data-src')
            if ss and '/i.pinimg.com' in ss:
                screen_shot.append(ss)
    data = {
        'iamge' : Image1,
        'name' : name,
        'Comments' : comments,
        'views' : views,
        'Details' : details1,
        'Screen_shot' : screen_shot

        
    }
    All_data_list.append(data)
    print(url)
df = pandas.read_excel('Mohd_Naiz_List_links.xlsx')
for count in range(len(df)):
     url = df.iloc[count]['all_links']
     Product_details(url)
df = pandas.DataFrame(All_data_list)
df.to_excel('Mohd_Naiz_All_Product_data.xlsx')



    