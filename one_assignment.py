import streamlit as st

st.title("Solving 1st Assignment")

st.subheader("Develop a selectbox of multiple Programing Language")

lang=st.selectbox("Choose Your Favourite Programming Language :",["Python","C++","C","Java","R","JavaScript","other"])

st.write(f"Your Favourite Programming Language is **{lang}**")