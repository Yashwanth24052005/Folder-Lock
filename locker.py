import os
import pyotp
import shutil
from cryptography.fernet import Fernet

key = ""

enckey = bytes()

fernet = Fernet(enckey)

uri = pyotp.totp.TOTP(key).provisioning_uri(
	name='Folderv2',
	issuer_name='Fredrick')

os.chdir("..")

totp = pyotp.TOTP(key)


if "Locker" in os.listdir():
    if 'y' == input('Do you want to Lock this folder?'):
        shutil.make_archive("Locker",'zip',"Locker")
        with open('Locker.zip', 'rb') as file:
            original = file.read()
        
        encrypted = fernet.encrypt(original)

        with open('Locker.zip', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
        
        os.system('ren Locker.zip "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"')
        os.system('attrib +h +s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"')
        shutil.rmtree(os.path.join(os.getcwd(),"Locker"))
elif "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" in os.listdir():
    print("Folder is locked")
    while True:
        if (totp.verify(input(("Enter the Code : ")))):
            os.system('attrib -h -s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"')
            os.system('ren "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" Locker.zip')
            with open('Locker.zip', 'rb') as enc_file:
                encrypted = enc_file.read()
            
            decrypted = fernet.decrypt(encrypted)
            
            with open('Locker.zip', 'wb') as dec_file:
                dec_file.write(decrypted)

            shutil.unpack_archive('locker.zip','Locker','zip')
            os.remove("Locker.zip")
            print("Unlocked")
            break
        else:
            print("Wrong code try again")
else:
    os.mkdir("Locker")