import streamlit as st
import requests
from PIL import Image
from validators.url import url
if st.button("Kanna!"):
    st.title('Kanna Says!!')
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
    with open("temp.png", "rb") as file:
     btn = st.download_button(
             label="Download image",
             data=file,
             file_name="temp.png.png",
             mime="image/png"
           )
else:
    st.write("Meow")
