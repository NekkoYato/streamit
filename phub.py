from http.client import REQUEST_ENTITY_TOO_LARGE
from urllib import request
import streamlit as st
from PIL import Image, ImageMath
import urllib3
import os
try:
    import telegraph
except ModuleNotFoundError:
    os.system("pip3 install telegraph")
text = st.file_uploader("Enter the image you want to use!")
response = upload_file(text)
text1 = f"https://telegra.ph{response[0]}"
text3 = st.text_input("Enter username!!")
text2 = st.text_input("Enter the comment you want!")
if text1 and text2 and text3 != "":    
    r = REQUEST_ENTITY_TOO_LARGE.get(
        f"https://nekobot.xyz/api/imagegen?type=phcomment&image={text1}&text={text2}&username={text3}"
    ).json()
    a = r.get("message")
    iurl = urllib3(a)
    with open("temp.png", "wb") as f:
        f.write(request.get(a).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
else:
    st.write("well, try something interesting hehe")
