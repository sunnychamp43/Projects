from requests import session
from bs4 import BeautifulSoup as BS
import pandas

list1= []

list2 = ['http://yellowpages.in/hyderabad/apparels-and-accessories/110497301','http://yellowpages.in/hyderabad/food-and-beverages/606286653','http://yellowpages.in/hyderabad/beauty-and-wellness/256159214']
s = session ()
s.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0'

url = 'http://yellowpages.in/hyderabad/printing-and-stationaries/655042489'
r = s.get (url)
soup = BS (r.text,'html.parser')
for i in soup.find_all('div','eachPopular'):
    
    name = i.find('a','eachPopularTitle').text
    block = i.find('div',"eachPopularRatingBlock").text
    contact = i.find('a','businessContact').text
    timing = i.find('div','openNow').text
    location = i.find('address','businessArea').text
    item = dict()
    item ['title'] = name
    item ['review'] = block
    item ['contact'] = contact
    item ['time'] = timing
    item ['location'] = location
    list1.append(item)

print(list1)

df = pandas.DataFrame(list1)
df.to_excel('yellow.xlsx')



df = pandas.DataFrame(list1)
df.to_excel("")