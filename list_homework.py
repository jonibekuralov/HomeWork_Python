# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# narxlar = [12000, 15000, 64000, 45654]
# sonlar = ['bir', 'ikki', 3,4,5]

# clear() - ro'yhatdagi barcha elementlarni o'chiradi
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# print(mevalar.clear())
#
# narxlar = [12000, 15000, 64000, 45654]
# print(narxlar.clear())
#
# sonlar = ['bir', 'ikki', 3,4,5]
# print(sonlar.clear())


# copy() - Ro'yxatning nusxasini qaytaradi
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# a = mevalar.copy()
# print(type(a))
# a = a.append("uzum")
# print(a)
# print(mevalar)

#
# narxlar = [12000, 15000, 64000, 45654]
# print(narxlar.copy())
#
# sonlar = ['bir', 'ikki', 3,4,5]
# print(sonlar.copy())


# count() - Belgilangan qiymat bilan elementlar sonini qaytaradi
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik",'anjir']
# print(mevalar.count('anjir'))
#
# narxlar = [12000, 15000, 64000, 45654, 64000, 45654, 64000, 45654]
# print(narxlar.count(64000))
#
# sonlar = ['bir', 'ikki', 3,4,5]
# print(sonlar.count(3))


# extend() - Joriy ro'yxatning oxiriga ro'yxat elementlarini (yoki har qanday takrorlanadigan) qo'shing
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# sonlar = ['bir', 'ikki', 3, 4, 5]
# mevalar.extend(sonlar)
# print(mevalar)
#
# narxlar = [12000, 15000, 64000, 45654]
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# narxlar.extend(mevalar)
# print(narxlar)
#
# a = [11,2,3,45]
# b = ["o'n", 'ikki', 'uch']
# a.extend(b)
# print(a)


# index() - Belgilangan qiymat bilan birinchi elementning indeksini qaytaradi
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# print(mevalar.index('anjir'))
# #
# narxlar = [12000, 15000, 64000, 45654]
# print(narxlar.index(12000))
#
# sonlar = ['bir', 'ikki', 3,4,5]
# print(sonlar.index(4))


# pop() - Belgilangan holatda elementni olib tashlaydi
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# mevalar.pop(1)
# print(mevalar)
#
# narxlar = [12000, 15000, 64000, 45654]
# narxlar.pop(3)
# print(narxlar)
#
# sonlar = ['bir', 'ikki', 3,4,5]
# sonlar.pop(4)
# print(sonlar)


# reverse() - Ro'yxat tartibini o'zgartiradi
# mevalar = ['olma', 'anjir', 'shaftoli']
# mevalar.reverse()
# print(mevalar)
# narxlar = [12000, 15000, 64000, 45654]
# narxlar.reverse()
# print(narxlar)
#
# sonlar = ['bir', 'ikki', 3,4,5]
# sonlar.reverse()
# print(sonlar)


# sort() - Ro'yxatni tartiblaydi
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# mevalar.sort()
# print(mevalar)
#
# narxlar = [12000, 15000, 64000, 45654]
# narxlar.sort()
# print(narxlar)
#
# sonlar = ['bir', 'ikki', 'uch', "to'rt"]
# sonlar.sort()
# print(sonlar)
