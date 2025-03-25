import os
import pyotp
import qrcode
from cryptography.fernet import Fernet


# Get the passphrase from the user
key = input("Enter a passphrase: ")

# Modify the value of key in locker.py
with open("locker.py", "r") as file:
    content = file.read()

enckey = Fernet.generate_key()

content = content.replace('enckey = bytes()', f'enckey = bytes({enckey})')
content = content.replace('key = ""', f'key = "{key}"')


with open("locker.py", "w") as file:
    file.write(content)

# Generate the TOTP URI and save it as a QR code
uri = pyotp.totp.TOTP(key).provisioning_uri(
    name='Folderv2',
    issuer_name='Fredrick'
)

print(uri)

qrcode.make(uri).save("qr.png")

os.system("pyarmor gen locker.py")

print("Delete the qr after Scanning")