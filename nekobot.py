import streamlit as st
import requests
from PIL import Image
from validators.url import url
st.title("Hello there!")
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
