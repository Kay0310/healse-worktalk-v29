import streamlit as st
import os
from PIL import Image

st.set_page_config(page_title="WORK TALK 위험성평가", layout="wide")

if "responses" not in st.session_state:
    st.session_state.responses = []

st.markdown("### 사진 1장 업로드 ➜ 질문 4개 응답 ➜ 저장 ➜ 다음 사진 순서대로 진행해 주세요.")
st.image("WORK_TALK_small.png", width=150)

name = st.text_input("이름")
team = st.text_input("부서")

uploaded_file = st.file_uploader("📷 작업 사진 업로드", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, use_container_width=True)

    q1 = st.text_input("어떤 작업을 하고 있는 건가요?", key="q1")
    q2 = st.text_input("이 작업은 왜 위험하다고 생각하나요?", key="q2")
    q3 = st.radio("이 작업은 얼마나 자주 하나요?", ["연 1-2회", "반기 1-2회", "월 2-3회", "주 1회 이상", "매일"], key="q3")
    q4 = st.radio("이 작업은 얼마나 위험하다고 생각하나요?", [
        "약간의 위험: 일회용 밴드 치료 필요 가능성 있음",
        "조금 위험: 병원 치료 필요. 1-2일 치료 및 휴식",
        "위험: 보름 이상의 휴식이 필요한 중상 가능성 있음",
        "매우 위험: 불가역적 장애 또는 사망 가능성 있음"], key="q4")

    if st.button("💾 저장하기"):
        st.session_state.responses.append({
            "이름": name,
            "부서": team,
            "파일명": uploaded_file.name,
            "어떤 작업을 하고 있는 건가요?": q1,
            "이 작업은 왜 위험하다고 생각하나요?": q2,
            "작업 빈도": q3,
            "위험도": q4
        })
        st.success("✅ 저장 완료! 다음 사진을 입력해 주세요.")