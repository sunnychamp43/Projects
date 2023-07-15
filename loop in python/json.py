
import requests
from requests import Session
s = Session()



cookies = {
    'HAB_Var': 'Apothecary',
    'HAB_XDI': 'Apothecary',
    '_cg': '4000',
    'X-Default-City': '1',
    'X-Pincode': '400001',
    '_gcl_aw': 'GCL.1687777665.Cj0KCQjw7uSkBhDGARIsAMCZNJvWQVkdReinBuMDtOzUqJO2f1PkQX4rfF8E1Oe_cap7NMIb5LUWbNEaAsf4EALw_wcB',
    '_gcl_au': '1.1.1478635864.1687776679',
    'dtm_token_sc': 'AAANOFcdiH6qYAB96OhaAAAAAAE',
    'XdI': '01cf2ae1689a67cb3e1468a7c9f89684',
    '_ga': 'GA1.2.1431142586.1687776679',
    '_gac_UA-60621013-1': '1.1687777665.Cj0KCQjw7uSkBhDGARIsAMCZNJvWQVkdReinBuMDtOzUqJO2f1PkQX4rfF8E1Oe_cap7NMIb5LUWbNEaAsf4EALw_wcB',
    '_ga_J4XE9SW84F': 'GS1.1.1688466934.8.1.1688466955.39.0.0',
    'WZRK_G': '164abb7ad51447cbb2fe807d91e0dfc7',
    'dtm_token': 'AQEMOVYciX-rYQF86elbAQBBbQE',
    'XPESD': '%7B%22session_id%22%3A%22s_w_01cf2ae1689a67cb3e1468a7c9f89684_1688466931000%22%2C%22session_id_flag%22%3A%22ct_id%22%2C%22referrer%22%3A%22%22%2C%22session_start_time%22%3A%222023-07-04T10%3A35%3A31.975Z%22%7D',
    '_fbp': 'fb.1.1687777669966.1023294151',
    '_gid': 'GA1.2.244134911.1688387427',
    'XPESS_v2': 's_w_01cf2ae1689a67cb3e1468a7c9f89684_1688466931000',
    'WZRK_S_R9Z-WWR-854Z': '%7B%22p%22%3A3%2C%22s%22%3A1688466934%2C%22t%22%3A1688466956%7D',
    '_gat_UA-60621013-1': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-INSTANA-T': '922564c2333bed6f',
    'X-INSTANA-S': '922564c2333bed6f',
    'X-INSTANA-L': '1,correlationType=web;correlationId=922564c2333bed6f',
    'Connection': 'keep-alive',
    'Referer': 'https://pharmeasy.in/health-care/top-products-9297',
    # 'Cookie': 'HAB_Var=Apothecary; HAB_XDI=Apothecary; _cg=4000; X-Default-City=1; X-Pincode=400001; _gcl_aw=GCL.1687777665.Cj0KCQjw7uSkBhDGARIsAMCZNJvWQVkdReinBuMDtOzUqJO2f1PkQX4rfF8E1Oe_cap7NMIb5LUWbNEaAsf4EALw_wcB; _gcl_au=1.1.1478635864.1687776679; dtm_token_sc=AAANOFcdiH6qYAB96OhaAAAAAAE; XdI=01cf2ae1689a67cb3e1468a7c9f89684; _ga=GA1.2.1431142586.1687776679; _gac_UA-60621013-1=1.1687777665.Cj0KCQjw7uSkBhDGARIsAMCZNJvWQVkdReinBuMDtOzUqJO2f1PkQX4rfF8E1Oe_cap7NMIb5LUWbNEaAsf4EALw_wcB; _ga_J4XE9SW84F=GS1.1.1688466934.8.1.1688466955.39.0.0; WZRK_G=164abb7ad51447cbb2fe807d91e0dfc7; dtm_token=AQEMOVYciX-rYQF86elbAQBBbQE; XPESD=%7B%22session_id%22%3A%22s_w_01cf2ae1689a67cb3e1468a7c9f89684_1688466931000%22%2C%22session_id_flag%22%3A%22ct_id%22%2C%22referrer%22%3A%22%22%2C%22session_start_time%22%3A%222023-07-04T10%3A35%3A31.975Z%22%7D; _fbp=fb.1.1687777669966.1023294151; _gid=GA1.2.244134911.1688387427; XPESS_v2=s_w_01cf2ae1689a67cb3e1468a7c9f89684_1688466931000; WZRK_S_R9Z-WWR-854Z=%7B%22p%22%3A3%2C%22s%22%3A1688466934%2C%22t%22%3A1688466956%7D; _gat_UA-60621013-1=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'categoryId': '9297',
    'page': '2',
}

response = requests.get('https://pharmeasy.in/api/otc/getCategoryProducts', params=params,cookies=cookies,headers=headers)
s.headers.update(headers)

url = 'https://ph8armeasy.in/api/otc/getCategoryProducts?categoryId=11315&page='
js = response.json()
js['data']['products']
print(js)


