import streamlit as st
import datetime

#텍스트 입력
st.title("텍스트 입력 사용")
user_id = st.text_input("아이디(ID) 입력", value = 'streamlit', max_chars = 15)
user_pw = st.text_input("패스워드 입력", value = 'acde', type = 'password')

if user_id == 'streamlit':
    if user_pw ==  '1234':
        st.write("로그인 성공!")
    else:
        st.write("패스워드 오류")

else:
    st.write("없는 ID, 회원가입을 하거나 아이디 체크")

#날짜 입력
birth = st.date_input("1, 당신의 생일은?", value = datetime.date(2000,1,1))
st.write("당신의 생일 : ", birth)

data_range = st.date_input("2. 시작과 끝 날짜를 선택?",
                           value=[datetime.date(2024,3,1),datetime.date(2024,5,30)],
                           min_value=datetime.date(2024,2,1),
                           max_value=datetime.date(2024,6,7))
st.write("선택한 날짜의 범위 : ", data_range)

#시간 입력
alarm_time = st.time_input("알람 시각을 설정", value=datetime.time(7,30))
st.write("알람 설정 시간 : ", alarm_time)