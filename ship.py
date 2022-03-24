import requests
import streamlit as st
from PIL import Image
from validators.url import url
from telegraph import upload_file
text1 = st.file_uploader("Enter first image you want to use!",type=['png', 'jpg','jpeg'])
if text1 != None:
     xt = Image.open(text1)
     xt.save("mp.png",optimize=True,quality=95)
     response = upload_file("mp.png")
     text1 = f"https://telegra.ph{response[0]}"
     text2 = st.file_uploader("Enter second image you want to use!",type=['png', 'jpg','jpeg'])
     if text2 != None:
       x = Image.open(text2)
       x.save("m.png",optimize=True,quality=95)
       resp = upload_file("m.png")
       text2 = f"https://telegra.ph{resp[0]}"    
       x = Image.open(text2)
       x.save("m.png",optimize=True,quality=95)
       resp = upload_file("m.png")
       text2 = f"https://telegra.ph{resp[0]}"    
       r = requests.get(
           f"https://nekobot.xyz/api/imagegen?type=ship&user1={text1}&user2={text2}"
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
    st.write("Let's ship some people!")
