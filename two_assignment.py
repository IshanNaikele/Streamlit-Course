import streamlit as st
import datetime


min_date=datetime.date(1900,1,1)

dob=st.date_input("What's your Date of Birth ?",min_value=min_date)
  
if dob:
    # Get current date
    today = datetime.date.today()

    # Calculate age
    age = today.year - dob.year

    # Adjust if birthday hasn't occurred yet this year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    st.write(f"Your age is: **{age}** years")