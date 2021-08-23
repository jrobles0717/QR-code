import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://github.com/jrobles0717')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="#56fca2")

img.save("github-jrobles.png")