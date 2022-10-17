from bs4 import BeautifulSoup
import requests
import pandas as pd

list = []

for season in range(5):
    season_number = season + 1
    
    s_url = f'https://www.imdb.com/title/tt6468322/episodes?season={season_number}'
    print(f"Season link : {s_url}")
    response = requests.get(s_url)
    soup = BeautifulSoup(response.content)
    title = soup.find_all('div', class_ = 'info')
    
    for episode_no, episode in enumerate(title):
        episode_name = episode.strong.a.text
        episode_no = episode_no + 1
        
        airdate = episode.find('div', class_ = 'airdate')
        airdates = airdate.text.strip().replace('.', '')
        
        description = episode.find('div', class_ = 'item_description').get_text().strip().replace(',', '') 
        
        rating = episode.find('span', class_ = 'ipl-rating-star__rating').get_text()
        
        vote = episode.find('span', class_ = 'ipl-rating-star__total-votes').get_text()
        
        data = {"Season":season_number,
                "Episode":episode_no,
                "Title":episode_name,
                "Airdate":airdates,
                "Description":description,
                "Rating":rating,
                "Votes":vote,}
        
        list.append(data)
        
df = pd.DataFrame(list, columns = ['Season', 'Episode', 'Title', 'Airdate', 'Rating', 'Votes', 'Description'])
df.to_csv('money_heist.csv', index=False)