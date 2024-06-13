import streamlit as st
from PIL import Image
import pandas as pd

st.title("사용자 지정 화면 분할")

df2 = pd.read_csv("D:\AI_NICOL2024\data\공장별_생산현황2.csv",index_col = 'year')

[col1, col2] = st.columns(2)

with col1:
    st.subheader("DF data")
    st.dataframe(df2)

with col2:
    st.subheader("꺽은선 차트")
    st.line_char(df2)

columns = st.columns([1.2,1.0,0.8])
