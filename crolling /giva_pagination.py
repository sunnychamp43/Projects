from requests import session
from bs4 import BeautifulSoup as BS
s = session()
# s.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Alt-Used': 'www.giva.co',
    'Connection': 'keep-alive',
    # 'Cookie': 'secure_customer_sig=; localization=IN; _cmp_a=%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22merchant_geo%22%3A%22IN%22%2C%22sale_of_data_region%22%3Afalse%7D; _y=49ed54e0-a91e-4cb9-9960-5ce73fd2531b; _shopify_y=49ed54e0-a91e-4cb9-9960-5ce73fd2531b; _orig_referrer=https%3A%2F%2Fwww.google.com%2F; _landing_page=%2F%3Fpsafe_param%3D1%26gclid%3DCjwKCAjwsvujBhAXEiwA_UXnAHTtTzyyKOVrz9hZcGzCN43asXmNWi_PHuibtTDeq1g8NNeDTmdYFhoC67MQAvD_BwE; swym-session-id="w9p5judjetqmrmily02gr63vw158tq077yv42ln74y20n1d6xs0azw0qq1tzlvp2"; __stp=eyJ2aXNpdCI6InJldHVybmluZyIsInV1aWQiOiI2N2U3MzZiNC0xNWY4LTQ0MGQtODZhYi00MGE3NTlmM2Y5YzUifQ==; __stgeo=IjAi; __stbpnenable=MA==; _hsu=hs.1686051140084.b0e733fe76; _hscl=; bxSesC=MTY4NjA1MTE0MDE3Mg%3D%3D; bxSegDetail=eyJieFNlc1QiOjE2ODYwNTExNDAxNzIsInVzZXJUeXBlIjoicmV0dXJuaW5nIiwidXNlclJhbmRvbSI6MC41NzM3NjM1MDE2OTQ4OTIxLCJwcnZNdiI6IjYiLCJwdWJNdiI6IjYiLCJleHBJZCI6IjY0NzliY2Y0ZjExNDRmNDdiNWU1OTZlNyIsInVzZXJTZWciOiJfZGVmYXVsdCIsIm1vZGVsU2VnIjoiNl9fZGVmYXVsdCJ9; boxx_token_id=NjdlNzM2YjQtMTVmOC00NDBkLTg2YWItNDBhNzU5ZjNmOWM1; deduplication_cookie=google; deduplication_cookie=google; _gcl_aw=GCL.1686051185.CjwKCAjwsvujBhAXEiwA_UXnAHTtTzyyKOVrz9hZcGzCN43asXmNWi_PHuibtTDeq1g8NNeDTmdYFhoC67MQAvD_BwE; _gcl_au=1.1.1586050687.1686051141; trackingId3=lik7bew3j6n9181e18; visitId3=lik7bew36d6fpifp8ou; last_referrer3=www.google.com; last_utm_campaign3=null; last_params3=psafe_param%3D1%26gclid%3DCjwKCAjwsvujBhAXEiwA_UXnAHTtTzyyKOVrz9hZcGzCN43asXmNWi_PHuibtTDeq1g8NNeDTmdYFhoC67MQAvD_BwE; uniquePVEvent=true; swym-pid="ww6VoVDv1y3rHsp9RKpg7dkHxh+vDHrWI01W1cZ1on4="; _ga_34LM183QM4=GS1.1.1686060345.2.1.1686061486.39.0.0; _ga=GA1.1.982371759.1686051142; _gid=GA1.2.1531961099.1686051142; _gac_UA-146125996-1=1.1686051185.CjwKCAjwsvujBhAXEiwA_UXnAHTtTzyyKOVrz9hZcGzCN43asXmNWi_PHuibtTDeq1g8NNeDTmdYFhoC67MQAvD_BwE; _cnt_first_visit_time=1686051142.434; _cnt_last_visit_time=1686051142.434; _cnt_current_visit_time=1686051142.434; _cnt_num_of_vists=1; _cnt_event_user_id=6wrd4h6t62h97f2yllvw; _cnt_geo_country=India; _cnt_forms_status=%7B%2218718%22%3A%5B%22cnt_ab%22%2C1686051171%5D%7D; _cnt_cart_json=%7B%7D; _ttgclid=CjwKCAjwsvujBhAXEiwA_UXnAHTtTzyyKOVrz9hZcGzCN43asXmNWi_PHuibtTDeq1g8NNeDTmdYFhoC67MQAvD_BwE; _ttgclid=CjwKCAjwsvujBhAXEiwA_UXnAHTtTzyyKOVrz9hZcGzCN43asXmNWi_PHuibtTDeq1g8NNeDTmdYFhoC67MQAvD_BwE; _ttgclid=CjwKCAjwsvujBhAXEiwA_UXnAHTtTzyyKOVrz9hZcGzCN43asXmNWi_PHuibtTDeq1g8NNeDTmdYFhoC67MQAvD_BwE; FPGCLAW=GCL.1686051185.CjwKCAjwsvujBhAXEiwA_UXnAHTtTzyyKOVrz9hZcGzCN43asXmNWi_PHuibtTDeq1g8NNeDTmdYFhoC67MQAvD_BwE; FPAU=1.1.1586050687.1686051141; WIGZO_DAILYACTIVE=Active; WIGZO_LEARNER_ID=366230c2-1642-4d93-a235-882e4b7cbb9a; __stdf=MA==; PAGE_UUID=366230c2-1642-4d93-a235-882e4b7cbb9a; swym-swymRegid="EefLhWM1t03WVS5mAt8kEM87wGbgI7bnQAzpFf2-WRjxsVNAk5jsZEAS5x9HlFxS8vON4QVnXn8ma6gLUFCVJyraK85PgNtkqscv_mHFPqGoLgPV13FE8gY4z0-qNq0ELDk2tNKEM1NWsmz_Xj1aQvemGJFDfDxsj3-7Ic5WVlo"; swym-email=null; ln_or=eyIzMTg5MjYwIjoiZCJ9; _ga_F1NJ1E2HJ2=GS1.1.1686060348.2.1.1686061485.0.0.0; _clck=1hfymb4|2|fc8|0|1252; _fbp=fb.1.1686051147185.754630996; swym-cu_ct=undefined; swym-instrumentMap={}; _scid=67b48826-549f-495d-8bc2-a37b53af0d26; _cnt_discount_code_119833=_true; _sctr=1%7C1685989800000; cjConsent=MHxOfDB8Tnww; cjUser=2d9e9b85-4bd3-4ca3-807b-10dcc93292c9; uniqueVCEvent=true; bxSesT=MTY4NjA1OTE2ODM5NA%3D%3D; keep_alive=feefb635-13ad-4abe-8ebe-1fc6a339a2e2; _s=2fa3e0a3-6d1c-4da4-840a-d9e70d5bb5ac; _shopify_s=2fa3e0a3-6d1c-4da4-840a-d9e70d5bb5ac; _clsk=5h1vcj|1686061479369|7|1|u.clarity.ms/collect; __sts=eyJzaWQiOjE2ODYwNjAzNDU0OTgsInR4IjoxNjg2MDYxNDgwODkzLCJ1cmwiOiJodHRwcyUzQSUyRiUyRnd3dy5naXZhLmNvJTJGJTJGY29sbGVjdGlvbnMlMkYxOGstZ29sZC1wbGF0ZWQtamV3ZWxsZXJ5JTNGcGFnZSUzRDIiLCJwZXQiOjE2ODYwNjE0ODA4OTMsInNldCI6MTY4NjA2MDM0NTQ5OCwicFVybCI6Imh0dHBzJTNBJTJGJTJGd3d3LmdpdmEuY28lMkYlMkZjb2xsZWN0aW9ucyUyRjE4ay1nb2xkLXBsYXRlZC1qZXdlbGxlcnkiLCJwUGV0IjoxNjg2MDYwNjI5MDEwLCJwVHgiOjE2ODYwNjA2MjkwMTB9; _shopify_sa_t=2023-06-06T14%3A24%3A46.666Z; _shopify_sa_p=; swym-o_s=true; _gat_UA-146125996-1=1; _scid_r=67b48826-549f-495d-8bc2-a37b53af0d26; _uetsid=d1b08fc0045d11eeac2233ee77705069; _uetvid=d1b0cc20045d11eeac467d5e576d4aaa',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}
s.headers.update(headers)
url = 'https://www.giva.co/collections/earrings?page={}'

r = s.get(url)
soup = BS (r.text,'html.parser')

def Pagination (url2,page):
    r = s.get(url2.format(page))
    soup = BS (r.text,'html.parser')
    page+=1
    


Pagination(url,page=1)
