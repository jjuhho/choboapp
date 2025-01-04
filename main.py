import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----- 📌 페이지 설정 -----
st.set_page_config(
    page_title="카카오톡 출생률 변화",
    page_icon="🟡😃",
    layout="wide"
)

# ----- 🎨 스타일 설정 -----
st.markdown("""
    <style>
    .big-font {
        font-size: 28px !important;
        font-weight: bold;
    }
    .small-font {
        font-size: 18px;
        color: gray;
    }
    .kakao-yellow {
        color: #FEE500 !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ----- 📈 출생률 데이터 생성 -----
years = list(range(2000, 2024))  # 2000년부터 2023년까지
birth_rate = [
    1.47, 1.45, 1.42, 1.39, 1.31, 1.26, 1.22, 1.25, 1.19, 1.15, 1.23, 1.24, 
    1.30, 1.19, 1.21, 1.24, 1.17, 1.05, 0.98, 0.92, 0.84, 0.81, 0.78, 0.72
]  # 현실적인 데이터 반영

df = pd.DataFrame({
    "연도": years,
    "출생률 (%)": birth_rate
})

# ----- 🏆 메인 페이지 제목 -----
st.title("🟡😃 카카오톡 스타일: 한국 출생률 변화😃😃")
st.markdown('<p class="big-font">📉 연도별 출생률 추이</p>', unsafe_allow_html=True)
st.markdown('<p class="small-font">본 데이터는 현실적인 수치를 반영한 출생률 변화 그래프입니다.</p>', unsafe_allow_html=True)

# ----- 📊 사용자 선택: 그래프 유형 -----
chart_type = st.sidebar.radio("📊 원하는 차트 유형을 선택하세요:", ["출생률 변화 (라인 그래프)", "연도별 출생률 (막대 그래프)"])

# ----- 📈 출생률 데이터 시각화 -----
st.subheader("📉 한국 출생률 변화")

if chart_type == "출생률 변화 (라인 그래프)":
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df["연도"], df["출생률 (%)"], marker="o", linestyle="-", color="purple", markerfacecolor="mediumorchid", label="출생률 (%)")
    
    # 📌 **출생률 값을 그래프 위에 표시**
    for i, txt in enumerate(df["출생률 (%)"]):
        ax.annotate(f"{txt:.2f}", (df["연도"][i], df["출생률 (%)"][i]), 
                    textcoords="offset points", xytext=(0, 8), ha='center', fontsize=10, color="black")

    ax.set_ylabel("출생률 (%)", color="darkviolet")
    ax.set_xlabel("연도", color="darkviolet")
    ax.set_title("📉 한국 출생률 변화 (2000~2023)", color="darkviolet")
    ax.legend(loc="upper right", fontsize=12, facecolor="lavender", edgecolor="darkviolet")
    ax.grid(True, linestyle="--", alpha=0.5)
    st.pyplot(fig)

elif chart_type == "연도별 출생률 (막대 그래프)":
    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(df["연도"], df["출생률 (%)"], color="mediumorchid")
    
    # 📌 **막대 위에 출생률 값 표시**
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, f"{yval:.2f}", 
                ha='center', va='bottom', fontsize=10, color="black")

    ax.set_ylabel("출생률 (%)", color="darkviolet")
    ax.set_xlabel("연도", color="darkviolet")
    ax.set_title("📊 한국 연도별 출생률 변화", color="darkviolet")
    st.pyplot(fig)

# ----- 📜 데이터 테이블 -----
st.subheader("📋 연도별 출생률 데이터")
st.dataframe(df)

# ----- 📊 추가 설명 -----
st.sidebar.markdown("### 🟡😃 카카오톡 스타일 한국 출생률 현황😃😃")
st.sidebar.write("""
- 본 데이터는 현실적인 출생률을 반영하여 구성되었습니다.
- 출생률은 2000년대 이후 지속적인 하락 추세를 보이고 있습니다.
- 차트를 선택하여 데이터를 다양한 방식으로 확인하세요.
""")

st.sidebar.markdown('<p class="kakao-yellow">📌 출처: 통계청 & AI 데이터 분석</p>', unsafe_allow_html=True)
