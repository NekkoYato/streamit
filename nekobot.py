import requests
import streamlit as st
from PIL import Image, ImageMath, ImageDraw, ImageFont
from validators.url import url
from telegraph import upload_file

st.markdown("<h1 style='text-align: center; color: white;'>OwO, Hi There!</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white; font-size: medium;'>Nekobot! web based implementation of nekobot api</h1>", unsafe_allow_html=True)
with st.expander("Kanna"):
  st.markdown("<h1 style='text-align: center; color: white; font-size: small;'>Write with Kanna!</h1>", unsafe_allow_html=True)
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
with st.expander("Pornhub Comment"):
  text = st.file_uploader("Enter the image you want to use!",type=['png', 'jpg','jpeg'])
  if text != None:
         xt = Image.open(text)
         xt.save("mp.png",optimize=True,quality=95)
         response = upload_file("mp.png")
         text1 = f"https://telegra.ph{response[0]}"
         text3 = st.text_input("Enter username!!")
         text2 = st.text_input("Enter the comment you want!")
         if text2 and text3 != "":    
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
      st.write("Try it duh!")

with st.expander("Threats"):
  tex = st.file_uploader("Enter the threat image you want to use!",type=['png', 'jpg','jpeg'])
  if tex != None:
         xt = Image.open(tex)
         xt.save("mp.png",optimize=True,quality=95)
         response = upload_file("mp.png")
         tex = f"https://telegra.ph{response[0]}"    
         r = requests.get(
             f"https://nekobot.xyz/api/imagegen?type=threats&url={tex}"
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
      st.write("Threatening...")
      
with st.expander("Who would win?"):
  text11 = st.file_uploader("Enter first image you want to use!",type=['png', 'jpg','jpeg'])
  if text11 != None:
       xt = Image.open(text11)
       xt.save("mp.png",optimize=True,quality=95)
       response = upload_file("mp.png")
       text11 = f"https://telegra.ph{response[0]}"
       text22 = st.file_uploader("Enter second image you want to use!",type=['png', 'jpg','jpeg'])
       if text22 != None:
         x = Image.open(text22)
         x.save("m.png",optimize=True,quality=95)
         resp = upload_file("m.png")
         text2 = f"https://telegra.ph{resp[0]}" 
         r = requests.get(
             f"https://nekobot.xyz/api/imagegen?type=whowouldwin&user1={text11}&user2={text22}"
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
      st.write("Competition?")

with st.expander("Baguette"):
  textt = st.file_uploader("Enter the image you want to use!",type=['png', 'jpg','jpeg'])
  if textt != None:
         xt = Image.open(textt)
         xt.save("mp.png",optimize=True,quality=95)
         response = upload_file("mp.png")
         texxt1 = f"https://telegra.ph{response[0]}"    
         r = requests.get(
             f"https://nekobot.xyz/api/imagegen?type=baguette&url={texxt1}"
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
      st.write("baguette ?")
with st.expander("Captcha"):
  temxt = st.file_uploader("Enter the captcha image you want to use!",type=['png', 'jpg','jpeg'])
  if temxt != None:
         xt = Image.open(temxt)
         xt.save("mp.png",optimize=True,quality=95)
         response = upload_file("mp.png")
         temxt1 = f"https://telegra.ph{response[0]}"
         temxt2 = st.text_input("Enter username!!")
         if temxt2 != "":    
             r = requests.get(
                 f"https://nekobot.xyz/api/imagegen?type=captcha&url={temxt1}&username={temxt2}"
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
with st.expander("Fake google search"):
  search = st.text_input("Add text for search bar!")
  result = st.text_input("Add text for result bar!")
  if search and result != "":
      t = "temp.jpg"
      a = urllib.request.urlretrieve("https://i.imgur.com/wNFr5X2.jpg",t)
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
with st.expander("Change my mind?"):
  text = st.text_input("Change my mind?\n")
  if text != '':
      r = requests.get(f"https://nekobot.xyz/api/imagegen?type=changemymind&text={text}"
  ).json()
      a = r.get("message")
      iurl = url(a)
      with open("temp.png", "wb") as f:
          f.write(requests.get(a).content)
      img = Image.open("temp.png").convert("RGB")
      st.image(img)
  else:
      st.write("Type something!!")
with st.expander("Shipping!"):
  taext1 = st.file_uploader("Enter first image you want to use!",type=['png', 'jpg','jpeg'])
  if taext1 != None:
       xt = Image.open(taext1)
       xt.save("mp.png",optimize=True,quality=95)
       response = upload_file("mp.png")
       taext1 = f"https://telegra.ph{response[0]}"
       taext2 = st.file_uploader("Enter second image you want to use!",type=['png', 'jpg','jpeg'])
       if taext2 != None:
         x = Image.open(taext2)
         x.save("m.png",optimize=True,quality=95)
         resp = upload_file("m.png")
         taext2 = f"https://telegra.ph{resp[0]}" 
         r = requests.get(
             f"https://nekobot.xyz/api/imagegen?type=ship&user1={taext1}&user2={taext2}"
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

with st.expander("Tweet!"):
  textt1 = st.text_input("Enter the username!\n")
  textt2 = st.text_input("What do you want to tweet?\n")
  if textt1 and textt2 != '':
      r = requests.get(
          f"https://nekobot.xyz/api/imagegen?type=tweet&text={textt2}&username={textt1}"
      ).json()
      a = r.get("message")
      iurl = url(a)
      with open("temp.png", "wb") as f:
          f.write(requests.get(a).content)
      img = Image.open("temp.png").convert("RGB")
      st.image(img)
  else:
      st.write("Type something!!")
