import qrcode
import os

name = "Arsh Khan"
img = qrcode.make(name)
img.save("qr_name.png","PNG")
os.system("open qr_name.png")
