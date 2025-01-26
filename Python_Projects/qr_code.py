# import pyqrcode

# from pyqrcode import QRCode

# a  = input("Enter Url:")
# b = pyqrcode.create(a)

# b.svg("q1.svg",scale=10)


import pyqrcode

from pyqrcode import QRCode

a = input("Enter Url :")

b = pyqrcode.create(a)

b.svg("mail.svg",scale = 8)