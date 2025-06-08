import random

elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
panjang_password = int(input("Masukkan panjang password: "))
password = ""
for i in range(panjang_password):
    password += random.choice(elements)
print("Password Anda adalah: ", password)
print("Selamat, password anda telah dibuat!")
