from requests import session
from bs4 import BeautifulSoup as BS
s = session()
import pandas
l=[]

l2 = []
s.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0'
url = 'https://www.yellowpages.ca/'
base_url = 'https://www.yellowpages.ca{}'
r = s.get(url)
soup = BS (r.text,'html.parser')

def main_links(url1):
    r = s.get(url1)
    soup = BS (r.text,'html.parser')
    for i in soup.find_all('a','jsQuickLinks'):
        all_links = 'https://www.yellowpages.ca'+i.get('href')
        print(all_links)
        list_links(all_links)


def list_links(url2):
    r = s.get(url2)
    soup = BS (r.text,'html.parser')
    # for i in soup.find_all('a','listing__name--link listing__link jsListingName'):
    #     all_links_1 = i.get('href')

        

    
    
    next = [_next for _next in soup.find_all('a','ypbtn btn-theme pageButton') if 'Next' in _next.text.strip()]
    
    # if next:
    #     next_url = base_url.format(next[0].get('href'))
    #     print(next_url)
    #     list_links(next_url)
    print(next)

# def product_page (url3):
#     r = s.get(url3)
#     soup = BS (r.text,'html.parser')


df = pandas.DataFrame(l2)
df.to_excel('yellow canada.xlsx')


    
    

main_links(url)
# for i in soup.find_all('a','jsQuickLinks'):
#     links =i.get('href')
#     item = dict()
#     item["all links"] = "https://www.yellowpages.ca/"+links
#     l.append(item)
#     # print(item)

# for j in l:
#     c = j.get ("all links")
#     r = s.get(c)
#     soup = BS (r.text,'html.parser')
#     product = soup.find_all('div','listing__content__wrap--flexed jsGoToMp')


        
            
#         # else:
#         #     l.append(" ")
            
    





    
