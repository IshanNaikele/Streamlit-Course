import streamlit as st
import pandas as pd
import numpy as np

st.title("Learning from Gen AI Course")
data=pd.DataFrame({
    'first_column':[10,20,30,40],
    'second_column':[1,2,3,4]
})

st.write(data)

st.line_chart(data)

chart_data=pd.DataFrame(
    np.random.randn(10,3),columns=['one','two','three']
)

st.line_chart(chart_data)