from requests import session
from bs4 import BeautifulSoup as BS
l =[]
import pandas


s = session()
s.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0'
url = 'https://www.fastenersuperstore.com'
r = s.get(url)
soup = BS (r.text,'html.parser')

link2 = []
list3 =[]
for i in soup.find_all('a'):
    

    b =i.get('href')
    if b and b.startswith('/category'):
        if b not in l:
            l.append(b)        
            item = dict()
            item ['all links'] = 'https://www.fastenersuperstore.com/'+b
            # print(item)
            link2.append(item)
            
            
# print(link2)
for j in link2:
    c = j.get('all links')
    r = s.get(c)
    soup = BS (r.text,'html.parser')
    product = soup.find_all('li')
    


    for num in product:
        
        # name = num.find('p')
        # print(name)
        if num.find('h2'):
            name = (num.find('h2').text)
        if num.find('p'):
            feat = (num.find('p').text)
        if num.find('span'):
            img = num.find('img').get('src')
            print(img)
            
            item = dict()
            item ['name'] = name
            item ['feature'] = feat
            item ['image'] = img
            list3.append(item)
            print(item)


df = pandas.DataFrame(list3)
df.to_excel('fastner super store.xlsx')        # img = i.find('img')














# for i in soup.find_all('a'):
#     ...:     name = i.find('h2')
#     ...:     img = i.find('img')



#     for i in soup.find_all('p','hidden-xs'):
#     ...:     hide = i.text
#     ...:     print(hide)