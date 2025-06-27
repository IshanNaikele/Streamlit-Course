import streamlit as st

st.title("Learning Streamlit")
st.subheader("Welcome to Streamlit App")
st.text("What's Going on?")
st.write("""  
         # Hello World
         I am Learning *Streamlit*
         I am Learning Streamlit
         """)

ans=st.selectbox("Which is your Favourite Sport ?",["Cricket","Football","Hockey","Chess","Basketball"])

st.write(f"You choose {ans}")
st.text(f"You choose {ans}")

st.success("Your Sports has been collected")