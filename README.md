# Movie_recommindor

## Movie Recommender System | Collaborative Filtering Based Recommendation
This project implements a Machine Learning-based Movie Recommender System using Collaborative Filtering and K-Nearest Neighbors (KNN). The system consists of two main components:

1️⃣ Model Training (movie_recommindation.ipynb) → Prepares the dataset, trains the recommendation model, and saves processed data.
2️⃣ Web Application (app.py) → Loads the trained model and provides an interactive interface for users to get movie recommendations.

1. # **Project Overview**
This project is a movie recommendation system that suggests movies based on user preferences. It applies collaborative filtering, where recommendations are made based on user ratings.

✨ ## **Features**
✔ Uses KNN (K-Nearest Neighbors) for collaborative filtering.
✔ Suggests movies similar to a given movie.
✔ Fetches movie posters dynamically from TMDb & OMDb APIs.
✔ Provides an interactive UI using Streamlit.
✔ Processes the MovieLens dataset for recommendations.

2. # **Code Breakdown**
📌 movie_recommindation.py – Model Training & Preprocessing

This script prepares data, trains the recommendation model, and saves processed data for later use.

🛠 ## **Steps in model_training.py**
1️⃣ Load the MovieLens dataset

Reads movies.csv (movie titles) and ratings.csv (user ratings).

Displays dataset information using .info() and .head().

2️⃣ Filter Active Users

Keeps only users who have rated more than 200 movies for better recommendations.

3️⃣ Merge Ratings with Movie Titles

Joins ratings with movies to link movieId to actual movie titles.

4️⃣ Filter Movies with Enough Ratings

Keeps only movies with at least 5000 ratings to ensure quality recommendations.

5️⃣ Create a Pivot Table

Converts the dataset into a user-movie matrix, where:

Rows = Movie titles

Columns = Users

Values = Ratings (0 for missing ratings)

6️⃣ Train the KNN Recommendation Model

Converts the pivot table into a sparse matrix for efficient computation.

Trains a Nearest Neighbors model using the Brute Force algorithm.

7️⃣ Test Movie Recommendations

Finds similar movies for "Spider-Man (2002)" and "Batman Begins (2005)".

Prints the top 6 closest movies based on similarity.

8️⃣ Save Model & Processed Data

Stores the trained model and processed data using pickle.

📌 app.py – Streamlit Web Application

This script loads the trained model and provides an interactive interface where users can select a movie and receive recommendations.

🛠 ## **Steps in app.py**

1️⃣ Load Required Libraries

Imports pickle (for loading the model), numpy, requests, and streamlit.

2️⃣ Load Pre-Trained Model & Processed Data

Loads:

model.pkl → Trained KNN model

movies_pivot.pkl → Movie-user pivot table

final_rating.pkl → Processed movie rating dataset

movie_names.pkl → List of available movie titles

3️⃣ Set Up API Keys

Uses TMDb API and OMDb API to fetch movie posters.

Defines a default placeholder image for missing posters.

4️⃣ Functions to Fetch Movie Posters

fetch_movie_poster_tmdb() → Gets movie posters from TMDb.

fetch_movie_poster_omdb() → Falls back to OMDb if TMDb fails.

fetch_movie_poster() → Tries TMDb first, then OMDb, otherwise uses a default image.

5️⃣ Fetch Movie Genres

fetch_genre(suggestion) → Retrieves genres for recommended movies.

6️⃣ Movie Recommendation Function

recommend_movies(movie_name, number_of_movies)

Finds similar movies using the trained KNN model.

Fetches movie genres for the recommendations.

Returns a list of recommended movie titles & genres.

7️⃣ Create a Streamlit Web App

Movie Selection Dropdown (st.selectbox) → Allows users to select a movie.

Number of Recommendations Dropdown (st.selectbox) → Lets users choose how many movies to get.

"Show Recommendation" Button (st.button) → Displays recommendations, including:

Movie titles
Movie genres
Movie posters
