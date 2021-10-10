import pyqrcode
import png
from pyqrcode import QRCode
import sys

if len(sys.argv) != 2:
    print("Use: python3 app.py <text>")
else:
    text = sys.argv[1]
    file_name = text.replace("/", "-")
    file_name = file_name.replace(":", "-")
    file_name = file_name.replace(".", "-")
    print(text)
    qr = pyqrcode.create(text)
    qr.png(file_name + ".png", scale=8)
    print(dir(qr))
    