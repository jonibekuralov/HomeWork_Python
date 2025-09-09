# myset = {1,"apple", True, "banana",0, "cherry", 'apple', False}
# print(myset)
# print(len(myset))
# print(type(myset))
# # True == 1
# # False == 0
#
# thisset = set(("apple", "banana", "cherry", "banana")) # note the double round-brackets
#
# print(thisset)



# while True:
#     print("010001", end=" ")
#
# son = 1 # son ga 1 qiymatini beramiz
# while son<=5: # toki son 5 dan kichik yoki teng ekan...
#     print(son, end=' ') # son ni konsolga chiqaramiz,
#     # son = son+1 # songa 1 qo'shamiz.
#     son+=1

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)


print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)**2)
