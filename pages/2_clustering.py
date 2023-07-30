import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn import cluster
from helper import get_dataframe


st.title('Profit clustering')

st.markdown('Clustering is an unsupervised learning technique in the field of Machine Learning. It is used to find natural patterns and structures in a dataset by grouping the examples into "clusters" or groups, where the members of each cluster are more similar to each other than to members of other clusters.')

st.markdown('Next, we will use the scikit-learn library to apply a clustering technique to our dataframe. The template must use the _"profit"_ field next to _"budget"_ to group movies into _"blockbuster"_, _"moderated"_ or _"failure"_.')

st.markdown('The chosen clustering algorithm was K-means. It divides the dataset into K clusters, where K is a user-defined number. The algorithm tries to minimize the sum of squares of the examples distances to the centroid of their cluster.')


st.divider()


st.markdown('''First let's import our dataframe using the helper function.''')

code1 = '''movies_profit = get_dataframe(profit=True)'''
st.code(code1, language='python')

movies_profit = get_dataframe(profit=True)

with st.expander('View dataframe'):
    st.write(movies_profit)


st.markdown('We select the columns of "budget" and "profit"')

st.code('x_movies = movies_profit.iloc[:, [7, 11]].values', language='python')
x_movies = movies_profit.iloc[:, [7, 9]].values

with st.expander('View resulting dataframe'):
    st.write(x_movies)



st.markdown('Then, using the StandardScaler function of scikit-learn we will calculate the fits')

code2 = '''
    scaler_movies = StandardScaler()
    x_movies = scaler_movies.fit_transform(x_movies)
'''
st.code(code2, language='python')

scaler_movies = StandardScaler()
x_movies = scaler_movies.fit_transform(x_movies)

with st.expander('View resulting dataframe'):
    st.write(x_movies)



st.markdown('''To decide the ideal number of clusters, let's rely on wcss.''')
st.markdown('WCSS (Within-Cluster Sum of Squares), also known as Sum of Squares Within Clusters, is a metric commonly used in clustering to assess the quality of clusters formed by a clustering algorithm such as K-Means. The purpose of WCSS is to measure the compression of data within each cluster.')
st.markdown('To display the graph, use the following code:')

code3 = '''
    wcss = []
    for i in range(1, 11):
        kmeans_movies = cluster.KMeans(n_clusters = i, random_state = 0)
        kmeans_movies.fit(x_movies)
        wcss.append(kmeans_movies.inertia_)

    graph = px.line(x = range(1, 11), y = wcss)
'''
st.code(code3, language='python')

wcss = []
for i in range(1, 11):
    kmeans_movies = cluster.KMeans(n_clusters = i, random_state = 0)
    kmeans_movies.fit(x_movies)
    wcss.append(kmeans_movies.inertia_)

graph = px.line(x = range(1, 11), y = wcss)

st.write(graph)



st.markdown('With the number of clusters chosen, we can proceed with the implementation of the algorithm:')

code4 = '''
    kmeans_movies = cluster.KMeans(n_clusters=3, random_state=0, n_init='auto')
    labels = kmeans_movies.fit_predict(x_movies)
    labels = pd.DataFrame(labels)
    labels.replace(2, 'blockbuster', inplace=True)
    labels.replace(1, 'moderate', inplace=True)
    labels.replace(0, 'failure', inplace=True)

    fig = px.scatter(x = x_movies[:, 0], y = x_movies[:, 1], color=labels[0])
'''

kmeans_movies = cluster.KMeans(n_clusters=3, random_state=0, n_init='auto')
labels = kmeans_movies.fit_predict(x_movies)
labels = pd.DataFrame(labels)
labels.replace(2, 'blockbuster', inplace=True)
labels.replace(1, 'moderate', inplace=True)
labels.replace(0, 'failure', inplace=True)

fig = px.scatter(x = x_movies[:, 0], y = x_movies[:, 1], color=labels[0], title='Movies Clustered by Profit')

st.write(fig)