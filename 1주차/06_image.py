import streamlit as st
from PIL import Image

st.title("이미지 표시 사용")
# 컴퓨터 내에 있는 이미지 파일을 열어서 표시
st.subheader("1.컴퓨터 내의 이미지 파일을 표시")
img_1 = Image.open(r"D:\AI_NICOL2024\data\avenue.jpg")
st.image(img_1,width=350,caption="컴퓨터 내의 이미지 파일을 열어서 표시한 이미지")
# 웹상의 이미지 표시
st.subheader("2.웹의 이미지 파일을 표시")
# img_1 = Image.open("data\avenue.jpg")
img_url = "https://news.samsungdisplay.com/upload/notice/2023/05/dlvpDzohdp_20230531151658.jpg"
st.image(img_url,width=350,caption="웹상의 이미지 파일을 열어서 표시한 이미지")