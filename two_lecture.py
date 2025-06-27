import streamlit as st
import datetime
st.title("Learning Streamlit")

if st.button("Man ,You have to Win"):
    st.success("**Consistency**+**Discipline**+**Focus**+**Dedication**==**Success**")


cricketer=st.checkbox("Virat Kohli" )
 
if cricketer:
    st.write("Who are you ?")

ans=st.radio("Pick your FAvourite Cricketer :",["Virat Kohli","Rohit Sharma","Sai  Sudharshan","Yashashvi Jaiswal","Jasprit Bumbrah"])

if ans :
    st.write("Favourite Cricketer :",ans)

find=st.selectbox("Pick your FAvourite Cricketer :",["Virat Kohli","Rohit Sharma","Sai  Sudharshan","Yashashvi Jaiswal","Jasprit Bumbrah"])

if find:
    st.write("Favourite Cricketer :",find)

mark=st.slider("Which is your Physics Score ?",0,100,5)

if mark:
    st.write(mark)

count=st.number_input("pick your Spoken Profiency:",min_value=1,max_value=10,step=1)

if count==1:
    st.write("Beginner")
if count==10:
    st.write("Pro" )


name=st.text_input("What is your name?")
if name:
    st.write(f"The name is **{name}**")

# Set date range: only allow dates up to 31-Dec-2015
min_date = datetime.date(1900, 1, 1)
max_date = datetime.date(2015, 12, 31)
dob=st.date_input("What's your Date of Birth ?",min_value=min_date,max_value=max_date)

if dob :
    st.write(f"The Date of Birth :{dob}")





