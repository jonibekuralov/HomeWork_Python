# # dinamik
# a = 5
# b = 10.3
# c = 5+3j
# print(type(a))
# print(type(b))
# print(type(c))

# print(c)
# print(type(a))
# print(type(b))
#
# # statik
# a = 10
# b = "50"
#
# print(a+b)


# immutable - o'zgarmas
a = 3
print(a+5)
print(id(a))
a = 5
print(id(a))
print(a)

#mutable - o'zgaradi
# list
a = [1,2,3]
print(id(a))
a = [1,2,3,4]
# a.append(9)
print(id(a))
print(a)
# set
b = {5,3,"25"}
print(id(b))
b = {5,3,"25",4}
print(id(b))
print(b)
a=3
b=4
# inkroment
b+=3
b=b+3
b-=3
b=b-3

print(b)
print(a+b)