
import qrcode   #extension qrcode

datos = "https://www.asos.com/es/hombre/"

qr = qrcode.QRCode(
    version=1,  # Tamaño del QR Code (1-40)
    box_size=10,  # Tamaño de cada caja en el codigo qr
    border=5  # Tamaño del borde (en cajas)
)

qr.add_data(datos)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")

img.save("qrasos.png")
