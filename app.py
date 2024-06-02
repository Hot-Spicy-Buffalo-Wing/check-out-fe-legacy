# %%
import streamlit as st
import pandas as pd
import requests
from PIL import Image
import dotenv
import os

dotenv.load_dotenv()

# %%
st.set_page_config(page_title="Lookbook", layout="wide")

lookbook_images = ["images/img1.png", "images/img2.png", "images/img3.png"]
# %%
# 메인 페이지 타이틀
st.title("Lookbook")

# 다른 사람들의 lookbook 이미지 표시
st.header("Explore Lookbooks")
cols = st.columns(3)
for i, img_path in enumerate(lookbook_images):
    img = Image.open(img_path)
    cols[i % 3].image(img, use_column_width=True)

# 오늘의 추천받은 옷차림 공간
st.header("Today's Outfit Recommendation")

if "recommended_outfit" not in st.session_state:
    st.session_state.recommended_outfit = None

if st.session_state.recommended_outfit:
    st.image(st.session_state.recommended_outfit, use_column_width=True)
else:
    st.write("오늘의 옷차림을 추천받으세요!")
    # if st.button("추천받기"):
    #     # 임시 이미지 추천 (실제 추천 시스템 연결 필요)
    #     st.session_state.recommended_outfit = "recommended_image.jpg"  # 실제 추천 이미지로 변경하세요
    #     st.experimental_rerun()
# %%
area_df = pd.read_excel("data/areaNo.xlsx", sheet_name="final_formatted")
area_df.head()

# %% TODO: dependent selection box
with st.expander("Create Lookbook"):
    gender = st.selectbox("성별", ["여자", "남자", "논바이너리"])
    age_range = st.selectbox(
        "연령대",
        [
            "10대 초반",
            "10대 후반",
            "20대 초반",
            "20대 후반",
            "30대 초반",
            "30대 후반",
            "40대 이상",
        ],
    )

    province_options = area_df["1단계"].unique().tolist()
    province_selection = st.selectbox("사는 지역", province_options)
    city_options=area_df[area_df["1단계"]==province_selection]["2단계"].dropna().unique().tolist()
    city_selection = st.selectbox("구/군", city_options)  # 선택지 추가 가능
    district_options=area_df[area_df["2단계"]==city_selection]["3단계"].dropna().unique().tolist()
    district_selection = st.selectbox("동/읍/면", district_options)  # 선택지 추가 가능
    tpo = st.multiselect(
        "TPO 정보",
        [
            "데이트",
            "여행",
            "출근",
            "결혼식 하객으로 참석",
            "꾸안꾸",
            "여름코디",
            "캠퍼스룩",
            "데일리",
            "휴양지",
            "놀이공원",
            "카페",
            "운동하러",
            "축제",
            "파티",
            "소개팅",
        ],
    )

    if st.button("lookbook 생성"):
        # url="https://ai.check-out.paperst.ar/lookbook"
        # url = "http://localhost:8000/lookbook"
        url = f'{os.getenv("API_BASE_URL")}/lookbook'
        response = requests.post(
            url,
            json={
                "gender": gender,
                "ageRange": age_range,
                "area": {
                    "province": province_selection,
                    "city": city_selection,
                    "district": district_selection,
                },
                "TPO": tpo,
            },
        )
        response_url = response.content.decode("utf-8")["url"]
        # TODO: 이미지 url을 받아서 이미지를 S3에 업로드하고, 새로운 이미지 url을 반환받아 image_urls에 추가
        # st.session_state.outfit_image = "/images/outfit1.jpg"  # 실제 생성된 코디 이미지로 변경하세요
        # st.experimental_rerun()
# %%
# 코디 이미지 선택 및 업로드 승인
if "outfit_images" in st.session_state:
    st.header("Your Lookbook")
    outfit_images = st.session_state.outfit_images
    cols = st.columns(3)
    for i, img_path in enumerate(outfit_images):
        img = Image.open(img_path)
        if cols[i % 3].button("BEST CHOICE", key=img_path):
            st.session_state.best_choice = img_path
            st.experimental_rerun()

if "best_choice" in st.session_state:
    st.image(st.session_state.best_choice, use_column_width=True)
    if st.button("업로드 승인"):
        st.write("Lookbook 업로드 승인되었습니다!")
        # 실제 업로드 처리 로직 추가 필요

# 실제 코디 이미지 업로드
if "best_choice" in st.session_state:
    st.header("Upload Your Actual Outfit Photo")
    uploaded_file = st.file_uploader("Choose a file", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        actual_outfit_img = Image.open(uploaded_file)
        st.image(actual_outfit_img, caption="Actual Outfit", use_column_width=True)
        # 실제 업로드 처리 로직 추가 필요
