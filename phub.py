import requests
import streamlit as st
from PIL import Image, ImageMath
from validators.url import url
from telegraph import upload_file
text = st.file_uploader("Enter the image you want to use!")
if text != None:
    xt = Image.open(text)
    xt.save("mp.png")
    response = upload_file("mp.png")
    text1 = f"https://telegra.ph{response[0]}"
else:
    st.write("Upload some image!")
text3 = st.text_input("Enter username!!")
text2 = st.text_input("Enter the comment you want!")
if text1 and text2 and text3 != "":    
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=phcomment&image={text1}&text={text2}&username={text3}"
    ).json()
    a = r.get("message")
    iurl = url(a)
    with open("temp.png", "wb") as f:
        f.write(requests.get(a).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.png", "png")
    st.image(img)
else:
    st.write("well, try something interesting hehe")
