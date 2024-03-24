import random
print("Parola Uzunluğunu Sayı Şeklinde Yazın")
bot = int(input("Kaç Harf Veya Rakamlı Olsun"))
bot1 = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
şifre = ""


for i in range(bot):
    şifre += random.choice(bot1)

print(şifre)
