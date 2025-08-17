from cryptography.fernet import Fernet
import os

key = None

with open("key.key", "rb") as f:
    key = f.read()

f = Fernet(key)

dir_base = os.listdir()
print("Decrypting files in the current directory:")
print(dir_base)
print("Decrypting files...")


ask = input("Are you sure...? (y/n)")

if ask == "n":
    exit()

for file in dir_base:
    if os.path.isfile(file):
        if file != "encrypt.py" and file != "key.key" and file != "decrypt.py":
            with open(file, "rb") as f_in:
                encrypted_data = f_in.read()
            decrypted_data = f.decrypt(encrypted_data)
            with open(file, "wb") as f_out:
                f_out.write(decrypted_data)

print("Decryption complete.")
print("Files decrypted successfully.")
