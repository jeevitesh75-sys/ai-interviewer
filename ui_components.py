import streamlit as st

def royal_css(theme="Dark"):
    if theme == "Dark":
        bg = "#000000"
        text = "white"
        box = "#111"
    else:
        bg = "#ffffff"
        text = "black"
        box = "#f5f5f5"

    st.markdown(f"""
    <style>

    .stApp {{
        background: {bg};
        color: {text};
    }}

    .title {{
        text-align: center;
        font-size: 48px;
        font-weight: bold;
        color: gold;
        text-shadow: 0 0 10px gold;
    }}

    .question-box {{
        background: {box};
        border-left: 5px solid gold;
        padding: 15px;
        margin: 10px 0;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(255,215,0,0.4);
    }}

    .answer-box {{
        background: {box};
        border-left: 5px solid goldenrod;
        padding: 15px;
        margin: 10px 0;
        border-radius: 10px;
    }}

    .stButton>button {{
        background: linear-gradient(45deg, gold, goldenrod);
        color: black;
        border-radius: 10px;
        box-shadow: 0 0 10px gold;
    }}

    </style>
    """, unsafe_allow_html=True)
import base64
import streamlit as st

def set_background(uploaded_file):
    if uploaded_file is not None:
        encoded = base64.b64encode(uploaded_file.read()).decode()

        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{encoded}");
                background-size: cover;
                background-position: center;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )    
st.markdown("""
<style>

.question-box:hover, .answer-box:hover {
    box-shadow: 0 0 20px gold;
    transform: scale(1.02);
    transition: 0.3s;
}

</style>
""", unsafe_allow_html=True)