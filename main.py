# QRCode generator

# import qrcode.image.svg
def qrcodefunc(qrversion, qrboxsize, qrborder, qrdata, qrfilelocation, qrfillcolor, qrbackcolor, qrsave, savenow):
    import os
    import qrcode
    #Style information

    qr = qrcode.QRCode(
        version=qrversion,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=qrboxsize,
        border=qrborder,
    )
    qr.add_data(qrdata)
    qr.make(fit=True)

    img = qr.make_image(fill_color=str(qrfillcolor), back_color=str(qrbackcolor))

    # Create QR Code
    filelocation = qrfilelocation

    completename = os.path.join(filelocation, qrsave)

    if savenow:
        img.save(completename)


