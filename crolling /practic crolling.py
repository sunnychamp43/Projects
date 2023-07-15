from requests import session
from bs4 import BeautifulSoup as BS
import pandas

list3= []
list1 = []
link2 = []
s = session ()
s.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0'
url = 'http://yellowpages.in/'
r = s.get(url)
soup = BS(r.text,"html.parser")



for i in soup.find_all('a','eachHomeCategory'):
    b = i.get('href')
    item = dict()
    item ['all link'] = 'http://yellowpages.in/'+b
    link2.append(item)


for i in link2:
    
    c = i.get('all link')
    r = s.get(c)
    soup = BS(r.text,'html.parser')
    product = soup.find_all('div','eachPopular')

    for j in product:

        name = j.find('a','eachPopularTitle').text
        block = j.find('div',"eachPopularRatingBlock").text
        contact = j.find('a','businessContact').text
        timing = j.find('div','openNow').text
        location = j.find('address','businessArea').text
        item = dict()
        item ['category url'] = c
        item ['title'] = name
        item ['review'] = block
        item ['contact'] = contact
        item ['time'] = timing
        item ['location'] = location
        list3.append(item)

print(list3)

df = pandas.DataFrame(list3)
df.to_excel("yellow pages catogery.xlsx")

