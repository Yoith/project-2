import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import os
import sys
from src.extraction import extract_votes

# Cleaning Data Frame

# Deleting columns and renaming
    
def clean_dataframe(df, columns_to_erase=[], rename=True):
    if rename:
        df.columns = [i.lower().replace(" ", "_").strip() for i in df.columns]

    df.dropna(thresh=2, inplace=True)
    df.drop(columns=columns_to_erase, inplace=True, errors="ignore")

    return df


# Unifying values
def unify_values(df):
    df.loc[df['type'].str.contains('Strategy', case=False), 'type'] = 'Strategy'
    df.loc[df['type'].str.contains('Thematic', case=False), 'type'] = 'Thematic'
    df.loc[df['type'].str.contains('Family', case=False), 'type'] = 'Family'
    df['rating'] = df['rating'].round(1)   
    df['bestplayers'] = df['bestplayers'].str.split(',').str[0]
    df['bestplayers'] = df['bestplayers'].replace(['4','5', '6'], '4+')

    df.to_csv('data/bgg_modified.csv', index=False)

    return df



def url_to_votes (urls):

    all_votes = pd.DataFrame()

    for url in urls:
        time.sleep(2)
        df = extract_votes(url)
        all_votes_df = pd.concat([all_votes, df], ignore_index=True)

    all_votes_df.to_csv('data/top_ten_votes.csv', index=False)

    top_ten = pd.read_csv("data/top_ten_votes.csv")
    
    if 'Unnamed: 0' in df.columns:
        top_ten.drop(columns=['Unnamed: 0'], inplace=True)

    return top_ten

def reducing_names (top_ten):
    top_ten['game_name'] = top_ten.apply(lambda row: row['game_name'].split(':')[0] if row['game_name'] != 'Brass: Birmingham' else row['game_name'], axis=1)
    # in this case I'm applying a lambda that will split the name after the colon and taking the first part
    # if it's distinct to the value "Brass: Birmingham", if not, it will mantain the same name
    top_ten['num_players'] = top_ten['num_players'].replace(['4','5', '6'], '4+')
    top_ten.to_csv('data/top_ten_modified.csv', index=False)



