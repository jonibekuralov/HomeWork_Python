# a= {1, 2, 3}
# a.add(5)#yangi element qoshadi (agar bola gan bolsa)
# print(a)
#
# #clear()- set ichidagi barcha elementlarni ochiradi
# a= {1, 2, 3}
# # b= {4, 5, 6}
# c= a.clear()
# a.add(1)
# print(a)
#
# #union()- set ichidagi elementlarni birbiriga qoshib yuboradi
# a= {1, 2, 3}
# b= {5,6,7}
# b=a.union(b)
# print(b)
#
# #intersection()-ikkita set ichidagi elementni qidiradi (5)
# a= {5,6, 2, 3}
# b= {5,6,7}
# d=b.intersection(a)
# print(d)

# # difference()-w3schools dagi manosina chunmadim manimcha aichindagi eleementlani b ga otiri baradi
# a= {1, 2, 3,5,7}
# b= {5,6,7,1}
# e=a.difference(b)
# print(e)
#
# #symmetric_difference()-ikkkala element birlashmasini oz ichiga oladi
# a= {1, 2, 3,5}
# b= {5,6,7}
# f = a.symmetric_difference(b)
# print(f)
#
# #update()-Agar ikkala to'plamda ham element mavjud bo'lsa, yangilangan to'plamda ushbu elementning faqat bitta ko'rinishi mavjud bo'ladi.
# a= {1, 2,5, 3}
# b= {5,6,7,9}
# # b.clear()
# b.update(a)
# print(b)
#
# #discard()- korsatilgan elementni olib tashlaydi agar korsatilgan element topolmasa error bermaydi
# a= {1, 2,6,8,1,0}
# # b= {5, 6, 7}
# a.discard(6)
# print(a)
#
# #remove()- agar berilgan eelementni topolmasa error qaytaradi
# a={4,1, 2, 3}
# a.remove(4)
# print(a)

#issubset()-set ichida korsatilgan element mavjud bolsa True agar mavjud bolmasa False
# a={"salom dunyo"}
# b={"salom dunyo",5,0,1,2}
# l= a.issubset(b)
# print(l)
#
# #issuperset()- set ichiga korsatilgan element mavjud bolsa True agr vajud bolmasa False
# k= b.issuperset({1,2})
# print(k)

#
# #isdisjoint()-ikkala to'plamda elementlardan hech biri mavjud bo'lmasa, True qiymatini aks holda u False qiymatini qaytaradi.
# a={1,2,3,4,5}
# b={6,7}
# j= a.isdisjoint(b)
# print(j)
#
#pop()- set ichidagi birinchi elementni olib tashlaydi
# a={1,2,3,4,5}
# b={"banana","apple","shaftoli"}
# print(b)
# a.pop()
# b.pop()
# print(a,b)

# a = {'a', 'b', 'c',"f"}
# b = {'b',"f", 'c', 'd'}
# c = {'c', 'f', 'g'}
# print(a & b & c)


# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#
# while True: # abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break # tsiklni to'xtatish
#     else:
#         print(float(qiymat)**2)
#
#
# sonlar = list(range(1,1000))
# for son in sonlar:
#     if son == 10: # son 5 ga teng bo'lsa kod to'xtaydi
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")

# ismlar = []
#
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break
#
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())


# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)  # ism kalit, yosh qiymat
#
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/no)")
#     if javob == "no":
#         ishora = False
#
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")


# cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
#     cars.remove('nexia') # nexia ni ro'yxatdan olib tashla
# print(cars)
#
# talabalar = ['jonibek', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho
#
# print(baholangan_talabalar)


i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("sikl tugadi")