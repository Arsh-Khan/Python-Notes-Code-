import qrcode
import os

img = qrcode.make("https://www.youtube.com/channel/UCPxls4le5pnXxEVsnjM8--g")

img.save("qr.png","PNG")
os.system("open qr.png")

#pip install pillow  -- dependency