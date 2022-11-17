# pip list --format=freeze > requirements.txt
import pandas as pd
import pickle
#import _pickle as cPickle
#import bz2
import requests
import streamlit as st
from custom_functions import st_button


dict_of_movies = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(dict_of_movies)
# Load any compressed pickle file
#def decompress_pickle(file):
#    data = bz2.BZ2File(file, 'rb')
#    data = cPickle.load(data)
#    return data
#similarity = decompress_pickle('similarity_comp.pbz2')
similarity = pickle.load(open('similarity_scores.pkl','rb'))

def fetch_movie_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3c946f1b1729f6bf9771a49d54aceb9d&language=en-US'.format(movie_id))
    data = response.json()
    try:
        return "https://image.tmdb.org/t/p/w500" + data['poster_path']
    except:
        pass

def recommend_top_movies(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_tuple = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    poster_url = []
    for entry in movies_tuple:
        movie_id = movies.iloc[entry[0]].id
        recommendations.append(movies.iloc[entry[0]].title)
        # fetch poster from API
        poster_url.append(fetch_movie_poster(movie_id))
        # since poster_path given in our dataset is not working for some movies, so we use api method to fetch posters
        #poster_url.append("https://image.tmdb.org/t/p/w500" + movies.iloc[entry[0]].poster_path)
    return recommendations, poster_url

st.title('Movie Recommender System')

entered_movie = st.selectbox(
'Please enter a movie of your choice',
movies['title'].values
)

if st.button('Recommend'):
    movie_names, movie_posters = recommend_top_movies(entered_movie)
    print(movie_names)
    #print(movie_posters)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_names[0])
        st.image(movie_posters[0])
    with col2:
        st.text(movie_names[1])
        st.image(movie_posters[1])
    with col3:
        st.text(movie_names[2])
        st.image(movie_posters[2])
    with col4:
        st.text(movie_names[3])
        st.image(movie_posters[3])
    with col5:
        st.text(movie_names[4])
        st.image(movie_posters[4])

st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

st.markdown("<h4 style='text-align: center; color: black;'>- by Mohammad Irfan</h1>", unsafe_allow_html=True)
#st.write("Mohammad Irfan")
icon_size=18
st_button('github','https://www.github.com/mirfan57','Github', icon_size)
st_button('linkedin','https://www.linkedin.com/in/mirfan57','Linkedin', icon_size)

