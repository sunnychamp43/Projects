from requests import session
from bs4 import BeautifulSoup as BS
s = session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Authorization': 'Basic cDFob3NwaXRhbGl0eTpzZWNyZXQ=',
    'Connection': 'keep-alive',
    # 'Cookie': 'XSRF-TOKEN=eyJpdiI6IlZTS3FwUTFqS3FvZTNqTjdQZFFCREE9PSIsInZhbHVlIjoib1VTbzI1dWcwd2pUNnRFVUJ0NTZzVHBtV0t2Nm5GUENiU2FYQ01wanZjbUVFeDBIczREaGZGUnV6TC9MeEhmWkw4K2FqTitrc3FEWVJCV1Q4OWcxenJjVC9nNnpRSmZnRXRweUlUaXRjSjVRK0JuK2NyTm14VnNOQ1l6ajhxN3IiLCJtYWMiOiIxNDUzYzJlMzUyNDk4OGFiY2U0MWI2NWRkMGFhN2FiNTk1NjBiMDAxOWNlZTk5YTVjYTI2YjM4Zjc1YzI5Mzg0IiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6Imc3dTY4eXM5QkVRVU9jbzFId1Z4Z0E9PSIsInZhbHVlIjoiaXM4NEpuSWFERHVoWWxEbXFYOXpmRGlpN0lBMC9Wb2YzTEpoOUJZUWFnd200Z1dlZEZKbE1HcHd6cTA0UG1WbVdydnI5OWh1aEphSUp1OUUzSTIwSTFjNWp3eTVTaDRmZ3IxWjNxaXlCZVF3SVUxbWx4R0hLdGdZSmJCZW42c1oiLCJtYWMiOiJmYWZjYzcwNTZkNTBiMjBhODg1ZmYyZWFiZjM1YjdjNzMwYzg5MWM2ODYzZTVkOTQ4ZTU1MTNkMmJmMGE4YWQ3IiwidGFnIjoiIn0%3D',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
}
s.headers.update(headers)
url = 'https://b2b.travelflow.com/p1-corporate-hospitality?page=2'
r = s.get(url)
soup = BS (r.text,'html.parser')




def B2b(url):

    for i in soup.find_all('td','p-0'):
        league_name = i.find('span').text.split(',')[0]    
        league_name1 = i.find('span').text.split(',')[1]
        league_date= i.find('span').text.split(',')[2]
        orgnizer = i.find('small').text.split('-')[0]
        orgnizer1 = i.find('small').text.split('-')[2]
        # print(league_name)


    # for i in soup.find_all('h5'):
    #     b = i.text
    #     print(b)


    price=[]
    for i in soup.find_all('tr')[1:]:
        league_name = i.find_all('td')
        if len(league_name) ==1:
            price.append({'price':""})
        else:
            price.append({'price':league_name[1].text.strip()})
        print

    # price_with_hotel=[]
    # for i in soup.find_all('tr')[1:]:
    #     league_name = i.find_all('td')
    #     if len(league_name) ==1:
    #         price_with_hotel.append({'price_with_hotel':""})
    #     else:
    #         price_with_hotel.append({'price_with_hotel':league_name[2].text.strip()})

    # ticket_stock =[]
    # for i in soup.find_all('tr')[1:]:
    # league_name = i.find_all('td')
    #     if len(league_name) ==1:
    #         ticket_stock.append({'price_with_hotel':""})
    #     else:
    #         ticket_stock.append({'price_with_hotel':league_name[3].text.strip()})


B2b (url)