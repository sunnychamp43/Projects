from requests import session
from bs4 import BeautifulSoup as BS
s = session()
s.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0'
url = 'https://www.soft32.com/'
base_url = 'https://www.soft32.com{}'
import pandas

# list1 = []
list3 = []
list2= []

def Main_cat (url1):
    r = s.get(url1)
    soup = BS (r.text,'html.parser')
    for i in soup.find('div',attrs = {'id':'navigation'}).find_all('a'):
        all_links=i.get('href')
        if 'rss/' not in all_links and 'navigation' not in all_links:
            # print(a ll_links)

        # print(all_links)
            list2.append(all_links)


def List_link (url2):
    
    flag = True
    while flag:
        r = s.get(url2)
        soup = BS (r.text,'html.parser')
        
        for i in soup.find_all('a','soft'):
            list1 = []
            list_links = i.get('href')
            if list_links not in list1:

                item = dict()
                item ['List_links'] = list_links
                list1.append(list_links)
                list3.append(list1)
                
                
                
                
            


                



        next = [_next.find('a') for _next in soup.find_all('li','next') if 'Next' in _next.text.strip()]
        # print(next)
        # print(next)
        
        if next:

            next_1 = base_url.format(next[0].get('href'))
            item = dict()
            item ['All_links'] = next_1
            list1.append(item)
            # print('List--------------------',r.url)        
            url2 = next_1

        else:
            # print("Nothing")
            flag = False


# def Pro_page(url3):
#     r = s.get(url)
#     soup = BS (r.text,'html.parser')
#     name = soup.find('h1','title').text.strip()
#     description = soup.find('strong',{'id':'short_description'}).text.strip()
#     for i in soup.find('div',{'id':'specifications'}).find_all('span'):
#         spec = i.text.strip()
#         print(spec)
#     rating = soup.find('span','next').text.strip()
#     screen_shot = soup.find('div',{'id':'screenshots'}).find('a').find('img').get('src')
#     image = soup.find('span','icon windows').find('img').get('src')

        
        


    


Main_cat(url)


for Links in list2:
    List_link(Links)

df = pandas.DataFrame(list3)
df.to_excel('Soft32_All_List_links.xlsx',index= False)
