# Top 250 movies rating 
# movie name rank, release date and IMBD rating
from bs4 import BeautifulSoup as  bs
import pandas as pd
import requests

movie_link=requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250').text

soup=bs(movie_link,'html.parser')

data=soup.find('tbody',class_="lister-list").find_all('tr')

name=[]
rank=[]
year=[]
rating=[]
for movie in data:
    name.append(movie.find('td',class_='titleColumn').a.text.strip())
    rank.append(movie.find('td',class_='titleColumn').get_text(strip=True).split('.')[0])
    year.append(movie.find('td',class_='titleColumn').span.text.strip('()'))
    rating.append(movie.find('td',class_='ratingColumn').strong.text)
    
data_set={"Rank":rank,"Movie Name":name,"Realease Date":year,"IMDB Ratings":rating}
df=pd.DataFrame(data_set)

   
  
    
    
