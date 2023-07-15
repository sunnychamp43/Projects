from requests import session
from bs4 import BeautifulSoup as BS
import pandas
s = session()
base_url = "https://www.flipkart.com{}"
# s.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Connection': 'keep-alive',
    # 'Cookie': 'T=TI168034711254900084835350402184779422108750594280716550725480484567; SN=VI5F58CDF278204DD1AB66274100C0A237.TOK5A29297B98C54EAC96C34EDEB5302BF3.1684845712.LO; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE2ODYyMjU0NDQsImlhdCI6MTY4NDQ5NzQ0NCwiaXNzIjoia2V2bGFyIiwianRpIjoiZjk5N2E3ZDktMWUyMC00YjlhLTg0MDYtMWM0N2U2Y2I2Y2ZiIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNjgwMzQ3MTEyNTQ5MDAwODQ4MzUzNTA0MDIxODQ3Nzk0MjIxMDg3NTA1OTQyODA3MTY1NTA3MjU0ODA0ODQ1NjciLCJrZXZJZCI6IlZJNUY1OENERjI3ODIwNEREMUFCNjYyNzQxMDBDMEEyMzciLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.BHq6Q9UknyN0cQ4WBVk0fir14UI0MV38Gt67SNnpMls; K-ACTION=null; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19500%7CMCMID%7C83154438782733891881313486868899911162%7CMCAID%7CNONE%7CMCOPTOUT-1684771318s%7CNONE%7CMCAAMLH-1685102244%7C12%7CMCAAMB-1685368918%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI; _pxvid=13e3b30a-d07d-11ed-aac2-53b2d410adf0; __pxvid=1446bdac-d07d-11ed-8c50-0242ac120003; S=d1t14bT8/P2U/Pz9fd1hxMz8/P4E0LbspY6tRzVUQkonBWjl2z8rekalRerU0+lpmxUnIBec16Ama+exq/XwAsOEk/g==; qH=2a8df1e39ffa9e71; pxcts=ad4e69c2-f959-11ed-8228-4d6758475657; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Awomens-footwear%25253Aflats%25253Apr%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Fwomens-footwear%25252Fflats%25252Fpr%25253Fsid%25253Dosp%2525252Ciko%2525252C9d5%252526otracker%25253Dnmenu_sub_Women_0_Fla%2526ot%253DA; _px3=2427a31abeaf5d4cc559e53f9593e5ae5389acce2f99b47c4634a01bfdc799b1:4rB29IssL+RLrRru6td+uEJ+88R3bOeNC/lGbzivHY5v3QTFYK9goUrYag+J91+iKKxsUl0HrhjRl9PiEK+JiA==:1000:vq5PQdxduJ1BtEvVUkTydNBgCgeWbMzYm9suseJNlztcPV3ZvgvesZbI83YhLqr5FASPck/R3TZrUIhz+VDkbXHmup6t45hhyvl7EnhhFRT3/35M9BxisCxfh0CF49BbXm4gdzjbwcBG1x0E4LjElo/nO6+ZU3AEhcSBr0s/KCMrvd0i+KPijN8EJ7TWzHG03+nM25mNOu5lxUj4fzubeg==',
}
s.headers.update(headers)
url = 'https://www.flipkart.com/womens-footwear/flats/pr?sid=osp,iko,9d5&otracker=nmenu_sub_Women_0_Flats'

l2 = []

def crawling_list_page(url):
    r = s.get(url)
    soup = BS (r.text,'html.parser')

    for i in soup.find_all('div','_1xHGtK _373qXS'):
        image = i.find('img').get('src')
        name = i.find('div','_2WkVRV').text
        details = i.find('a','IRpwTa').get('title')
        size =  i.find('div').find('span','_376u-U')
        if i.find('div','_3Ay6Sb').find('span'):
            discount = (i.find('div','_3Ay6Sb').find('span').text)
        else:
            discount = (" ")
        
        if i.find('div','_30jeq3'):
            price = (i.find('div','_30jeq3').text)
        else:
            price = (" ")


        item = dict()
        item ['iamge'] = image
        item ['name'] = name
        item ['details'] = details
        item ['price'] = price
        item ['discount'] = discount
        l2.append(item)
        print(item)

    next_page = soup.find("nav","yFHi8N")
    if next_page:
        next_page = [page_ for page_ in next_page.find_all("a") if "next" in page_.text.strip().lower()]
        next_url = base_url.format(next_page[0].get("href"))
        print("Calling Next page")
        print(next_url)
        crawling_list_page(next_url)


crawling_list_page(url)
df = pandas.DataFrame(l2)
df. to_excel('flipkart men.xlsx')
