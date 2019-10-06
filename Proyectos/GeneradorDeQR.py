pip install qrcode[pil]

Sleep 2

import qrcode

Qr = qrcode.make("Hola Chunche")
Qr.save('chuncheQR.png')


# creacion de qr completo

import qrcode

qr = qrcode.QRCode(
 version=1,
     error_correction=qrcode.constants.ERROR_CORRECT_H,
 box_size=5,
 border=5
)

# datos de entrada que quiere en tienda
qr_data='welcome to simply python'

#add data

qr.add_data(qr_data)
qr.make(fit=True)

# creacion de la imagen

Img = qr.make_image(fill_color='blue', back_color='white')

# guardar imagen

Img.save('Chunche95.png')
