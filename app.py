# $ pip install streamlit
# $ streamlit hello # $ = 터미널에 쓰인다는 의미
# ctrl + c : 실행 종료 (터미널)

import streamlit as st  # streamlit -> import (가져오기) -> as (st 이름)
# st라는 변수명으로 streamlit의 기능들을 사용하겠다

# st. -> ctrl + space(기능보기) -> 다양한 기능(함수, 메소드)을 가지고 있다

st.title("나의 파이썬 웹 페이지")
st.header("수업 8일차에 만들었어요")
st.subheader("그래도 잘 만들었죠?")
st.write("내가 만든 페이지, 너를 위해 구웠지 feat. Chong")

# 기능이 실행되는 순수대로 화면에서 추렭
st.video("https://www.youtube.com/watch?v=SaCheA6Njc4") # 암 유투브 링크

st.githy("https://media2.giphy.com/media/MT5UUV1d4CXE2A37Dg/giphy.gif?cid=7941fdc6ko0md0152a5yh2pzbmjcevj3u457281v3jc5bqz8&ep=v1_gifs_search&rid=giphy.gif&ct=g")
st.git("https://media2.giphy.com/media/MT5UUV1d4CXE2A37Dg/giphy.gif?cid=7941fdc6ko0md0152a5yh2pzbmjcevj3u457281v3jc5bqz8&ep=v1_gifs_search&rid=giphy.gif&ct=g")

# streamlit run app.py