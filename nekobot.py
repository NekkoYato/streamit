import streamlit as st
st.markdown("<h1 style='text-align: center; color: white;'>OwO, Hi There!</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white; font-size: medium;'>Nekobot! web based implementation of nekobot api</h1>", unsafe_allow_html=True)
m = st.markdown("""
<style>
div.stButton > button:first-child { 
color: #4F8BF9;
border-radius: 20%;
backgroud-color: #00ff00;
height: 3em;
width: 3em; 
}
</style>""", unsafe_allow_html=True)

b = st.button("test")
if b:
  st.write("Zamn")
else:
  st.write("")
