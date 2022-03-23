import requests
from urllib import request
import streamlit as st
from PIL import Image, ImageMath
import urllib3
from telegraph import upload_file
text = st.file_uploader("Enter the image you want to use!")
xt = Image.open(text)
xt.save("mp.jpg")
response = upload_file("mp.jpg")
text1 = f"https://telegra.ph{response[0]}"
text3 = st.text_input("Enter username!!")
text2 = st.text_input("Enter the comment you want!")
if text1 and text2 and text3 != "":    
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=phcomment&image={text1}&text={text2}&username={text3}"
    ).json()
    a = r.get("message")
    iurl = url(a)
    with open("temp.png", "wb") as f:
        f.write(request.get(a).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
else:
    st.write("well, try something interesting hehe")
