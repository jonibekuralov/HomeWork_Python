# # cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# # cars.sort()
# # print(cars)
# #
# mehmonlar = ['Jonibek', 'Temurbek', 'Javlonbek', "O'tkirbek", 'Anvar', 'Bekzod']
# mehmonlar.sort()
# print("sorted() qaytargan ro'yxat:", sorted(mehmonlar)) #a-z
# print("sorted() qaytargan ro'yxat:", sorted(mehmonlar, reverse=True)) #z-a
#
# print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)
#
#
# ages = [12, 98, 34, 65, 34, 76, 11]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse=True))
#
#
# fruits = ['pear','banana','apple','watermelon','lemon']
# fruits.reverse()
# print(fruits)


# fruits = ['pear','banana','apple','watermelon','lemon','apricot']
# print("Elementlar soni:",len(fruits)) # len(fruits) ro'yxat uzunligini qaytaradi
#
#
# sonlar = list(range(0,10)) #
# print(sonlar)
#
# juft_sonlar = list(range(0,100,2))
# print(juft_sonlar)
#
# toq_sonlar = list(range(1,100,2))
# print(toq_sonlar)

# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)
#
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars[1:3]
# print(my_cars)
# print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
# print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi


# sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
# sonlar2 = sonlar[:] # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)

#tuple - o'zgarmas ro'yhat
tomonlar = (20, 30, 55.2)
# tomonlar.append(10)
# del tomonlar[2]
# tomonlar.insert(3, 33)
print(tomonlar[2])


toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
print(toys)
# Ro'yxatga o'zgartirishlar kiritamiz
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcqQueen'
toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
print(toys)
