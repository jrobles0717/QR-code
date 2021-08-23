import pyqrcode
import os, shutil

title = input("Give your QR code a title! >>")
text = input("What would you like the QR Code to say? >>")

file_name_svg = title + ".svg"
file_name_png = title + ".png"

url = pyqrcode.create(text)

url.svg(file_name_svg, scale=8)
url.png(file_name_png, scale=10)

os.mkdir(fr"/Users/jrobles/Documents/{title}")

shutil.move(f"{file_name_png}", fr"Macintosh HD:/Users/jrobles/Documents/{title}")
shutil.move(f"{file_name_svg}", fr"Macintosh HD:/Users/jrobles/Documents/{title}")
