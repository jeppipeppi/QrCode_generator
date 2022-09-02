import qrcode
import colorama
import os
from colorama import init,Fore
init()
os.system("cls" or "clear")


data = input(Fore.BLUE + 'Data saved in QrCode: ')

qr = qrcode.QRCode(version = 1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'black', back_color = 'white')

path = 'output'
file_name = 'QrCode'

img.save(path + "/" + file_name + ".png")

print('QrCode got saved in output!')
