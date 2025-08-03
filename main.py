import streamlit as st

st.title("名前記憶アプリ")

if 'givenname' not in st.session_state:
    st.session_state.givenname =""

name = st.text_input("あなたの名前を入力してください")
if st.button("名前を記録"):
    st.session_state.givenname = name

st.write(f"記憶している名前:{st.session_state.givenname}")