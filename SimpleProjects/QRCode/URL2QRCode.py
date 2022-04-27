import qrcode # import the required module

# Enter the url to be converted
url = input("Enter URL to convert to QRCode: ")
# out = r'C:\Users\claim\Desktop\Programming\PY\SimpleProj\QRCode\QRcode.png' # Can be anything

#           Version 1               #
# This version is very simple way of converting
# img = qrcode.make(url)
# img.save(out)

#           Version 2               #
#           This version helps      #
#                   in styling      #
qr = qrcode.QRCode(version = 1, box_size = 5, border = 5) # setup dimensions
qr.add_data(url)    # add the url
qr.make(fit=True)   # fits the background
img = qr.make_image(fill_color = 'blue', back_color = 'yellow') # Image is produced of particular design
img.save(out)    # Image with QRCode is saved
print('QRCode is created!')
