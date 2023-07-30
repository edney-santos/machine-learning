import pandas as pd
import streamlit as st


st.title('Data pre-processing')
st.subheader('Importing data')
st.markdown('We will start by importing our database using the pandas library with the read_csv function.')

code1 = '''dataframe = pd.read_csv(
    './data/top_1000_popular_movies_tmdb.csv',
    lineterminator='\\n',
    index_col=0
    )'''

st.code(code1, language='python')

dataframe = pd.read_csv('./data/top_1000_popular_movies_tmdb.csv', lineterminator='\n', index_col=0)

with st.expander('View raw dataframe'):
    st.write(dataframe)


st.divider()


st.subheader('Removing unused fields')
st.markdown('We will remove the _"id"_, _"overview"_ and _"tagline"_ fields that will not be useful for exploratory analysis')

code2 = '''dataframe.drop(['id', 'overview', 'tagline'], axis=1, inplace=True)'''

st.code(code2, language='python')

dataframe.drop(['id', 'overview', 'tagline'], axis=1, inplace=True)

with st.expander('View resulting dataframe'):
    st.write(dataframe)


st.divider()


st.subheader('Removing records with null fields')
st.markdown('We will remove all records that have a null field, keeping the results cleaner')

code3 = '''dataframe.dropna(axis=0, inplace=True)'''

st.code(code3, language='python')

dataframe.dropna(axis=0, inplace=True)

with st.expander('View Resulting dataframe'):
    st.write(dataframe)


st.divider()


st.subheader('Manipulating film genre field')
st.markdown('The **_"geres"_** field of the dataset is an array of strings like:')
st.markdown('["Action", "Crime", "Thriller"]')
st.markdown('We will use the **_"apply(eval)"_** function that will evaluate and separate our genres')

code4 = '''dataframe['genres'] = dataframe['genres'].apply(eval)'''

st.code(code4, language='python')

dataframe['genres'] = dataframe['genres'].apply(eval)

with st.expander('View Resulting dataframe'):
    st.write(dataframe)


st.divider()


st.subheader('Creating the profit field')
st.markdown('For future uses we will create a field with the profit of the movie')
st.markdown('To do this, first we will remove the fields in which _"budget"_ and _"revenue"_ are equal to 0')

code5 = '''movies_profit = dataframe.drop(dataframe[(dataframe['budget'] == 0)
& (dataframe['revenue'] == 0)].index)'''

st.code(code5, language='python')

movies_profit = dataframe.drop(dataframe[(dataframe['budget'] == 0) & (dataframe['revenue'] == 0)].index)

st.markdown('Next, we will create the profit field using the calculation of _"revenue"_ subtracted from _"budget"_')

code6 = '''movies_profit['profit'] = movies_profit['revenue'] - movies_profit['budget']'''

st.code(code6, language='python')

movies_profit['profit'] = movies_profit['revenue'] - movies_profit['budget']

with st.expander('View Resulting dataframe'):
    st.write(movies_profit)