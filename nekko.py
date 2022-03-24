import streamlit as st
import requests
from PIL import Image
from validators.url import url
st.markdown(""" div.stButton > button:first-child {
background-color: #00cc00;color:white;font-size:20px;height:3em;width:50%;border-radius:10px 10px 10px 10px;
}
""", unsafe_allow_html=True)
col1,col2,col3=st.columns([0.3,1.2,0.3])
with col1:
 st.empty()
with col2:
 if st.button(“the notice you want to show”):
    st.markdown("<h1 style='text-align: center; color: white;'>Kanna!</h1>", unsafe_allow_html=True)
    st.title('Kanna Says!!')
    st.image("https://c.tenor.com/BAjY_lw4z3gAAAAd/kanna-eating.gif")
    text = st.text_input("What do you want kanna to say?\n")
    if text == '':
     st.write("Type something!!")
    else:
     r = requests.get(f"https://nekobot.xyz/api/imagegen?type=kannagen&text={text}"
     ).json()
     a = r.get("message")
     iurl = url(a)
     with open("temp.png", "wb") as f:
        f.write(requests.get(a).content)
     img = Image.open("temp.png").convert("RGB")
     st.image(img)
with col3:
 st.empty()
