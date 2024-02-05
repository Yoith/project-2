import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("data/bgg_modified.csv")

df_2 = pd.read_csv("data/top_ten_modified.csv")

def barplot_year (df):

    filtered_data = df[(df['year'] >= 1995) & (df['year'] <= 2020)]

    sns.set(style="whitegrid")

    sns.histplot(filtered_data['year'], kde=True, bins=25, color="teal")

    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.title('Distribution of Game Release Years')

    release_distribution = "release_years.png"
    plt.savefig(f"images/{release_distribution}")
    plt.close()



def barplot_type(df):
    type_counts = df['type'].value_counts()

    type_counts.plot(kind='pie', autopct='%1.1f%%', colors=["teal", "darkred", "darkorange", "gold",  "lightskyblue"], textprops={'color': 'black'})

    plt.title('Distribution of Game Types')

    type_distribution = "type_distribution.png"
    plt.savefig(f"images/{type_distribution}")
    plt.close()


def barplot_age(df):
    custom_colors = ["teal", "darkred", "darkorange", "gold", "lightskyblue"]

    average_minage_by_type = df.groupby('type')['minage'].mean().reset_index()

    sns.barplot(x='type', y='minage', data=average_minage_by_type, palette=custom_colors)

    plt.xlabel('Type of Game')
    plt.ylabel('Average Minimum Age')
    plt.title('Average Minimum Age by Game Type')

    plt.xticks(rotation=25)

    age_type = "age_type.png"
    plt.savefig(f"images/{age_type}", bbox_inches = 'tight')


def barplot_rating(df):

    def reducing_names (df):
        df['name'] = df.apply(lambda row: row['name'].split(':')[0] if row['name'] != 'Brass: Birmingham' else row['name'], axis=1)

    reducing_names(df)    

    custom_colors = ["cyan", "teal", "darkmagenta", "darkred", "tan", "darkorange", "darkgoldenrod", "gold", "lightskyblue", "palegreen"]

    top_ten_games = df.sort_values(by='rank').head(10)

    sns.barplot(x='name', y='rating', data=top_ten_games, palette=custom_colors)

    plt.xlabel('Name of the game')
    plt.ylabel('Rating')
    plt.title('Top Ten Games by rating')

    plt.xticks(rotation=25, ha='right')

    top_rating = "top_rating.png"
    plt.savefig(f"images/{top_rating}", bbox_inches = 'tight')
    plt.close()



def barplot_total_votes(df_2):
    custom_colors = ["cyan", "teal", "darkmagenta", "darkred", "tan", "darkorange", "darkgoldenrod", "gold", "lightskyblue", "palegreen"]

    total_votes = df_2.groupby('game_name')['num_votes'].sum().sort_values(ascending=False)


    sns.barplot(x=total_votes.index, y=total_votes.values, palette=custom_colors)

    plt.xlabel('Game')
    plt.ylabel('Total Votes')
    plt.title('Top 10 Games by Total Votes')

    plt.xticks(rotation=25, ha='right')

    top_votes = "top_votes.png"
    plt.savefig(f"images/{top_votes}", bbox_inches = 'tight')
    plt.close()


def barplot_oneplayer(df_2):

    one_best = df_2[(df_2['num_players'] == '1') & (df_2['value'] == 'Best')].copy()

    total_votes_one = one_best.groupby('game_name')['num_votes'].agg('sum').reset_index()

    total_votes_one['num_votes'] = total_votes_one['num_votes'].astype(int)

    total_votes_one = total_votes_one.sort_values(by='num_votes', ascending=False)

    custom_colors = ["cyan", "teal", "darkmagenta", "darkred", "tan", "darkorange", "darkgoldenrod", "gold", "lightskyblue", "palegreen"]

    sns.barplot(x=total_votes_one['game_name'], y=total_votes_one['num_votes'], palette=custom_colors)

    plt.xlabel('Game Name')
    plt.ylabel('Total Votes')
    plt.title('Best Game for 1 Player')

    plt.xticks(rotation=25, ha='right')

    one_player = "one_player.png"
    plt.savefig(f"images/{one_player}", bbox_inches = 'tight')
    plt.close()



def barplot_twoplayer(df_2):
    
    two_best = df_2[(df_2['num_players'] == '2') & (df_2['value'] == 'Best')].copy()

    total_votes_two = two_best.groupby('game_name')['num_votes'].agg('sum').reset_index()

    total_votes_two['num_votes'] = total_votes_two['num_votes'].astype(int)

    total_votes_two = total_votes_two.sort_values(by='num_votes', ascending=False)

    custom_colors = ["cyan", "teal", "darkmagenta", "darkred", "tan", "darkorange", "darkgoldenrod", "gold", "lightskyblue", "palegreen"]

    sns.barplot(x=total_votes_two['game_name'], y=total_votes_two['num_votes'], palette=custom_colors)

    plt.xlabel('Game Name')
    plt.ylabel('Total Votes')
    plt.title('Best Game for 2 Players')

    plt.xticks(rotation=25, ha='right')

    two_players = "two_players.png"
    plt.savefig(f"images/{two_players}", bbox_inches = 'tight')


def barplot_threeplayer(df_2):

    three_best = df_2[(df_2['num_players'] == '3') & (df_2['value'] == 'Best')].copy()

    total_votes_three = three_best.groupby('game_name')['num_votes'].agg('sum').reset_index()

    total_votes_three['num_votes'] = total_votes_three['num_votes'].astype(int)

    total_votes_three = total_votes_three.sort_values(by='num_votes', ascending=False)

    custom_colors = ["cyan", "teal", "darkmagenta", "darkred", "tan", "darkorange", "darkgoldenrod", "gold", "lightskyblue", "palegreen"]

    sns.barplot(x=total_votes_three['game_name'], y=total_votes_three['num_votes'], palette=custom_colors)

    plt.xlabel('Game Name')
    plt.ylabel('Total Votes')
    plt.title('Best Game for 3 Players')

    plt.xticks(rotation=25, ha='right')

    three_players = "three_players.png"
    plt.savefig(f"images/{three_players}", bbox_inches = 'tight')
    plt.close()



def barplot_fourplayer(df_2):

    four_best = df_2[(df_2['num_players'] == '4+') & (df_2['value'] == 'Best')].copy()

    four_best = four_best.groupby('game_name')['num_votes'].agg('sum').reset_index()

    four_best['num_votes'] = four_best['num_votes'].astype(int)

    four_best = four_best.sort_values(by='num_votes', ascending=False)

    custom_colors = ["cyan", "teal", "darkmagenta", "darkred", "tan", "darkorange", "darkgoldenrod", "gold", "lightskyblue", "palegreen"]

    sns.barplot(x=four_best['game_name'], y=four_best['num_votes'], palette=custom_colors)

    plt.xlabel('Game Name')
    plt.ylabel('Total Votes')
    plt.title('Best Game for 4 or more Players')

    plt.xticks(rotation=25, ha='right')

    four_players = "four_players.png"
    plt.savefig(f"images/{four_players}", bbox_inches = 'tight')
    plt.close()
