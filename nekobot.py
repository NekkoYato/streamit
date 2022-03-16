import streamlit as st
import requests
from PIL import Image, ImageDraw, ImageFont
from validators.url import url
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
    
search = st.text_input("Add text for search bar!")
result = st.text_input("Add text for result bar!")
if search and result !="":
    img = Image.open("resources/fakegs.jpg")
    drawing = ImageDraw.Draw(img)
    blue = (0, 0, 255)
    black = (0, 0, 0)
    font1 = ImageFont.truetype(font="resources/ProductSans-BoldItalic.ttf", size=20)
    font2 = ImageFont.truetype(font="resources/helpers/styles/ProductSans-Light.ttf", size=23)
    drawing.text((450, 258), result, fill=blue, font=font1)
    drawing.text((270, 37), search, fill=black, font=font2)
    img.save("temp.jpg")
    st.image(img)
else:
    st.write("Maybe type something?")
