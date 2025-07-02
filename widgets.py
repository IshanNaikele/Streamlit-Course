import streamlit as st
import datetime
st.title("Learning about Widgets from Course")
ans1=st.radio("Which is your Stream ",['CSE','IT','Mech','Civil','Areonotical'])
st.write(ans1)

ans2=st.button("Click Here")
if ans2:
    st.write("Kya haal chal ?")


ans3=st.checkbox('CSE' )
st.write(ans3)

min_date = datetime.date(1900, 1, 1)
max_date = datetime.date(2015, 12, 31)
ans4=st.date_input("Whats your DOB",min_value=min_date,max_value=max_date)
st.write(ans4)

info=st.slider("",0,100,9)
st.write(info)

find=st.selectbox("Pick your FAvourite Cricketer :",["Virat Kohli","Rohit Sharma","Sai  Sudharshan","Yashashvi Jaiswal","Jasprit Bumbrah"])

if find:
    st.write("Favourite Cricketer :",find)


name=st.text_input("Provide info .")
st.write(name)

num=st.number_input("Provide the no",min_value=12,max_value=88)
st.write(num)


uploaded_file=st.file_uploader("Please Provide your Resume")

if uploaded_file:
    st.write(f"Man,Your resume looks good .")

