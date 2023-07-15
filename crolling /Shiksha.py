from requests import session
from bs4 import BeautifulSoup as BS
s = session()
s.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firef112.0'
url = 'https://www.shiksha.com/'
r = s.get(url)
soup = BS(r.text,'html.parser')
All_pro_data = []
import pandas


def Shiksha_Cat_Page(url1):
    r = s.get(url1)
    soup = BS (r.text,'html.parser')
    next = ['https://www.shiksha.com/'+all.get('href') for all in soup.find_all('a', attrs = {'ea':'Top Ranked Colleges'}) if 'https:' not in all.get('href')]
    return next

def Shiksha_list_links(url2):
    r = s.get(url2)
    # print(r.url)
    soup = BS (r.text,'html.parser')
    for i in soup.find_all('div','tuple-inst-info'):
        list_links = 'https://www.shiksha.com'+i.find('a').get('href')
        Pro_page(list_links)

def Pro_page (url3):
    r = s.get(url3)
    soup = BS(r.text,'html.parser')
    image = soup.find('div','c55b78')
    if image:
        image = image.find('img').get('src')
    else:
        image = 'Not given'

    name = soup.find('h1','e70a13')
    if name:
        name = name.text
    else:
        name = 'Not given'
    
    location = soup.find('span','_7164e4 ece774 ece774')
    if location:
        location = location.text
    else:
        location = 'Not given'

    rating_review = soup.find('span','f05f57 ece774 ece774')
    if rating_review:
        rating_review = rating_review.text
    else:
        rating_review = 'Not given'

    comments = soup.find('a','dc3573')
    if comments:
        comments = comments.text
    else:
        comments = 'Not given'

    about_collage = soup.find('p',attrs = {'style':'text-align: justify;'})

    if about_collage:
        about_collage = about_collage.text
    else:
        about_collage = 'Not given'
    list1 = []
    for i in soup.find_all('span','efc38e ece774'):
        establish = i.text.split('Public/GovernmentUniversity')[0]
        list1.append(establish)
    data = { 
        'Image' : image,
        'Name' : name,
        'Location' : location,
        'Rating_Review' : rating_review,
        'Comments' : comments,
        'About_Collage' : about_collage,
        'Establish_date' : list1,


    }
    All_pro_data.append(data)

    print(r.url)


        

    





cat_url = Shiksha_Cat_Page ('https://www.shiksha.com/')
for cat_urls in cat_url:
    Shiksha_list_links(cat_urls)

df = pandas.DataFrame(All_pro_data)
df.to_excel('Shiksha.xlsx')

