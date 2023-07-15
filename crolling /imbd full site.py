from requests import session
from bs4 import BeautifulSoup as BS
s = session()
s.headers ['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0'
url = 'https://www.imdb.com/title/tt4154796/?ref_=nv_sr_srsg_0_tt_8_nm_0_q_avenge'
All_Data_list = []
r = s.get(url)
soup = BS (r.text,'html.parser')
import pandas

def single_cat(url):
    r = s.get(url)
    soup = BS (r.text,'html.parser')
    for i in soup.find_all('div','ipc-page-content-container ipc-page-content-container--center'):
        movie_name = i.find('div','sc-52d569c6-0 kNzJA-D')
        if movie_name:
            movie_name = movie_name.find('h1').text
            # print(movie)
        rating = i.find('div','sc-3a4309f8-1 kKSYln')
        if rating:
            rating = rating.text.replace('MYOUR RATINGRate','   ')
            # print(rating)
        year_time = i.find('ul','ipc-inline-list ipc-inline-list--show-dividers sc-afe43def-4 kdXikI baseAlt')
        if year_time:
            year_time = year_time.text.replace('UA',' Time:- ')
            # print(year_time)
        video = i.find('div','sc-385ac629-9 jiVoNU')
        if video:
            video = video.find('a','ipc-btn ipc-btn--single-padding ipc-btn--center-align-content ipc-btn--default-height ipc-btn--core-baseAlt ipc-btn--theme-baseAlt ipc-btn--on-onBase ipc-secondary-button sc-ceb22a5b-3 lltPEH').get('href').replace('/title','https://www.imdb.com/title')
            # print(video)
        top_rated = i.find('div','sc-fcdc3619-0 kKcbrZ base')
        if top_rated:
           top_rated = top_rated.text
        #    print(top_rated)
        image = i.find('div','ipc-title__wrapper')
        if image:
            image = image.find('a').get('href').replace('/title','https://www.imdb.com/title')
            # print(image)
    for top_cast in  soup('div','sc-bfec09a1-5 kUzsHJ'):
        cast = top_cast.find('a').get('href').replace('/name','https://www.imdb.com/name')
        # print(cast)
        item = dict()
        item ["Movie_Name"] = movie_name
        item ["Rating"] = rating
        item ["Release_year_timing"] = year_time
        item ["Video"] = video
        item ["Top_Rated_Award"] = top_rated
        item ["Top_Cast"] = cast
        All_Data_list.append(item)
        print(All_Data_list)
    





single_cat('https://www.imdb.com/title/tt4154796/?ref_=nv_sr_srsg_0_tt_8_nm_0_q_avenge')
            
df = pandas.DataFrame(All_Data_list)
df.to_excel('IMBd_Search_Data.xlsx')