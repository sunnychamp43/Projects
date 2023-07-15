from requests import session
from bs4 import BeautifulSoup as BS
s = session()
main= []
import pandas

s.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0'
url = 'https://www.flipkart.com/search?q=i%20phone%20&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
r = s.get(url)
soup = BS (r.text,'html.parser')



for i in soup.find_all('a','_1fQZEK'):
    name = i.find('div','_4rR01T').text
    rate = i.find('div','_3LWZlK').text
    review = i.find('span','_2_R_DZ').text
    spec = i.find('ul','_1xgFaf').text
    price = i.find('div','_30jeq3 _1_WHN1').text
    image = i.find('div','CXW8mj').find('img').get('src')
    # rate.append(review)


    item = dict()
    item ['name'] = name
    item ['rate & rev'] = rate,review
    item ['spec'] = spec
    item ['price'] = price
    item ['image'] = image
    main.append(item)
print(main) 

df = pandas.DataFrame(main)
df.to_excel('flipkart.xlsx')