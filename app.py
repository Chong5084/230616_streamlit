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

# 마크 다운
# https://heropy.blog/2017/09/30/markdown/

# # st.write / st.markdown
# st.write ->
# st.markdown -> 명백하게 마크다운을 사용 하겠다



# # 제목 마크다운 : 제목을 나타내는 문법
# st.write ("""
#  # : 가장 큰 제목(을 나타낼때 사용) (h1)
#  ## : 그 다음 큰 제목 (h2)
#  ### : 그것보단 작은 제목 <- 대부분 여기까지 (h3)
#  #### : 좀 다 작은 제목 (h4)
#  ##### : 있네 (h5)
#  ###### : 이게 잇네 (h6)
#  ###### : 이건없어
# """) # 문자열 넣으면 마크다운임
#
# # 서식
# text = """
# 기울임 : *별표*를 또는  _언더바_ 하나씩 써주면
#
# Enter 2번 : 줄바꿈
#
# 진하게(bold) : **별표**를 또는 __언더바__ 두 개씩 써주면
#
# 기울임 + 진하게(bold) : ***별표***를 또는  ___언더바___ 세 개씩 써주면
#
# 취소선 : ~물결~
#
# 밑줄 : <u>및줄</u>
#
# 형광펜  : <mark>형광펜<mark>
# """
# # st.write(text)
# # 태그를 허용하는 옵션
# st.markdown(text, unsafe_allow_html=True)
#
# # 레이아웃
# st.subheader("레이아웃")
# st.write("""
#     ### 순서가 없는 리스트
#     * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
#     * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
#     * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
#         * 들여쓰기1
#             * 들여쓰기2
#                 * 들여쓰기3
#     - (-)를 여백 1칸 이상과 사용하면 순서가 없는 리스트
#     - (-)를 여백 1칸 이상과 사용하면 순서가 없는 리스트
#     - (-)를 여백 1칸 이상과 사용하면 순서가 없는 리스트
#         - 들여쓰기1
#             - 들여쓰기2
#                 - 들여쓰기3
# """)
#
#
# st.write("""
#     ### 순서가 있는 리스트
#     1. 순서가
#     2. 있는
#     100. 리스트- 숫자를 건나 뛰어도 무시하고 순서를 따름
#         1. 들여쓰기 1
#             1. 들여쓰기 2 # 1로 시작하지 않으면 무시
#                 1. 들여쓰기 3
#
#    1. 순서가
#    1. 1로 넣어도
#    1. 증가됨
#    ### 가로줄
#    ---
#    (---)
#    ___
#    (___)
#     ### 테이블(표)
#     |머리|머리|
#     |-|-|
#     |파이썬|성장중|
#     |자바|개나줘|
# """)
#
# # 링크
# st.divider()
# st.subheader("링크")
# l1 = "https://naver.com"
# l2 = "https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg"
#
# st.write(f"""
#     * [표시할 텍스트](https://naver.com)
#     * [표시할 텍스트]({l1})
#     * ![이미지에 대한 설명](https://i.imgur.com/3iw01Tk.jpeg)
#     * ![이미지에 대한 설명]({l2})
#     * [![이미지에 대한 설명](https://i.imgur.com/3iw01Tk.jpeg)](https://naver.com)
#
# """)
# # 인용
# st.divider()
# st.subheader("인용")
# st.write(f"""
#     > 무언가 멋진 말 - 유명한 사람
#
#
#     > 진입장벽은 수익이다 - 어느 코딩 강사
#
#     책이나, 사람말 인용할 때...
#     > 인용 첫줄
#     > > 인용문 안에 인용임
#
#     #### 코드
#     `코드를 나타낼 때 주로 쓰이는 묶음 표시 (한줄)`
#     ```
#     여러 줄로 코드를 나타내고
#     줄바꿈도 반영하고 싶으면...
#     print("파이썬!")
#     ```
#     ```python
#     print("파이썬!")
#     ```
# """)





import streamlit as st  # streamlit -> import (가져오기) -> as (st 이름)

# 마크다운
# https://heropy.blog/2017/09/30/markdown/
st.title("마크다운")
# st.write / st.markdown
# st.write -> 입력하는 것에 맞춰서 알아서 결정 => 마크다운
# st.markdown -> 명백하게 마크다운을 사용하겠다
st.divider()
st.subheader("제목")
# 제목 마크다운
st.write("""
# 가장 큰 제목 (h1 - headline1 - st.title)
## 그 다음 큰 제목 (h2 - headline2 - st.header)
### 그것보단 작은 제목 <- 대부분 여기까지만 씀 (h3 - headline3 - st.subheader)
#### 좀 더 작은 제목 (h4)
##### 이건 없겠지? (h5)
###### 이것도 있나? (h6)
####### 이건 없어.
""")  # 문자열을 넣으면 마크다운임
st.divider()
# 서식
st.subheader("서식")
text = """
기울임 : *별표* 또는 _언더바_ 하나씩 써주면

진하게(bold) : **별표**를 또는 __언더바__ 두개씩 써주면

기울임 + 진하게(bold) : ***별표***를 또는 ___언더바___ 세개씩 써주면

취소선 : ~물결표~

밑줄 : <u>밑줄</u>

형광펜 : <mark>형광펜</mark>
"""
# st.write(text)
# 태그를 허용하는 옵션
st.markdown(text, unsafe_allow_html=True)

# 레이아웃
st.divider()
st.subheader("레이아웃")
st.write("""
    #### 순서가 없는 리스트
    * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
        * 들여쓰기1
            * 들여쓰기2
                * 들여쓰기3
    - (-)를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    - (-)를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    - (-)를 여백 1칸 이상과 사용하면 순서가 없는 리스트
        - 들여쓰기1
            - 들여쓰기2
                - 들여쓰기3
""")
st.write("""
    #### 순서가 있는 리스트
    1. 순서가
    2. 있는
    4. 리스트 - 숫자를 건너 뛰어도 무시하고 순서를 따름
        1. 들여쓰기1
            1. 들여쓰기2 # 1로 시작하지 않으면 들여쓰기는 무시
                1. 들여쓰기3
    1. 순서가
    1. 1로 넣어도
    1. 증가됨
    ### 가로줄
    ---
    (---)
    ___
    (___)
    ### 테이블(표)
    |이름|직업|
    |-----|---|
    |파이썬|백수|
    |자바|일잘러|
""")

# 링크
st.divider()
st.subheader("링크")
l1 = "https://naver.com"
l2 = "https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg"
st.write(f"""
    * [표시할 텍스트](https://naver.com)
    * [표시할 텍스트]({l1})
    * ![이미지에 대한 설명](https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg)
    * ![이미지에 대한 설명]({l2})
    * [![이미지에 대한 설명](https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg)](https://naver.com)
""")

# 인용
st.divider()
st.subheader("인용")
st.write(f"""
    > 무언가 멋진 말 - 유명한 사람


    > 진입장벽은 수익이다 - 어느 코딩 강사

    책이나, 사람말 인용할 때...
    > 인용 첫줄
    > > 인용문 안에 인용임

    #### 코드
    `코드를 나타낼 때 주로 쓰이는 묶음 표시 (한줄)`
    ```
    여러 줄로 코드를 나타내고
    줄바꿈도 반영하고 싶으면...
    print("파이썬!")
    ```
    ```python
    print("파이썬!")
    ```
""")

st.title("컴포넌트")
# 위-아래로 한 줄로만....
st.write("👨🏿‍🔬")
cols = st.columns(2)  # 컬럼 리스트
cols[0].write("👨🏿‍🔬")
cols[1].write("👨🏿‍🔬")
cols = st.columns(3)
# 🐦 -> n등분 -> 3등분
cols[0].write("🐦") # 컬러리스트 1번째에 넣겠다
cols[1].write("🐦")
cols[-1].write("🐦")
cols = cols[0].columns(3) # 열의 열인 거임
cols[0].write("🐦")
cols[1].write("🐦")
cols[-1].write("🐦")
col1, col2 = st.columns(2) # 리스트 언팩킹
col1.write("왼쪽 열")
col2.write("오른쪽 열")
# col1, col2 헷갈릴 때

with col1: # col1을 기준으로 streamit을 써주겠다
    # 블록(:)을 열면 -> 이 안에서는 streamit 실행 시 cols1 에 종속
    st.write("왼쪽")
with col2: # col2을 기준으로     streamit을 써주겠다
    # 블록(:)을 열면 -> 이 안에서는 streamit 실행 시 cols2 에 종속
    st.write("오른 쪽")









