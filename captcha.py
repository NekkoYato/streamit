import requests
import streamlit as st
from PIL import Image, ImageMath
from validators.url import url
from telegraph import upload_file
text = st.file_uploader("Enter the captcha image you want to use!",type=['png', 'jpg','jpeg'])
if text != None:
       xt = Image.open(text)
       xt.save("mp.png",optimize=True,quality=95)
       response = upload_file("mp.png")
       text1 = f"https://telegra.ph{response[0]}"
       text2 = st.text_input("Enter username!!")
       if text2 != "":    
           r = requests.get(
               f"https://nekobot.xyz/api/imagegen?type=captcha&url={text1}&username={text2}"
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
    st.write("Proving your humanity?")
