import pandas as pd 
import src.cleaning as clean
import src.extraction as ext
import src.visualization as viz
import time

# 1. Cleaning: Kaggle

df = pd.read_csv("data/BGG100.csv", encoding = 'ISO-8859-1')

df_2 = pd.read_csv("data/top_ten_votes.csv")

columns_to_drop = ["subtitle", "weight"]

df = clean.clean_dataframe(df, columns_to_drop, rename=True)
df = clean.unify_values(df)

# 2. Extracting: web-scrapping

urls = ["https://api.geekdo.com/xmlapi/boardgame/174430/",
    "https://api.geekdo.com/xmlapi/boardgame/161936/",
    "https://api.geekdo.com/xmlapi/boardgame/224517/",
    "https://api.geekdo.com/xmlapi/boardgame/167791/",
    "https://api.geekdo.com/xmlapi/boardgame/233078/",
    "https://api.geekdo.com/xmlapi/boardgame/291457/",
    "https://api.geekdo.com/xmlapi/boardgame/220308/",
    "https://api.geekdo.com/xmlapi/boardgame/187645/",
    "https://api.geekdo.com/xmlapi/boardgame/182028/",
    "https://api.geekdo.com/xmlapi/boardgame/115746/"]

#ext.extract_votes(urls)

df_2 = clean.url_to_votes (urls)

# 3. Visualizing

viz.barplot_year(df)
viz.barplot_type(df)
viz.barplot_age(df)
viz.barplot_rating(df)

viz.barplot_total_votes(df_2)
viz.barplot_oneplayer(df_2)

viz.barplot_twoplayer(df_2)
viz.barplot_threeplayer(df_2)
viz.barplot_fourplayer(df_2)