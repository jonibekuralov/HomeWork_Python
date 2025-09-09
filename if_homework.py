# # # # summa=float(input("Kartangizdagi summani kiriting:"))
# # # # summa1=float(input("Yechib olmoqchi bo'lgan summani kiriting:"))
# # # # if summa<summa1:
# # # #     print(f"Hisobingizda yetarli mablag' mavjud emas.")
# # # # elif summa1<5000:
# # # #     print(f"Minimal yechish summasi 5000 so'm")
# # # # else:
# # # #     print(f"Pul muvaffaqiyatli yechildi.")
# # #
# # # # mb=int(input("Oyiga qancha internet tarifidan foydalanasiz?"))
# # # # if mb<1024:
# # # #     print(f"Sizga 'Mini' tarifi mos keladi.")
# # # # elif 1024<mb<1024*5:
# # # #     print(f"Sizga 'Standard'tarifi mos keladi")
# # # # else:
# # # #     print(f"Sizga 'Unlimited tarifi mos keladi")
# # #
# # #
# # # talaba_0 = {
# # #     'ism':'jonibek',
# # #     'familiya':'uralov',
# # #     'yosh':22,
# # #     'fakultet':'kompyuter injenering',
# # #     'kurs':2
# # #     }
# # #
# # # print(talaba_0.items())
# # #
# # # for kalit, qiymat in talaba_0.items():
# # #     print(f"Kalit: {kalit}")
# # #     print(f"Qiymat: {qiymat} \n")
# #
# #
# # mahsulotlar = { # Do'kondagi mahsulotlar
# #     'olma':10000,
# #     'anor':20000,
# #     'uzum':40000,
# #     'anjir':25000,
# #     'shaftoli':30000
# #     }
# #
# # print(mahsulotlar.keys())
# # print('Do\'kondagi mahsulotlar:')
# # for mahsulot in mahsulotlar.keys():
# #     print(mahsulot.title())
# #
# # bozorlik = ['anor','uzum','non','baliq']
# # for mahsulot in mahsulotlar:
# #     if mahsulot in bozorlik:
# #         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
# #     else:
# #         print(f"Iltimos, do'koningizga {mahsulot} ham olib keling")
# #
# #
# # products = sorted(mahsulotlar)
# # print(products)
# # print("Do'konimizdagi mahsulotlar:")
# # for mahsulot in sorted(mahsulotlar):
# #     print(mahsulot.title())
# #
# # print(mahsulotlar.values())
# #
# # print('Mahsulot narxlari')
# # for mahsulot in mahsulotlar.values():
# #     print(mahsulot)
#
#
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'
#     }
#
# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in set(telefonlar.values()):
#     print(tel)


car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat'
        }

car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'korobka':'mexanika'
        }

car2 = {
'model':'gentra',
'rang':'qizil',
'yil':2019,
'narh':15000,
'km':20000,
'korobka':'mexanika'
}
