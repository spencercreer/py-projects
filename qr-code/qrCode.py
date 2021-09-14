import qrcode

def createQrCode(data, box_size, border, color, background_color):
    data = data

    qr = qrcode.QRCode(version = 1, box_size = box_size, border = border)

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color = color, back_color = background_color)

    img.save('C:/Users/spenc/Documents/coding/01-github/python-projects/qr-code/2_qrcode.png')

myQrCode = {
    'data': 'https://github.com/spencercreer',
    'box_size': 10,
    'border': 5,
    'color': 'black',
    'background_color': 'yellow',
}

createQrCode(**myQrCode)