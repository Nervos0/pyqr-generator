
# QR CODE GENERATOR
# Author: https://github.com/Nervos0
# Version: 0.1

# Importing libraries

import pyqrcode                 #pip install pyqrcode
import png                      #pip install pypng
from pyqrcode import QRCode


# QR Code generation

url=input("[*] Enter the URL> ")    # Enter the URL which represents the QR code
qr=pyqrcode.create(url)             # Generate QR code
qr.png('myqr.png', scale = 6)       # Save the qr in "myqr.png"
