import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Streamlit 요소 데모", layout="wide")

st.title("Streamlit 요소 데모")
st.header("기본 텍스트 요소")
st.subheader("서브헤더 예시")
st.text("텍스트 예시입니다.")
st.markdown("**마크다운** _스타일_ 지원! :sunglasses:")
st.code("print('Hello Streamlit!')", language="python")

st.header("입력 요소")
name = st.text_input("이름을 입력하세요")
age = st.number_input("나이", min_value=0, max_value=120, value=25)
bio = st.text_area("자기소개를 입력하세요")
agree = st.checkbox("약관에 동의합니다")
gender = st.radio("성별 선택", ["남성", "여성", "기타"])
color = st.selectbox("좋아하는 색상", ["빨강", "파랑", "초록", "노랑"])
multi = st.multiselect("관심사 선택", ["IT", "음악", "운동", "여행", "독서"])
date = st.date_input("날짜 선택")
time = st.time_input("시간 선택")
slider = st.slider("점수", 0, 100, 50)

st.header("버튼 및 상호작용")
if st.button("클릭!"):
    st.success(f"{name}님, 버튼을 눌렀습니다!")

st.header("파일 업로드")
uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("업로드된 데이터:")
    st.dataframe(df)

st.header("미디어 요소")
st.image("https://static.streamlit.io/examples/dog.jpg", caption="강아지 이미지", use_column_width=True)
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
st.video("https://www.w3schools.com/html/mov_bbb.mp4")

st.header("차트와 시각화")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)
st.line_chart(chart_data)
st.bar_chart(chart_data)
st.area_chart(chart_data)

st.header("알림 및 상태 표시")
st.success("성공 메시지 예시")
st.info("정보 메시지 예시")
st.warning("경고 메시지 예시")
st.error("에러 메시지 예시")

st.header("진행률 표시")
import time
progress = st.progress(0)
for i in range(1, 101):
    progress.progress(i)
    time.sleep(0.01)

st.header("사이드바")
st.sidebar.title("사이드바 메뉴")
st.sidebar.write("여기서도 다양한 요소를 넣을 수 있습니다.")
sidebar_option = st.sidebar.selectbox("사이드바 옵션", ["옵션1", "옵션2", "옵션3"])
st.sidebar.slider("사이드바 슬라이더", 0, 10, 5)
