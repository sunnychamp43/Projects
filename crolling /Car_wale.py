from requests import session
from bs4 import BeautifulSoup as BS
s = session()
s.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0'
url = 'https://www.carwale.com/'
r = s.get(url)
soup = BS (r.text,'html.parser')
# list1 =[]
All_Data_List = []
import pandas



def Carwale_Catogery_page (Catogery_links):
    r = s.get(Catogery_links)
    soup = BS (r.text,'html.parser')
    for i in soup.find_all('a','o-cKuOoN o-frwuxB'):
        all_links = 'https://www.carwale.com'+i.get('href')
        # print('Main----',all_links)
        Carwale_list_page(all_links)


def Carwale_list_page (List_links):
    r = s.get(List_links)
    # print('Main______',r.url)
    soup = BS (r.text,'html.parser')
    for i in soup.find_all('li','o-fzptUA'):
        List_links = 'https://www.carwale.com'+i.find('a').get('href')
        # print(List_links)
        Carwale_Product_page(List_links)


def Carwale_Product_page (Product_Data):
    r = s.get(Product_Data)
    soup = BS (r.text,'html.parser')
    image = soup.find('div','o-bqHweY o-bfyaNx o-brXWGL OW5DVf o-dgboEW')
    if image:
        image = image.find('img').get('src')
    else:
        image = 'Not Given'

    name = soup.find('h1','o-dOKno o-bNCMFw o-eqqVmt')
    if name:
        name = name.text
    else:
        name = 'Not Given'

    model = soup.find('div','o-efHQCX o-bTDyCI o-fDnrXc o-buzfYq o-cpnuEd')
    if model:
        model = model.text.replace('Version','Version:- ')
    else:
        model = 'Not Given'
    
    review = soup.find('a','o-eemiLE o-eqqVmt o-fznJEv ZD2kKf')
    if review:
        review = review.text
    else:
        review = 'Not Given'

    price = soup.find('span','o-Hyyko o-bPYcRG o-eqqVmt')
    if price:
        price = price.text
    else:
        price = 'Not Given'
    # Cars_details = soup.find('tbody')
    # if Cars_details is not soup.find('tbody'):
    list1=[]
    for i in soup.find_all('tr'):
    
        if i.find('span'):
            cars_details = i.text
            if not cars_details.startswith('Jimny') and not cars_details.startswith('1.0/51'):
                cars_details = cars_details
                list1.append(cars_details)
    item = dict()
    item ['Image_links'] = image
    item ['Name'] = name
    item ['MOdel'] = model
    item ['Review'] = review
    item ['Price'] = price
    item ['Cars_Details'] = list1
    All_Data_List.append(item)
    print    



Carwale_Catogery_page('https://www.carwale.com/')


# for cars in list1:
#     Carwale_Catogery_page(cars)

df = pandas.DataFrame(All_Data_List)
df.to_excel('Carwale_single_page_catogery_data.xlsx')