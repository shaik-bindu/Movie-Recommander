!ls

app_code ="""
import streamlit as st
from model_utils import load_data, build_models, get_content_recommendations, get_collab_recommendations, hybrid_recommend

st.set_page_config(page_title="🎬Personalized Movie Recommendation Dashboard", layout="centered")
st.title("🎬 Personalized Movie Recommendation System")

with st.spinner("Loading data and building models..."):
    movies, ratings = load_data()
    models = build_models(movies, ratings)

option = st.selectbox("Choose recommendation type:", ["Content-Based", "Collaborative", "Hybrid"])

if option == "Content-Based":
    movie = st.selectbox("Select a movie:", movies['title'].unique())
    if st.button("Recommend"):
        recs = get_content_recommendations(movie, models)
        st.subheader("🎯 Recommendations based on genres")
        st.table(recs)

elif option == "Collaborative":
    userId = st.number_input("Enter User ID:", min_value=1, value=1)
    if st.button("Recommend"):
        recs = get_collab_recommendations(userId, models)
        st.subheader("👥 Recommendations based on user behavior")
        st.table(recs)

elif option == "Hybrid":
    userId = st.number_input("Enter User ID:", min_value=1, value=1)
    movie = st.selectbox("Select a movie:", movies['title'].unique())
    if st.button("Recommend"):
        recs = hybrid_recommend(userId, movie, models)
        st.subheader("🔀 Hybrid Recommendations")
        st.table(recs)"""

with open("app.py", "w") as f:
    f.write(app_code)
