import ctypes
import requests
import time
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
def changetext():
    response = requests.get("https://api.kanye.rest/text") 
    data = response.json() 
    img = Image.open("D:\projects\kanyepaper\Background.png")
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("arial.ttf",16)
    print(type(data))
    print(data)
    text = '"' +  data["quote"]+'"'
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((500, 450),data["quote"],(255,255,255),font=font)
    draw.text((540, 470),"~Kanye West",(255,255,255),font=font)
    img.save('D:\projects\kanyepaper\sample-out.png')
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "D:\projects\kanyepaper\sample-out.png" , 0)

#while(1):
changetext()
time.sleep(60)
