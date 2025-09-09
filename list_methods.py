# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# # cars.sort()
# # print(cars)
# print(sorted(cars, reverse=True))
#
# ages = [12, 98, 34, 65, 34, 76, 11]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse=True))
#
# fruits = ['pear','banana','apple','watermelon','lemon']
# fruits.reverse()
# print(fruits)
#
# fruits = ['pear','banana','apple','watermelon','lemon']
# print("Elementlar soni:",len(fruits)) # len(fruits) ro'yxat uzunligini qaytaradi
#
# ism = "Ali"
# print(len(ism))
#
# sonlar = list(range(0,11)) #
# print(sonlar)
#
# sonlar2 = list(range(100)) #
# print(sonlar2)
#
# toq_sonlar = list(range(1,100,2))
# print(f"Toq sonlar:{toq_sonlar}")
#
# juft_sonlar = list(range(0,100,2))
# print(f"Juft sonlar:{juft_sonlar}")


# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)
#
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars[0:3] # 0-indeskdan boshlab 3-indeks element ajratib olamiz
# print(my_cars)
#
# print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
# print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi

# sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
# sonlar2 = sonlar[:] # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)

# tomonlar = (20, 30, 55.2)
# print(tomonlar)
#
# toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
# toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
#
# # Ro'yxatga o'zgartirishlar kiritamiz
# toys.append('dragon')
# toys.remove('bus')
# toys[1] = 'mcqueen'
#
# toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
# print(toys)


# i=0
# i=1
# i=2
# i=3
# .
# i=9

# for i in range(10):
#     # print(i)
#     print(f"{i}-salom")
#

# mehmonlar = ['Jonibek', 'Temurbek', 'Javlonbek', 'O\'tkirbek']
# for mehmon in mehmonlar:
#     print(mehmon)

# mehmonlar = ['Jonibek', 'Temurbek', 'Javlonbek', 'O\'tkirbek']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20-Mart kuni oshga taklif qilamiz")
#
#     print("Hurmat bilan, Palonchiyevlar oilasi")

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")
#
#
# sonlar_kvadrati =[] # bo'sh ro'yxat yaratamiz
# for son in sonlar:  # sonlar dagi har bir son uchun
#     sonlar_kvadrati.append(son**2) # uning kv.ni hisoblab, sonlar_kvadrati ga yuklaymiz
#
# print(sonlar)
# print(sonlar_kvadrati)


# dostlar = [] # bo'sh ro'yxat
# print("5 ta eng yaqin do'stingiz kim?")
# for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
#     dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
# print(dostlar)

# avtolar = ['audi','bmw','volvo','kia','hyundai']
# for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
#     if avto != 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
#         print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
#     else: # aks holda ...
#         print(avto.title()) # avto nomini faqat birinchi harfini katta bilann yoz.


# ism = input('Ismingiz nima?:') # Foydalanuvchi ismini so'raymiz
# if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa ...
#     print(f"Uzr, {ism.title()} biz Alini kutayapmiz.") # quyidagi xabar chiqadi
# else:
#     print("Salom, Ali")
#
#
# javob = float(input("12x6 nechiga teng?>>>"))
# if javob!=72:
#     print("Javob xato!")


# login = input("Yangi login tanlang:")
# if len(login)<=5: # login uzunligini tekshiramiz
#     print("Login 5 harfdan ko'proq bo'lishi shart!")
# else:
#     print("Login qabul qilindi")
#
#
# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")
#
#
# x, y = 25, 50 # x=25 va y=50
# print("x>y") if x>y else print("x<y")


# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# elif yosh<65:
#     price = 10000
# elif yosh>=65:
#     price = 8000
# print(f"Sizga kirish {price} so'm")

# kun = input("Bugun nima kun?>>>")
#
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugun dam olish kuni.')
# else:
#     print('Bugun ish kuni.')

# Mantiqiy qo'shish'
# 0 or 0 = 0
# 0 or 1 = 1
# 1 or 0 = 1
# 1 or 1 = 1
# Mantiqiy ko'paytirish'
# 0 and 0 = 0
# 0 and 1 = 0
# 1 and 0 = 0
# 1 and 1 = 1


#  not 1 = 0
# not 0 = 1

# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
#     print("Uyda dam olamiz!")


# narh = 15000  # mijoz 15 so'mga ovqat oldi
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
# # Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
# if choy:  # agar choy olsa
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:  # agar salat olsa
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:  # agar non olsa
#     print("Mijoz non oldi.")
#     narh = narh + 2000
# if kompot:  # agar kompot olsa
#     print("Mijoz kompot oldi.")
#     narh = narh + 5000
# if assorti:  # agar assorti olsa
#     print("Mijoz assorti oldi.")
#     narh = narh + 15000
#
# print(f"Jami {narh} so'm")


menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["somsa"]

if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q")
else: # agar ro'yxat bo'sh bo'lsa
    print("Savatchangiz bo'sh!")
