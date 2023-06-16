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

# 기능이 실행되는 순수대로 화면에서 출력
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

# st.tabs(["김치찌개", "된장찌개", "찌개"])
# tab1, tab2, tab3 = st.tabs(["김치찌개", "된장찌개", "찌개"]) # 위의 코드를 언팩킹

# tabs = st.tabs(["김치찌개", "된장찌개", "로제마라어묵찌개"])
tab_menus = ["김치찌개", "된장찌개", "로제마라어묵찌개"]
tab1, tab2, tab3 = st.tabs(tab_menus)
img1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4MFBhxEu7tdtEmSpJ-DEzVl9si8NYOiYmbruRyOr7vYS8ZMLSpu60YsPo5WtmB5xg_F0&usqp=CAU"
tab1.image(img1)
with tab2:
    img2 = "https://imagescdn.gettyimagesbank.com/500/201708/jv10940386.jpg"
    st.image(img2)
tab3.write("이런 건 없어요... 상상도 마라요")

exp = st.expander("Surprise!!!", expanded=False)
exp.image("https://i.namu.wiki/i/5lWwYGj-VC8ZqJxug7Exm5-7rHE97fdZui3DWEAjm0zdLiBCbcdw4mLyGhcbZ_KecZOQr4rtwNJSFs63Rsdd_Q.webp")
# with exp: ...

#입력
st.title("입력")
name = st.text_input("와타시노 나마에와")  # 변수로 받을 수 있음
name2 = st.text_input("키미노 나마에와")  # 변수로 받을 수 있음
# st.text_input("")
# st.write(name)
# st.write(name2)
st.write(f"신랑 {name}과 신부 {name2}는...")
# number = st.number_input("당신의 나이는?")
age = st.number_input("당신의 나이는?", step=1)
st.write(f"나의 나이는 {age}세")
height = st.number_input("당신의 키는?", step=0.1)
st.write(f"나의 키는 {height}cm")
# https://docs.streamlit.io/library/api-reference/widgets


st.divider()
mode = st.checkbox("강사님 잔소리모드")  # bool (T/F)
col1, col2, col3 = st.columns(3)
r = col1.radio("잔소리 내용 선택", ["취업", "코딩", "지각"])
s = col2.slider("잔소리 강도 선택", min_value=1, max_value=10)
b = col3.selectbox("잔소리 말투 선택", ["친절하게", "반말", "모욕적"])
if mode:
    # r -> 취업, 코딩, 지각
    format = None
    if b == "친절하게":
        format = lambda x: f"여러분~ {x}"
    elif b == "반말":
        format = lambda x: f"야! {x}"
    elif b == "모욕적":
        format = lambda x: f"XXXXXX! {x}"
    if r == "취업":
        for i in range(s):
            st.write(format("8월에는 자소서 넣어야겠죠?")) # format("") #("")은 변수 x에 기입됨
    elif r == "코딩":
        st.write(format("저보다 파이썬 잘해요?"))
    elif r == "지각":
        st.write(format("9시랑 9시 1분은 다른 거에요."))


# app.py, Sindaebang_TOP3.py, streamlit_app.py, home.py ...
# 리팩토링 -> 코드를 깔끔하고 간명하게 만드는 작업...

# streamlit
import streamlit as st # streamlit 기능묶음(패키지) -> import 불러오고, as ~한 변수명으로 쓰겠다.
# 짧은 별칭(별명) -> 길다보니까 사용성이 낮아져서...
from widget.food_list import get_food_list
from widget.food_detail import get_food_detail

st.title("신대방삼거리 3대맛집")
# streamlit run app.py
# -> 프로젝트 생성 -> 가상환경 (파이썬 관련 설치를 매번 독립적)
# 새로운 프로젝트를 만들면 -> 새롭게 설치
# pip install streamlit

# https://crop-circle.imageonline.co/
# store1 = {
#     "name": "모스키친",
#     "img": "img/s1.png",
#     "star": 5,
#     "desc": "**모스키친**은 신대방삼거리역에 위치한 돈까스 전문점입니다. 이곳의 돈까스는 프리미엄 등심돈까스와 스페셜 등심돈까스 등으로 구성되어 있으며, 특히 스페셜 등심돈까스는 가브리살이 포함되어 더욱 쫄깃한 식감을 제공합니다. 이들 메뉴는 품질에 비해 가격이 매우 합리적이며, 맛있는 음식과 함께 접객이 빠른 서비스로 많은 손님들에게 인기가 있습니다. 최고의 맛을 위해 히말라야 소금에 콕 찍어 와사비를 얹어 먹는 것을 추천합니다."
# }
def make_store(name, img, star, desc, map, link):
    return dict(name=name, img=img, star=star, desc=desc, map=map, link=link)
store1 = make_store(
    "모스키친", "img/s1.png", 5,
    "**모스키친**은 신대방삼거리역에 위치한 돈까스 전문점으로,"\
    "가성비 좋은 고급 돈까스와 빠른 서비스로 인기를 끌고 있습니다."\
    "특히 스페셜 등심돈까스는 가브리살이 포함되어 쫄깃한 식감을 제공하며,"
    "히말라야 소금에 와사비를 얹어 먹는 것을 추천합니다.",
    "img/m1.png",
    "https://naver.me/5JJQDIz0",
)
store2 = make_store(
    "스미비부타동", "img/s2.png", 4,
    "**스미비부타동**은 신대방삼거리역에 위치한 일본식 돼지고기 덮밥(부타동) 전문점으로,"\
    "맛과 양이 풍부하여 혼밥하기 좋은 곳이며, 가격도 합리적이다",
    "img/m2.png",
    "https://naver.me/xfavYBSR",
)
store3 = make_store(
    "미분당", "img/s3.png", 3,
    "**미분당**은 신대방삼거리에 위치한 베트남 음식점으로, 특히 쌀국수로 유명합니다."\
    " 이곳은 베트남 전통 음식인 쌀국수를 한국인의 입맛에 맞게 재해석하였으며,"\
    "일본풍의 분위기와 중국식 상호를 사용하여 다양한 문화와 개성을 지닌 사람들이"\
    "즐길 수 있는 문화 공간을 제공하려는 취지를 가지고 있습니다.",
    "img/m3.png",
    "https://naver.me/5NdqqXJ4",
)
stores = [store1, store2, store3]

# 일종의 딕셔너리 (페이지가 모두 공유하는 딕셔너리)
if 'detail' not in st.session_state:  # key를 확인해서
    st.session_state['detail'] = ""  # 초기값
    st.session_state['map'] = ""  # 초기값
    st.session_state['link'] = ""  # 초기값

# 맛집 리스트
get_food_list(stores)

# 맛집 상세보기
if st.session_state['detail']:  # 초기값의 빈 문자열
    get_food_detail()  # 처음에는 실행하지 않고... 클릭했을 때 반응해서 그려지게

    import streamlit as st


    def set_detail(name):
        st.session_state['detail'] = name


    def get_food_list(stores):
        # 가게 리스트
        # 4개 열 -> 4개 열마다 사진, 가게명, 간단한 설명.
        # for col in st.columns(4):
        for idx, col in enumerate(st.columns(len(stores))):
            # st.columns(4) -> 4개의 열이 묶인 리스트
            # 해당 열들을 순서대로 col이라는 변수로 사용
            # ...
            store = stores[idx]  # <- 외부에서 데이터를 받아서...
            # col.header("맛집이름")
            col.header(store["name"])
            # col.image("https://cdn.pixabay.com/photo/2017/02/10/08/38/pasta-2054656_640.jpg")
            col.image(store["img"])
            # star_count = 5
            star_count = store["star"]
            col.write("".join(["⭐"] * star_count))
            # col.write("설명 설명...")
            col.write(store['desc'])
            # There are multiple identical st.button widgets with the same generated key.
            # st.button -> bool => 눌리면 해당 button => True
            if col.button("자세히보기", key=f"button{idx}", use_container_width=True):
                # 눌렀을 때 실행되는 코드...
                # col.write(store["name"])
                st.session_state['detail'] = store["name"]
                st.session_state['map'] = store["map"]
                st.session_state['link'] = store["link"]
            # 버튼마다 다른 key가 있어야함.


