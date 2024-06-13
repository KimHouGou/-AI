import streamlit as st

#버튼
st.title("버튼 입력 사용")
clicked = st.button("버튼1")
st.write("버튼1일 클릭 상태 : ", clicked)

if clicked:
    st.write("버튼 1을 클릭했습니다.")
else:
    st.write("버튼 1을 클릭하지 않음")

#체크박스
st.title("체크박스 사용")
clicked1 = st.checkbox("체크박스1")
st.write("체크박스 상태 : ", clicked1)

#라디오 버튼
st.title("라디오 버튼 사용")
ra_op1 = ['10','20','30','40']
radio1_selected = st.radio('1.(5x5+5)는 얼마인가요?', ra_op1)
st.write("선택한 답 : ", radio1_selected)

ra_op2 = ['마라톤','축구','수영','발레']
radio2_selected = st.radio('2.좋아하는 운동은?', ra_op2)
st.write("선택한 답 : ", radio2_selected)

se1_op = ['하이든','모짜르트','베토벤','슈만']
se2_selected = st.radio('3.좋아하는 음악가는?', se1_op)
st.write("선택한 답 : ", se2_selected)
