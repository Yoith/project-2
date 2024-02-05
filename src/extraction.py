import requests
import pandas as pd
from bs4 import BeautifulSoup

def extract_votes(url):
        
        response = requests.get(url)
        xml_data = response.text
        soup = BeautifulSoup(xml_data, "xml")
    
        game_name = soup.find("name", {"primary": "true", "sortindex": "1"}).text

        poll_section = soup.find("poll")
    
        top_ten_votes = []

   
        for poll_result in poll_section.find_all("results"):
        
            numplayers = poll_result.get("numplayers", "")
        
        
            for result in poll_result.find_all("result"):
            
                value = result.get("value", "")
                numvotes = result.get("numvotes", "")
            
            
            top_ten_votes.append({
                "game_name": game_name, 
                "num_players": numplayers,
                "value": value,
                "num_votes": numvotes
            })

   
        df_2 = pd.DataFrame(top_ten_votes)
    
        return df_2