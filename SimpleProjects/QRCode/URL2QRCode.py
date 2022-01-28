import qrcode # import the required module

# Enter the url to be converted
url = input("Enter URL to convert to QRCode: ")

#           Version 1               #
# This version is very simple way of converting
# img = qrcode.make(url)
# img.save('C:/Users/claim/Desktop/Programming/PYTHON/QRcode.png')

#           Version 2               #
#           This version helps      #
#                   in styling      #
qr = qrcode.QRCode(version = 1, box_size = 10, border = 5) # setup dimensions
qr.add_data(url)    # add the url
qr.make(fit=True)   # fits the background
img = qr.make_image(fill_color = 'blue', back_color = 'green')      # Image is produced
img.save('C:/Users/claim/Desktop/Programming/PYTHON/QRcode.png')    # Image with QRCode is saved