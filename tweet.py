import streamlit as st
import requests
from PIL import Image
from validators.url import url
text1 = st.text_input("Enter the username!\n")
text2 = st.text_input("What do you want to tweet?\n")
if text1 and text2 != '':
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=tweet&text={text2}&username{text1}"
).json()
    a = r.get("message")
    iurl = url(a)
    with open("temp.png", "wb") as f:
        f.write(requests.get(a).content)
    img = Image.open("temp.png").convert("RGB")
    st.image(img)
else:
    st.write("Type something!!")
