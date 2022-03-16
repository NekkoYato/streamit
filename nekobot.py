import streamlit as st
import requests
from PIL import Image
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
if search and result == "":
    st.write("Maybe write something?")
else:
    imgurl = "https://i.imgur.com/wNFr5X2.jpg"
    with open("./temp/temp.jpg", "wb") as f:
        f.write(requests.get(imgurl).content)
    img = Image.open("./temp/temp.jpg")
    drawing = ImageDraw.Draw(img)
    blue = (0, 0, 255)
    black = (0, 0, 0)
    font1 = ImageFont.truetype("resources/ProductSans-BoldItalic.ttf", 20)
    font2 = ImageFont.truetype("resources/helpers/styles/ProductSans-Light.ttf", 23)
    drawing.text((450, 258), result, fill=blue, font=font1)
    drawing.text((270, 37), search, fill=black, font=font2)
    img.save("./temp/temp.jpg")
    st.image(img)
