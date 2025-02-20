import streamlit as st
import numpy as np
import pandas as pd

#Title of the application 
st.title("hello streamlit")

df = pd.DataFrame({
    'first column': [ 1,2,3,4],
    'second column': [10,20,30,40]

})

st.write("here the data")
st.write(df)



chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)

st.line_chart(chart_data)