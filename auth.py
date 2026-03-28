import streamlit as st
import json
import os

USER_FILE = "users.json"


# ---------------- SAVE USER ----------------
def save_user(username, password):
    users = load_users()
    users[username] = password
    with open(USER_FILE, "w") as f:
        json.dump(users, f)


# ---------------- LOAD USERS ----------------
def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, "r") as f:
        return json.load(f)


# ---------------- SIGNUP ----------------
def signup():
    st.markdown("<h2 style='color:gold;'>📝 Create Account</h2>", unsafe_allow_html=True)

    new_user = st.text_input("Create Username")
    new_pass = st.text_input("Create Password", type="password")

    if st.button("Sign Up"):
        users = load_users()

        if new_user in users:
            st.error("User already exists ❌")
        elif new_user == "" or new_pass == "":
            st.warning("Please fill all fields ⚠️")
        else:
            save_user(new_user, new_pass)
            st.success("Account created successfully ✅")


# ---------------- LOGIN ----------------
def login():
    st.markdown("<h2 style='color:gold;'>🔐 Login</h2>", unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        users = load_users()

        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.session_state.current_user = username
            st.success("Login Successful ✅")
            st.rerun()
        else:
            st.error("Invalid Credentials ❌")

# ---------------- MAIN AUTH ----------------
def auth_page():
    choice = st.radio("Select Option", ["Login", "Sign Up"])

    if choice == "Login":
        login()
    else:
        signup()