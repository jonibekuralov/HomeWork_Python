
"""
5. Taxmin qilish o'yinini simulyatsiya qiladigan dastur yarating.
Dastur 1 dan 100 gacha bo'lgan tasodifiy sonni yaratishi va
foydalanuvchidan raqamni taxmin qilishni so'rashi kerak.
Agar foydalanuvchi taxmini haqiqiy raqamdan yuqori bo'lsa, dastur "Juda baland!" va
foydalanuvchidan yana taxmin qilishni so'rang. Xuddi shunday, agar foydalanuvchining
taxmini haqiqiy raqamdan past bo'lsa, dastur "Juda past!" va foydalanuvchidan yana taxmin
qilishni so'rang. Dastur foydalanuvchidan to'g'ri raqamni topmaguncha taxmin qilishni so'rashi kerak.
"""

import random

def guess_game():
    opportunities = 10
    rand = random.randrange(1, 100)
    while opportunities > 0:
        num = int(input("son kiriting: "))
        if num == rand:
            print("Tabriklaymiz! to'g'ri javob")
            break
        elif num > rand:
            print("Biz o'ylagan son siz o'ylagan sondan kichik")
        elif num < rand:
            print("Biz o'ylagan son siz o'ylagan sondan katta")
        opportunities -= 1
    else:
        print("Imkonyatingiz tugadi!")
    return f"Bot taxmin qilgan son: {rand}"


print(guess_game())