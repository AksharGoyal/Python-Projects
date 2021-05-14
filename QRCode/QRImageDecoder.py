# import the required modules
from pyzbar.pyzbar import decode
from PIL import Image

try:
    # get the image
    img = Image.open(input("Enter QR image path: "))
except:
    print("Wrong path given or file doesn't exist! Exiting!")
    exit()

try:
    # get the QRCode from the image
    result = decode(img)
    print(f'Data stored is: {(result[0][0]).decode("utf-8")}') # print the message
except:
    # Image didn't contain the QRCode
    print("Not a QRCode. Exiting!")
    exit()