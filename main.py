import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# ----- 📌 페이지 설정 -----
st.set_page_config(
    page_title="카카오톡 출생률 변화 예측",
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

# ----- 📈 실제 출생률 데이터 -----
years = np.array(list(range(2000, 2024))).reshape(-1, 1)  # 2000년~2023년
birth_rate = np.array([
    1.47, 1.45, 1.42, 1.39, 1.31, 1.26, 1.22, 1.25, 1.19, 1.15, 1.23, 1.24, 
    1.30, 1.19, 1.21, 1.24, 1.17, 1.05, 0.98, 0.92, 0.84, 0.81, 0.78, 0.72
])  # 현실적인 데이터 반영

df = pd.DataFrame({
    "연도": years.flatten(),
    "출생률 (%)": birth_rate
})

# ----- 📊 출생률 예측 모델 (2050년까지) -----
future_years = np.array(list(range(2024, 2051))).reshape(-1, 1)  # 2024년~2050년
model = LinearRegression()
model.fit(years, birth_rate)
predicted_rates = model.predict(future_years)  # 예측 출생률

# 📉 예측 결과를 DataFrame으로 정리
df_future = pd.DataFrame({
    "연도": future_years.flatten(),
    "출생률 예측 (%)": predicted_rates
})

# ----- 🏆 메인 페이지 제목 -----
st.title("🟡😃 카카오톡 스타일: 한국 출생률 변화 및 예측")
st.markdown('<p class="big-font">📉 연도별 출생률 추이 및 미래 예측</p>', unsafe_allow_html=True)
st.markdown('<p class="small-font">본 데이터는 현실적인 수치를 반영하며, 2050년까지 출생률을 예측합니다.</p>', unsafe_allow_html=True)

# ----- 📊 사용자 선택: 그래프 유형 -----
chart_type = st.sidebar.radio("📊 원하는 차트 유형을 선택하세요:", ["출생률 변화 (라인 그래프)", "연도별 출생률 (막대 그래프)"])

# ----- 🔮 사용자가 예측 데이터 활성화할지 선택 -----
show_prediction = st.sidebar.checkbox("🔮 2050년까지 출생률 예측 데이터 포함")

# ----- 📈 출생률 데이터 시각화 -----
st.subheader("📉 한국 출생률 변화")

if chart_type == "출생률 변화 (라인 그래프)":
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # 실제 데이터 그래프
    ax.plot(df["연도"], df["출생률 (%)"], marker="o", linestyle="-", color="purple", markerfacecolor="mediumorchid", label="실제 출생률")
    
    # 📌 데이터 레이블 추가
    for i, txt in enumerate(df["출생률 (%)"]):
        ax.annotate(f"{txt:.2f}", (df["연도"][i], df["출생률 (%)"][i]), 
                    textcoords="offset points", xytext=(0, 8), ha='center', fontsize=10, color="black")

    # 🔮 예측 데이터 추가
    if show_prediction:
        ax.plot(df_future["연도"], df_future["출생률 예측 (%)"], marker="o", linestyle="--", color="gold", label="출생률 예측")
        for i, txt in enumerate(df_future["출생률 예측 (%)"]):
            ax.annotate(f"{txt:.2f}", (df_future["연도"][i], df_future["출생률 예측 (%)"][i]), 
                        textcoords="offset points", xytext=(0, 8), ha='center', fontsize=10, color="darkorange")

    # 📌 X축을 3년 단위로 조정
    ax.set_xticks(np.arange(2000, 2051, 3))

    ax.set_ylabel("출생률 (%)", color="darkviolet")
    ax.set_xlabel("연도", color="darkviolet")
    ax.set_title("📉 한국 출생률 변화 (2000~2050)", color="darkviolet")
    ax.legend(loc="upper right", fontsize=12, facecolor="lavender", edgecolor="darkviolet")
    ax.grid(True, linestyle="--", alpha=0.5)
    st.pyplot(fig)

elif chart_type == "연도별 출생률 (막대 그래프)":
    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(df["연도"], df["출생률 (%)"], color="mediumorchid")
    
    # 📌 데이터 레이블 추가
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, f"{yval:.2f}", 
                ha='center', va='bottom', fontsize=10, color="black")

    # 🔮 예측 데이터 추가
    if show_prediction:
        bars_future = ax.bar(df_future["연도"], df_future["출생률 예측 (%)"], color="gold")
        for bar in bars_future:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, f"{yval:.2f}", 
                    ha='center', va='bottom', fontsize=10, color="darkorange")

    # 📌 X축을 3년 단위로 조정
    ax.set_xticks(np.arange(2000, 2051, 3))

    ax.set_ylabel("출생률 (%)", color="darkviolet")
    ax.set_xlabel("연도", color="darkviolet")
    ax.set_title("📊 한국 연도별 출생률 변화 및 예측", color="darkviolet")
    st.pyplot(fig)

# ----- 📜 데이터 테이블 -----
st.subheader("📋 연도별 출생률 데이터")
st.dataframe(df)

if show_prediction:
    st.subheader("🔮 2050년까지의 출생률 예측 데이터")
    st.dataframe(df_future)

# ----- 📊 추가 설명 -----
st.sidebar.markdown("### 🟡😃 카카오톡 스타일 한국 출생률 현황")
st.sidebar.write("""
- 본 데이터는 현실적인 출생률을 반영하여 구성되었습니다.
- 선형 회귀 모델을 사용하여 2050년까지 출생률을 예측합니다.
- 예측 데이터를 활성화하려면 체크박스를 눌러주세요.
""")

st.sidebar.markdown('<p class="kakao-yellow">📌 출처: 통계청 & AI 데이터 분석</p>', unsafe_allow_html=True)

