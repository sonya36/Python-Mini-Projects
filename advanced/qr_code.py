

import qrcode

# Data to be encoded in the QR code
data = "https://www.youtube.com/watch?v=XwPDxTBIRSc"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image to a file
img.save("scan_me.png")

print("QR Code generated and saved as qrcode.png")
