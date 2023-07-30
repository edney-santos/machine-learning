import pandas as pd

def get_dataframe(profit: bool):
    dataframe = pd.read_csv('./data/top_1000_popular_movies_tmdb.csv', lineterminator='\n', index_col=0)
    dataframe.drop(['id', 'overview', 'tagline'], axis=1, inplace=True)
    dataframe.dropna(axis=0, inplace=True)
    dataframe['genres'] = dataframe['genres'].apply(eval)
    
    if (profit):
        movies_profit = dataframe.drop(dataframe[(dataframe['budget'] == 0) & (dataframe['revenue'] == 0)].index)
        movies_profit['profit'] = movies_profit['revenue'] - movies_profit['budget']
        return movies_profit
    
    return dataframe