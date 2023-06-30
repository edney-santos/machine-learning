import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime


st.title('Top 10.000 TMDb movies data - exploratory analysis')


dataframe = pd.read_csv('./data/top_1000_popular_movies_tmdb.csv', lineterminator='\n', index_col=0)
dataframe.drop(['id', 'overview', 'tagline'], axis=1, inplace=True)
dataframe.dropna(axis=0, inplace=True)
dataframe['genres'] = dataframe['genres'].apply(eval)

if st.checkbox('Show raw dataframe'):
    st.write(dataframe)

st.divider()

st.subheader('Number of movies by language')
st.bar_chart(dataframe['original_language'].value_counts())



st.divider()




dataframe['release_date'] = pd.to_datetime(dataframe['release_date'])
release_year = dataframe['release_date'].dt.year

film_counts = release_year.value_counts().reset_index()
film_counts.columns = ['year', 'count']
film_counts = film_counts.loc[film_counts['year'] <= datetime.now().year]
film_counts = film_counts.sort_values('year', ascending=True)

st.subheader('Filmmaking through the years')
fig2 = px.line(film_counts, x='year', y='count')
st.plotly_chart(fig2)



st.divider()



all_genres = []

for genre_list in dataframe['genres']:
    all_genres.extend(genre_list)

unique_genres = sorted(list(set(all_genres)))

st.subheader('Top 10 popular movies by gender')
choice = st.selectbox('Choose a movie gender:', unique_genres, index=0)

df_exploded = dataframe.explode('genres')
filtered_movies = df_exploded.loc[df_exploded['genres'] == choice].sort_values('popularity', ascending=False)

# st.bar_chart(data=filtered_movies.head(10), x='title', y='popularity', use_container_width=True)

fig = px.bar(filtered_movies.head(10), x='title', y='popularity',)
st.plotly_chart(fig)
st.caption('Popularity score assigned to the movie by TMDB based on user engagement.')
