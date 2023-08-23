import pandas as pd
import streamlit as st
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


st.title("Data pre-processing")


dataframe = pd.read_csv(
    "./data/top_1000_popular_movies_tmdb.csv", lineterminator="\n", index_col=0
)

dataframe.drop(
    ["id", "title", "release_date", "overview", "tagline", "production_companies"],
    axis=1,
    inplace=True,
)

# dataframe.dropna(axis=0, inplace=True)
# dataframe = dataframe[dataframe["revenue"] != 0]

# Dummies dos gêneros
mlb = MultiLabelBinarizer()
genres_dummies = pd.DataFrame(
    mlb.fit_transform(dataframe["genres"].apply(eval)),
    columns=mlb.classes_,
    index=dataframe.index,
)
dataframe.drop(["genres"], axis=1, inplace=True)
dataframe = pd.concat([dataframe, genres_dummies], axis=1)


# Dummies das linguagens
lenguage_dummies = pd.get_dummies(dataframe['original_language'])
lenguage_dummies = lenguage_dummies.astype(int)
dataframe.drop(['original_language'], axis=1, inplace=True)
dataframe = pd.concat([dataframe, lenguage_dummies], axis=1)

temporary_column = dataframe.pop('revenue')
dataframe.insert(0, 'revenue',temporary_column)


x_movies = dataframe.iloc[:, 1:].values
y_movies = dataframe.iloc[:, 0].values

x_movies_treinamento, x_movies_teste, y_movies_treinamento, y_movies_teste = train_test_split(x_movies, y_movies, test_size=0.3, random_state=0)


# Regressão múltipla
regressor_mult_movies = LinearRegression()
regressor_mult_movies.fit(x_movies_treinamento, y_movies_treinamento)

print(regressor_mult_movies.score(x_movies_teste, y_movies_teste))

previsoes = regressor_mult_movies.predict(x_movies_teste)

print(mean_absolute_error(y_movies_teste, previsoes))

# st.subheader('Regressão múltipla')
# st.write('Regressão múltipla score: 0.7074702194743039')
# st.write('Regressão múltipla Error absoluto médio: 57541643.63203637')



# st.subheader('Regressão múltipla')

# poly = PolynomialFeatures(degree=2)

# x_movies_treinamento_poly = poly.fit_transform(x_movies_treinamento)
# x_movies_teste_poly = poly.transform(x_movies_teste)

# regressor_movies_poly = LinearRegression()
# regressor_movies_poly.fit(x_movies_treinamento_poly, y_movies_treinamento)

# previsoes = regressor_movies_poly.predict(x_movies_teste_poly)

# print(regressor_movies_poly.score(x_movies_teste_poly, y_movies_teste))
# print(mean_absolute_error(y_movies_teste, previsoes))