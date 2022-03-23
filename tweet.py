import streamlit as st
import requests
from PIL import Image
from validators.url import url
text = st.text_input("What to tweet with trump's twitter?\n")
if text == '':
    st.write("Type something!!")
else:
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}"
).json()
    a = r.get("message")
    iurl = url(a)
    with open("temp.png", "wb") as f:
        f.write(requests.get(a).content)
    img = Image.open("temp.png").convert("RGB")
    st.image(img)
