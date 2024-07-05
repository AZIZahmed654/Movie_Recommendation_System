import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=67751b8ace2704e0168f9e5bc7e3806b".format(movie_id)
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path



def recommend(movie):
    movie_index = movies[movies['title']== movie].index[0]
    distance=similarity[movie_index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[0:6]
    recommended_movie_posters = []
    recommended_movies=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        #fetch poster from api
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movie_posters



movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))



st.title("MOVIE RECOMMENDER SYSTEM")


selected_movie=st.selectbox(
    'please select your movie',
movies['title'].values)



if st.button("Give Recommendations"):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5, col6 = st.columns(6,gap="large")
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0],width=120)
        st.write(recommended_movie_names[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1],width=120)
        st.write(recommended_movie_names[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2],width=120)
        st.write(recommended_movie_names[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3],width=120)
        st.write(recommended_movie_names[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4],width=120)
        st.write(recommended_movie_names[4])
    with col6:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5],width=120)
        st.write(recommended_movie_names[5])


  
