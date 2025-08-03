import streamlit as st

st.title("ユーザー情報入力")

if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'grade' not in st.session_state:
    st.session_state.grade = ""
if 'hobbies' not in st.session_state:
    st.session_state.hobbies = ""

name = st.text_input("名前")
grade = st.selectbox("学年",
    ["","小学5年","小学６年","中学１年","中学2年","中学3年"])
hobbies = st.multiselect("趣味",
    ["読書","スポーツ","ゲーム","音楽","絵画","その他"])

if st.button("情報を保存"):
    st.session_state.user_name = name
    st.session_state.grade = grade
    st.session_state.hobbies = hobbies
    st.success("情報を保存しました")
