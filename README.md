Folder Lock
A simple Python-based GUI application to lock and unlock folders using Windows attrib commands. This tool provides basic folder hiding functionality but does not offer strong security encryption.

Features
Hide a folder (lock) using attrib +h +s

Unhide a folder (unlock) using attrib -h -s

Simple GUI with folder selection and password input

Built using tkinter

Prerequisites
Windows OS (since attrib is a Windows-specific command)

Python 3.x installed

Installation
Clone the repository:

git clone https://github.com/yourusername/folder-lock.git
cd folder-lock
Install required dependencies (if any):

pip install tk
Run the script:

python folder_lock.py
Usage
Open the application.

Select a folder to lock/unlock.

Enter a password (currently not used for authentication, only for UI purposes).

Click "Lock Folder" to hide the folder.

Click "Unlock Folder" to unhide the folder.

Security Warning ⚠️
This script does not provide strong security:

The password is not actually used to encrypt or protect the folder.

The attrib command only hides the folder; it can be revealed easily.

A more secure approach would involve NTFS permissions or encryption.

Future Enhancements
Implement password verification.

Improve security using NTFS permissions (icacls).

Add encryption for stronger protection.

License
This project is licensed under the MIT License. Feel free to modify and improve it!

Note: This is a basic demonstration and should not be used for sensitive data protection.
