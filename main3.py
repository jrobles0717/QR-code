import qrcode

img = qrcode.make("https://docs.google.com/forms/d/e/1FAIpQLSdfj6yuP1FFBPjPSocwBfeAW51G-0K-qdXBDLqTr5jjXSJZ_w/viewform?usp=sf_link")
# img.save("/Users/jrobles/Documents/QR Code/code.jpg")
print("the type of image is: ",type(img))
img.save("Tutorias-Diana.png")
# img.save("some_file.svg")
# with open('myfile.png', 'wb') as f:
#     img.save(f)
