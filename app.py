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
st.image("https://cdn.pixabay.com/photo/2023/06/02/14/12/woman-8035772_1280.jpg")  # 인터넷 링크
# streamlit run app.py
# 기능이 실행되는 순서대로 화면에서 표현
st.video("https://www.youtube.com/watch?v=SaCheA6Njc4")  # 유튜브 링크
st.image("https://cdn.pixabay.com/photo/2023/06/02/14/12/woman-8035772_1280.jpg")  # 인터넷 링크
st.image("https://i.imgur.com/jorp5JH.png")  # 인터넷 링크
# 여러 가지 옵션을 넣어서 세부 기능들을 차이

# 내 컴퓨터(내파일)내에 있는 이미지 첨부
st.image("img/img.png")  # 파일 경로 (app.py)
st.image(image="img/img.png")  # 키워드를 사용해서...
st.image("img/img.png", use_column_width=True)  #파일 경로 (app.py)
st.image("img/img.png", width=100)  # 파일 경로 (app.py) / width=100 = 이미지 픽셀 크기
# https://imgur.com/

# GIF 파일 로드하기
gif_file = open('example.gif', 'rb').read()

# 이미지 추가하기
st.image(gif_file, format='gif')

import requests

response = requests.get("https://media2.giphy.com/media/MT5UUV1d4CXE2A37Dg/giphy.gif?cid=7941fdc6ko0md0152a5yh2pzbmjcevj3u457281v3jc5bqz8&ep=v1_gifs_search&rid=giphy.gif&ct=g")
gif = response.content
st.image(gif, format="gif")