import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----- 📌 페이지 설정 -----
st.set_page_config(
    page_title="K-pop 스트리밍 순위",
    page_icon="🎵",
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
    </style>
""", unsafe_allow_html=True)

# ----- 🎵 K-pop 가수 리스트 & 가짜 스트리밍 데이터 생성 -----
kpop_artists = [
    "BTS", "BLACKPINK", "SEVENTEEN", "TWICE", "NEWJEANS",
    "STRAY KIDS", "IVE", "LE SSERAFIM", "EXO", "AESPA"
]

# 가짜 스트리밍 데이터 생성 (단위: 백만)
streaming_data = { 
    "가수": kpop_artists,
    "스트리밍 수 (백만)": np.random.randint(200, 1000, size=len(kpop_artists))
}

df = pd.DataFrame(streaming_data)
df = df.sort_values(by="스트리밍 수 (백만)", ascending=False)

# ----- 🏆 메인 페이지 제목 -----
st.title("🎶 K-pop 스트리밍 순위")
st.markdown('<p class="big-font">실시간 K-pop 스트리밍 랭킹</p>', unsafe_allow_html=True)
st.markdown('<p class="small-font">이 데이터는 현실적이지만 가상의 데이터입니다.</p>', unsafe_allow_html=True)

# ----- 📊 사용자 선택: 그래프 유형 -----
chart_type = st.sidebar.selectbox("📊 원하는 차트 유형을 선택하세요:", ["막대 그래프", "라인 그래프"])

# ----- 📈 스트리밍 데이터 시각화 -----
st.subheader("🔥 K-pop 스트리밍 랭킹 (단위: 백만)")

if chart_type == "막대 그래프":
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(df["가수"], df["스트리밍 수 (백만)"], color="dodgerblue")
    ax.set_ylabel("스트리밍 수 (백만)")
    ax.set_xlabel("가수")
    ax.set_title("K-pop 스트리밍 순위 (막대 그래프)")
    st.pyplot(fig)

elif chart_type == "라인 그래프":
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df["가수"], df["스트리밍 수 (백만)"], marker="o", linestyle="-", color="red")
    ax.set_ylabel("스트리밍 수 (백만)")
    ax.set_xlabel("가수")
    ax.set_title("K-pop 스트리밍 순위 (라인 그래프)")
    st.pyplot(fig)

# ----- 📜 데이터 테이블 -----
st.subheader("📋 전체 스트리밍 데이터")
st.dataframe(df)

# ----- 🎵 추가 정보 -----
st.sidebar.markdown("### 🎤 K-pop 스트리밍 현황")
st.sidebar.write("""
- 본 데이터는 가상의 스트리밍 순위입니다.
- 스트리밍 수치는 200~1000만 사이에서 랜덤 생성되었습니다.
- 차트를 선택하여 다양한 방식으로 데이터를 확인하세요.
""")

st.sidebar.markdown("📌 **제작: AI & 데이터 애널리틱스**")
