# 1. Elektron Pochta Manzillarini Tekshirish:
# Email manzillar ro'yxati berilgan:
# pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]
# for sikli va string metodlari yordamida har bir email manzilida "@" belgisi
# bor-yo'qligini tekshiring: Agar bo'lmasa, "Noto'g'ri email: email_manzi" deb
# chiqaring

pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]
for email_manzi in pochtalar:
   if "@" not in email_manzi:
       print(f"Noto'g'ri email: {email_manzi}")

# Parol Kuchini Tekshirish:
# ○ Foydalanuvchilarning parollar ro'yxati berilgan (masalan,
# ["password123", "Qwerty!", "admin", "StrongPass1!"]).
# ○ for sikli va shart operatorlari yordamida har bir parolni tekshiring:
# ■ Agar uzunligi 8 dan kam bo'lsa, "Juda qisqa"
# ■ Agar raqam yoki maxsus belgilar bo'lmasa, "Kuchsiz parol"
# ■ Aks holda, "Kuchli parol"


parollar = ["password123", "Qwerty!", "admin", "StrongPass1!"]
for parol in parollar:
    if len(parol) < 8:
       print("Juda qisqa: ", parol)
    elif parol.isalnum():
        print("Kuchsiz parol: ", parol)
    else:
       print("Kuchli parol: ", parol)


# 3. Ob-havo Ma'lumotlarini Tahlil Qilish:
# ○ Bir hafta davomida kundalik haroratlar ro'yxati berilgan (masalan, [20,
# 22, 19, 24, 25, 23, 21]).
# ○ for sikli yordamida o'rtacha haroratni hisoblang va har bir kun uchun
# agar harorat 22 dan yuqori bo'lsa, "Iliq kun", aks holda "Salqin
# kun" deb chiqaring.


haroratlar = [20, 22, 19, 24, 25, 23, 21]
k = 0
for harorat in haroratlar:
    k = k + harorat
    if harorat >= 22:
       print("Iliq kun: ", harorat)
    else:
       print("Salqin kun: ", harorat)

print("O'rtacha harorat: ", int(k/len(haroratlar)), "gardus")


# 4. Restoran Buyurtmalari:
# ● Mavjud taomlar ro'yxati berilgan (masalan, ["Osh", "Shashlik", "Manti",
# “Lag’mon” ]).
# ● Foydalanuvchidan buyurtma kiritishni so'rang.
# ● for sikli yordamida foydalanuvchi kiritgan buyurtma mavjud taomlarga mos
# keladimi-yo'qligini tekshiring:
# ○ Agar mos kelsa, "Buyurtmangiz qabul qilindi" deb chiqaring.
# ○ Aks holda, "Kechirasiz, bunday taom yo'q" deb chiqaring.

taomlar = ["Osh", "Shashlik", "Manti", "Lag’mon"]
buyurtma = input("Buyurtma kiriting: ")
if buyurtma in taomlar:
   print("Buyurtmangiz qabul qilindi")
else:
   print("Kechirasiz, bunday taom yo'q")


# 5. Anketa Tahlili:
# ● Foydalanuvchilarning yoshlari ro'yxati berilgan (masalan, [16, 21, 17,
# 30, 25]).
# ● for sikli yordamida har bir foydalanuvchining yoshini tekshiring:
# ○ Agar yosh 18 dan kichik bo'lsa, "Yosh chegarasiga yetmagan"
# deb chiqaring.
# ○ Aks holda, "Xush kelibsiz" deb chiqaring.


yoshlar = [16, 21, 17, 30, 25]
for yosh in yoshlar:
    if yosh < 18:
       print("Yosh chegarasiga yetmagan")
    else:
       print("Xush kelibsiz")


# 6. Mobil Ilova Bildirishnomalari: Bildirishnomalar sarlavhalari ro'yxati berilgan
# xabarlar=["Yangi xabar", "Batareya past", "Yangilanish
# mavjud"]).
# for sikli yordamida agar sarlavha "Batareya past" bo'lsa, "Telefoningizni
# quvvatlang" deb print chiqaring.


# xabarlar = ["Yangi xabar", "Batareya past", "Yangilanish mavjud"]
# for xabar in xabarlar:
#     if xabar == "Batareya past":
#        print("Telefoningizni quvvatlang")
#





# 7. Fayllarni guruhlash:
# fayllar = [ “kitob.jpg”, “ko_jiguli.mp3”, “tabiat.jpg”, “malohat.mp3”, “iphone16.jpg”]
# musiqalar=[ ] va rasmlar=[ ] nomli listlar yarating. Fayllar ustida sikl aylantirib “.jpg”
# larni rasmlar listiga, “.mp3” larni musiqalar listiga qo’shing. Yordam: find() string
# metodi va append() list metodidan foydalaning.

fayllar = ["kitob.jpg", "ko_jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]
musiqalar = []
rasmlar = []
for fayl in fayllar:
    if fayl.find(".jpg") != -1:
       rasmlar.append(fayl)
    elif fayl.find(".mp3") != -1:
       musiqalar.append(fayl)
print(musiqalar)
print(rasmlar)