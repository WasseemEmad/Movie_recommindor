import pickle
import streamlit as st
import numpy as np
import requests

st.header("ML Based Movie Recommender System | using collaborative filtering based recommendation system")

model = pickle.load(open('C:/Users/Wasseem/Desktop/project/movie recommendor/saved/model.pkl','rb'))
movies_pivot =  pickle.load(open('C:/Users/Wasseem/Desktop/project/movie recommendor/saved/movies_pivot.pkl','rb'))
final_rating = pickle.load(open('C:/Users/Wasseem/Desktop/project/movie recommendor/saved/final_rating.pkl','rb'))
movie_names = pickle.load(open('C:/Users/Wasseem/Desktop/project/movie recommendor/saved/movie_names.pkl','rb'))

TMDB_API_KEY = ""
OMDB_API_KEY = ""

DEFAULT_IMAGE = "C:/Users/Wasseem/Desktop/project/movie recommendor/no-image-icon-23494.png"

def fetch_movie_poster_tmdb(movie_title):
    """Fetch movie poster from TMDb API"""
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_title}"
    
    response = requests.get(search_url)
    data = response.json()
    
    if data.get('results'):
        poster_path = data['results'][0].get('poster_path')  
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"  
    
    return None  

def fetch_movie_poster_omdb(movie_title):
    """Fetch movie poster from OMDb API and handle 'N/A' response"""
    search_url = f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}"
    
    response = requests.get(search_url)
    data = response.json()
    
    poster_url = data.get("Poster")
    
    
    if poster_url == "N/A":
        return None

    return poster_url 

def fetch_movie_poster(movie_title):
    """Try fetching movie poster from TMDb first, then OMDb, else use a placeholder"""
    poster_url = fetch_movie_poster_tmdb(movie_title) 
    
    if not poster_url: 
        poster_url = fetch_movie_poster_omdb(movie_title)
    
    
    return poster_url if poster_url else DEFAULT_IMAGE



def fetch_genre(suggestion):
        """Try fetching movie genre"""
        movie_name = []
        ids_index = []
        movies_genres = []

        for movie_id in suggestion:
            movie_name.append(movies_pivot.index[movie_id])

        for name in movie_name[0]: 
            ids = np.where(final_rating['title'] == name)[0][0]
            ids_index.append(ids)

        for idx in ids_index:
            genre = final_rating.iloc[idx]['genres']
            movies_genres.append(genre)

        return movies_genres


def recommend_movies(movie_name, number_of_movies):
    movie_list = []
    movie_id = np.where(movies_pivot.index == movie_name)[0][0]
    distance, suggestion = model.kneighbors(movies_pivot.iloc[movie_id,:].values.reshape(1,-1), n_neighbors=number_of_movies)
    
    movie_genre = fetch_genre(suggestion)
    
    for i in range(len(suggestion)):
            movies = movies_pivot.index[suggestion[i]]
            for movie in movies:
                movie_list.append(movie)
    return movie_list , movie_genre


selected_movies = st.selectbox(
    "Type or select a movie",
    movie_names,
    key="movie_selectbox"
)

selected_movie_number = st.selectbox(
    "Select a number of recommender movies",
    list(range(5, 11)),
    key="number_selectbox"
)

if st.button('Show Recommendation'):
    recommendation_movie, movie_genres = recommend_movies(selected_movies,selected_movie_number+1)
    num_columns = len(recommendation_movie) 
    cols = st.columns(num_columns)
    for i in range(1, num_columns): 
        col = cols[i]
        with col:
            st.text(recommendation_movie[i])
            st.text(movie_genres[i])
            
            poster_url = fetch_movie_poster(recommendation_movie[i])
            st.image(poster_url)
    
