import qrcode

# making the QR Code
img = qrcode.make("https://docs.google.com/forms/d/e/1FAIpQLSdfj6yuP1FFBPjPSocwBfeAW51G-0K-qdXBDLqTr5jjXSJZ_w/viewform?usp=sf_link")
# saving the QR Code in an image
img.save("Tutorias-Diana.png")
