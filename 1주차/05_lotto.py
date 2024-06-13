import streamlit as st
import random
import datetime

def generate_lotto():
    lotto=[]

    while len(lotto) <6:
        number = random.randint(1,45)
        lotto.append(number)

    lotto.sort()
    return lotto

st.title("로또 생성가")
bu = st.button("로또를 생성해 주세요!")

if bu:
    for i in range(1,6):
        st.subheader(f"{1}. 행운의 번호 : {generate_lotto()}")
    st.write(f"생성된 시각 : {datetime.datetime.now().strftime('%Y-%m-%d-%H:%M')}")
