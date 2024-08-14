import streamlit as st
import pickle
import pandas as pd

def Recommand(anime):
    anime_index = new_df[new_df["Name"] == anime].index[0]
    distance = similar[anime_index]
    similar_movies_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:11]
    
    recommanded_movies = []
    for i in similar_movies_list:
        recommanded_movies.append(new_df.iloc[i[0]].Name)

    return recommanded_movies    


Anime_names = pickle.load(open('movies_dic.pkl','rb'))
Anime_names = pd.DataFrame(Anime_names)
new_df = pickle.load(open('movies.pkl','rb'))
similar = pickle.load(open('simplar_matrix.pkl','rb'))

st.title("Anime Recommandation System")

st.text("Here I Recommand the Anime Based on Current Choice")

Select_anime = st.selectbox("Select the Anime Name",Anime_names["Name"].values)

animes = Recommand(Select_anime)

if st.button("Recommand", type="primary"):
    for indexes,i in enumerate(animes):
        st.write(f"Top {indexes+1} : ",i)
