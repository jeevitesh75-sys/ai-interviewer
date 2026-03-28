import streamlit as st
from groq_client import generate_questions
from prompt_builder import build_prompt
from formatter import format_output
from ui_components import royal_css, set_background
from auth import auth_page

# ---------------- AUTH ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    auth_page()
    st.stop()

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Interview Generator", layout="wide")

# ---------------- SETTINGS ----------------
with st.sidebar:
    st.markdown("## ⚙️ Settings")

    theme = st.radio("Theme", ["Dark", "Light"])
    language = st.selectbox("Language", ["English", "Hindi", "Telugu"])

    st.markdown("### 📞 Support")
    st.markdown(
        "[Contact Us (Google Form)](https://forms.gle/bHdqtavaw9gBWxMZ8)",
        unsafe_allow_html=True
    )

# ---------------- LANGUAGE ----------------
translations = {
    "English": {
        "questions": "Questions",
        "answers": "Answers",
        "generate": "Generate Questions"
    },
    "Hindi": {
        "questions": "प्रश्न",
        "answers": "उत्तर",
        "generate": "प्रश्न बनाएं"
    },
    "Telugu": {
        "questions": "ప్రశ్నలు",
        "answers": "సమాధానాలు",
        "generate": "ప్రశ్నలు సృష్టించండి"
    }
}

t = translations[language]

# ---------------- APPLY THEME ----------------
royal_css(theme)

# ---------------- HEADER ----------------
st.markdown("<div class='title'>AI Interview Generator</div>", unsafe_allow_html=True)

col1, col2 = st.columns([5, 2])

with col1:
    st.markdown(f"👤 Welcome, {st.session_state.get('current_user', 'User')}")

with col2:
    if st.button("Logout", key="logout_btn"):
        st.session_state.logged_in = False
        st.rerun()

# ---------------- BACKGROUND ----------------
uploaded_bg = st.file_uploader("Upload Background Image", type=["png", "jpg", "jpeg"])
set_background(uploaded_bg)

# ---------------- SEARCH ----------------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    role = st.text_input("🔍 Search Job Role")

    if st.button("🎤 Voice Search"):
        st.write("Voice search works in browser with mic")

# ---------------- ROLES ----------------
roles = [
    "Software Engineer", "Data Scientist", "AI Engineer",
    "Frontend Developer", "Backend Developer", "Full Stack Developer",
    "DevOps Engineer", "Cloud Engineer", "Cyber Security Analyst"
]

st.subheader("Select Job Role")

if "selected_role" not in st.session_state:
    st.session_state.selected_role = None

cols = st.columns(3)

for i, r in enumerate(roles):
    with cols[i % 3]:
        if st.button(r, key=f"role_{i}"):
            st.session_state.selected_role = r

if role:
    st.session_state.selected_role = role

selected_role = st.session_state.selected_role

# ---------------- CONFIG ----------------
if selected_role:
    st.markdown(f"### Selected Role: {selected_role}")

    num_q = st.slider("Number of Questions", 5, 20, 10)
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])

    st.markdown("### Question Distribution (%)")

    col1, col2, col3 = st.columns(3)

    with col1:
        one_line = st.slider("One-line", 0, 100, 40)

    with col2:
        one_word = st.slider("One-word", 0, 100, 30)

    with col3:
        coding = st.slider("Coding", 0, 100, 30)

    # ---------------- GENERATE ----------------
    if st.button(t["generate"], key="generate_btn"):

        prompt = build_prompt(
            selected_role,
            num_q,
            difficulty,
            one_line,
            one_word,
            coding
        )

        result = generate_questions(prompt)

        # DEBUG (remove later if needed)
        result = generate_questions(prompt)

        questions, answers = format_output(result)

        if not questions:
            st.error("No questions generated. Check API/format.")
        else:
            st.session_state.questions = questions
            st.session_state.answers = answers
            st.session_state.show_answers = False

# ---------------- DISPLAY ----------------
if "questions" in st.session_state:

    st.markdown(f"## ✨ {t['questions']}")

    for i, q in enumerate(st.session_state.questions):
        st.markdown(f"**{i+1}. {q}**")

    if st.button("Show Answers", key="show_ans_btn"):
        st.session_state.show_answers = True

# ---------------- ANSWERS ----------------
if st.session_state.get("show_answers"):

    st.markdown(f"## 💡 {t['answers']}")

    for i, a in enumerate(st.session_state.answers):
        st.markdown(f"{i+1}. {a}")