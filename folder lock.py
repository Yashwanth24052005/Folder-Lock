import os
import pyAesCrypt
import pyotp
import base64
import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

# Buffer size for AES encryption
BUFFER_SIZE = 64 * 1024

# Generate or load a secret key for 2FA
if not os.path.exists("secret.key"):
    secret = pyotp.random_base32()
    with open("secret.key", "w") as f:
        f.write(secret)
else:
    with open("secret.key", "r") as f:
        secret = f.read()

# Generate QR code for Google Authenticator
uri = pyotp.totp.TOTP(secret).provisioning_uri(name="FolderLockApp", issuer_name="Secure Locker")
qr = qrcode.make(uri)
qr.save("2fa_qr.png")  # Saves QR code for scanning

# Function to encrypt files
def encrypt_folder():
    folder_path = filedialog.askdirectory()
    password = simpledialog.askstring("Password", "Enter encryption password:", show="*")

    if not folder_path or not password:
        messagebox.showwarning("Warning", "Please select a folder and enter a password.")
        return

    try:
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                encrypted_file = file_path + ".aes"
                pyAesCrypt.encryptFile(file_path, encrypted_file, password, BUFFER_SIZE)
                os.remove(file_path)  # Remove original file after encryption
        
        messagebox.showinfo("Success", "Folder encrypted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed: {e}")

# Function to decrypt files with 2FA
def decrypt_folder():
    folder_path = filedialog.askdirectory()
    password = simpledialog.askstring("Password", "Enter decryption password:", show="*")

    if not folder_path or not password:
        messagebox.showwarning("Warning", "Please select a folder and enter a password.")
        return

    # 2FA Verification
    totp = pyotp.TOTP(secret)
    otp_code = simpledialog.askstring("2FA Authentication", "Enter the OTP code from Google Authenticator:")

    if not totp.verify(otp_code):
        messagebox.showerror("Error", "Invalid OTP. Access Denied!")
        return

    try:
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if file_path.endswith(".aes"):
                decrypted_file = file_path.replace(".aes", "")
                pyAesCrypt.decryptFile(file_path, decrypted_file, password, BUFFER_SIZE)
                os.remove(file_path)  # Remove encrypted file after decryption
        
        messagebox.showinfo("Success", "Folder decrypted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {e}")

# GUI Setup
root = tk.Tk()
root.title("Secure Folder Locker")
root.geometry("400x300")

tk.Label(root, text="Scan this QR code in Google Authenticator", font=("Arial", 10)).pack(pady=5)
qr_img = tk.PhotoImage(file="2fa_qr.png")
qr_label = tk.Label(root, image=qr_img)
qr_label.pack(pady=5)

# Buttons
tk.Button(root, text="Encrypt Folder", command=encrypt_folder, bg="red", fg="white").pack(pady=10)
tk.Button(root, text="Decrypt Folder (with 2FA)", command=decrypt_folder, bg="green", fg="white").pack(pady=10)

root.mainloop()
