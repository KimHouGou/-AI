import streamlit
import pandas as pd

#텍스트 요소
streamlit.title("인공지능 모델 배포")
streamlit.header("헤더")
streamlit.text("김정희, 일반 텍스트 입니다.")

streamlit.markdown("스트림릿에서 **마크다운**")

#데이터 요소
df = pd.read_csv(r"D:\AI_NICOL2024\data\korea_rain1.csv")

streamlit.subheader("스트림릿에서 데이터 표시 - dataframe")
streamlit.dataframe(df)

streamlit.subheader("스트림릿에서 데이터 표시 - table")
streamlit.table(df)

#차트 요소
df1 = pd.read_csv("D:\AI_NICOL2024\data\공장별_생산현황.csv")
ax = df1.plot()
ax.set_title("공장별 생산 현황", fontsize = 20)
ax.set_xlabel("연도")
ax.set_ylabel("생산량")
fig1 = ax.get_figure()

streamlit.subheader("꺽은선형 차트")
streamlit.pyplot(fig1)

df2 = pd.read_excel("D:\AI_NICOL2024\data\영업팀별_판매현황.xlsx", index_col = '월')
ax = df2.plot.bar(grid = True, figsize = (15,5))
fig2 = ax.get_figure()

streamlit.subheader("막대형 차트")
streamlit.pyplot(fig2)
