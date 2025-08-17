from cryptography.fernet import Fernet
import os

key = Fernet.generate_key()

with open("key.key", "wb") as f:
    f.write(key)

f = Fernet(key)

dir_base = os.listdir()
print("Files in the current directory:")
print(dir_base)
print("Encrypting these files...")

ask = input("Are you sure...? (y/n)")

if ask == "n":
    exit()

for file in dir_base:
    if os.path.isfile(file):
        if file != "encrypt.py" and file != "key.key" and file != "decrypt.py":
            with open(file, "rb") as f_in:
                data = f_in.read()
            
            encrypted_data = f.encrypt(data)
            
            with open(file, "wb") as f_out:
                f_out.write(encrypted_data)

print("Encryption complete.")
print("Files encrypted successfully.")

