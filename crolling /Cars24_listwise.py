from requests import session
from bs4 import BeautifulSoup as BS
s = session()
s.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0'
url = 'https://www.cars24.com/buy-used-car?f=make%3A%3D%3Amaruti&sort=bestmatch&serveWarrantyCount=true&listingSource=Homepage_Filters&storeCityId=2'
r = s.get(url)
soup = BS (r.text,'html.parser')
Catogery_wise_data =[]
import pandas

def Cars24_list_links(list_links):
    r = s.get(list_links)
    soup = BS (r.text,'html.parser')
    for i in soup.find_all('a','_2kfVy'):
        all_links = i.get('href')
        # print(all_links)
        Cars24_product_page(all_links)


def Cars24_product_page(All_details):
    r = s.get(All_details)
    soup = BS (r.text,'html.parser')
    name = soup.find('div','_10kZS').text
    price = soup.find('strong','_2yYvS Wqfj6').text.replace('₹',' ₹')
    Emi_option = soup.find('div','_1hNEI').find('strong').text
    image = soup.find('div','_1eV4Q').find('img').get('src')
    item = dict()
    item ["Name"] = name
    item ['Price'] = price
    item ['Emi_Option'] = Emi_option
    item ['Image_links'] = image
    Catogery_wise_data.append(item)
    print(Catogery_wise_data)



Cars24_list_links('https://www.cars24.com/buy-used-car?f=make%3A%3D%3Amaruti&sort=bestmatch&serveWarrantyCount=true&listingSource=Homepage_Filters&storeCityId=2')

df = pandas.DataFrame(Catogery_wise_data)
df.to_excel('Cars24_list_&_product_data.xlsx')