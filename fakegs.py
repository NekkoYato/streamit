import streamlit as st
import requests
from PIL import Image, ImageDraw, ImageFont
from validators.url import url
from io import BytesIO
search = st.text_input("Add text for search bar!")
result = st.text_input("Add text for result bar!")
if search and result != "":
    a = "https://i.imgur.com/wNFr5X2.jpg"
    response = requests.get(a)
    a = Image.open(BytesIO(response.content))
    with open("temp.jpg", "wb") as f:
        f.write(requests.get(a).content)
    img = Image.open("temp.jpg")
    drawing = ImageDraw.Draw(img)
    blue = (0, 0, 255)
    black = (0, 0, 0)
    font1 = ImageFont.truetype("resources/ProductSans-BoldItalic.ttf", 20)
    font2 = ImageFont.truetype("resources/ProductSans-Light.ttf", 23)
    drawing.text((450, 258), result, fill=blue, font=font1)
    drawing.text((270, 37), search, fill=black, font=font2)
    img.save("temp.jpg")
    st.image(img)
else:
    st.write("Type something perhaps?")
