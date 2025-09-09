# # # capitalize() -
# # laptop = "My laptop is upgrade"
# # laptop_1 = laptop.capitalize()
print (laptop_1)
# #
# # market = "Sales are booming in the market"
# # market = market.capitalize()
# # print (market)
# #
# # book = "Today I read a new book"
# # book = book.capitalize()
# # print (book)
# #
# # # casefold -
# # python = "PYTHON IS FUN!"
# # python = python.casefold()
# # print(python)
# #
# # developer = "I am a Python developer!"
# # developer= developer.casefold()
# # print(developer)
# #
# #
# # hello = "HELLO, HOW ARE YOU?"
# # hello = hello.casefold()
# # print(hello)
# #
# # lowercase = "CASEFOLD MAKES TEXT LOWERCASE!"
# # lowercase = lowercase.casefold()
# # print(lowercase)
# #
# #
# # hello = "Hello"
# # hello = hello.center(10, "*")
# # print(hello)
# #
# # apple = "apple"
# # apple = apple.center(15)
# # print(apple)
# #
# # world = "world"
# # world = world.center(12, "-")
# # print(world)
# #
# # book = "I read books. Reading books is very useful. Books are a source of knowledge."
# # book = book.lower().count("book")
# # print(book)
# #
# # cat = "The cat chased the cat because the cat was curious."
# # cat = cat.count("cat")
# # print(cat)
# #
# # apple = "I like apples but not pineapple"
# # apple = apple.count("apple")
# # print(apple)
# #
# #
# # name = "what is your name"
# # name = name.encode()
# # print(name)
# #
# # weather = "The weather is nice today"
# # weather = weather.encode()
# # print(weather)
# #
# # read = "She is reading a newspaper"
# # read = read.encode()
# # print(read)
# #
# # learning = "I am learning Python"
# # learning= learning.endswith("Python")
# # print(learning)
# #
# # weather = "It is raining today"
# # weather = weather.endswith("sunny")
# # print(weather)
# #
# #
# # sentence = "This sentence ends with a question?"
# # x = sentence.endswith("?")
# # print(sentence)
# #
# # letters = "A\tB\tC"
# # letters = letters.expandtabs(4)
# # print(letters)
# #
# # txt = "Name\tAge\tCity"
# # x = txt.expandtabs(8)
# # print(x)
# #
# # txt = "Hello\tWorld"
# # x = txt.expandtabs(3)
# # print(x)
# #
# # txt = "I am learning Python programming."
# # x = txt.find("Python")
# # print(x)
# #
# # txt = "She sells seashells by the seashore."
# # x = txt.find("sea")
# # print(x)
# # txt = "Good morning!"
# # x = txt.find("evening")
# # print(x)
# #
# # txt = "The temperature is {temp:.1f} degrees Celsius."
# # print(txt.format(temp=36.6))
# #
# # txt = "Your balance is ${balance:.2f}."
# # print(txt.format(balance=1234.5))
# #
# # txt = "I ran {distance:.3f} kilometers today."
# # print(txt.format(distance=5))
# #
# # info = {"city": "Tashkent", "country": "Uzbekistan"}
# # txt = "I live in {city}, {country}."
# # print(txt.format_map(info))
# #
# # person = {"first": "shaxruza", "last": "otanazarova"}
# # txt = "My name is {first} {last}."
# # print(txt.format_map(person))
# #
# # data = {"ism": "shaxruza", "yosh": 18}
# # txt = "Salom, mening ismim {ism} va men {yosh} yoshdaman."
# # print(txt.format_map(data))
# #
# # txt = "Python programming is fun."
# # x = txt.index("programming")
# # print(x)
# #
# # # txt = "Good morning!"
# # # x = txt.index("evening")
# # # print(x)
# #
# # txt = "Hello, welcome to my world."
# # x = txt.index("welcome")
# # print(x)
# #
# # txt = "Python3"
# # print(txt.isalnum())
# #
# # txt = "Hello World"
# # print(txt.isalnum())
# #
# # txt = "123456"
# # print(txt.isalnum())
# #
# # txt = "HelloWorld"
# # print(txt.isalpha())
# #
# # txt = "Python3"
# # print(txt.isalpha())
# #
# # txt = "OpenAI"
# # print(txt.isalpha())
# #
# # txt = "Café"
# # print(txt.isascii())
# #
# # txt = "123456"
# # print(txt.isascii())
# #
# # txt = "Dunyo123"
# # print(txt.isascii())
# #
# # number = "56789"
# # print(number.isdecimal())
# #
# # number = "12.34"
# # print(number.isdecimal())
# #
# # number = "987654"
# # print(number.isdecimal())
# #
# #
# # txt = "12345"
# # print(txt.isdigit())
# #
# # txt = "1234a"
# # print(txt.isdigit())
# #
# # txt = "987654"
# # print(txt.isdigit())
# #
# # txt = "my_var"
# # print(txt.isidentifier())
# #
# # txt = "2cool"
# # print(txt.isidentifier())
# #
# # txt = "_private"
# # print(txt.isidentifier())
# #
# # txt = "python programming"
# # print(txt.islower())
# #
# # txt = "12345!"
# # print(txt.islower())
# #
# # txt = "hello world 123"
# # print(txt.islower())
# #
# # txt = "123456"
# # print(txt.isnumeric())
# #
# # txt = "12.34"
# # print(txt.isnumeric())
# #
# # txt = "2025"
# # print(txt.isnumeric())
# #
# # txt = "123abc"
# # print(txt.isnumeric())
# #
# # txt = "Ⅻ"
# # print(txt.isnumeric())
# #
# # txt = "56.78"
# # print(txt.isnumeric())
# #
# # myList = ["Apple", "Banana", "Pear"]
# # x = ", ".join(myList)
# # print(x)
# #
# # myTuple = ("sevinch", "shukurjan", "shoxruza")
# # x = " and ".join(myTuple)
# # print(x)
# #
# # words = ("Today", "the", "weather", "is", "good")
# # x = " ".join(words)
# # print(x)
# #
# # animal = "dog"
# # x = animal.ljust(10)
# # print(animal, "is very friendly.")
# #
# # animal = "cat"
# # animal = animal.ljust(8)
# # print(animal, "is a lovely pet.")
# #
# # txt = "car"
# # x = txt.ljust(8)
# # print(x, "is fast.")
# #
# # txt = "\n\nHello"
# # x = txt.lstrip()
# # print("Greeting:", x)
# #
# # txt = "    cat   "
# # x = txt.lstrip()
# # print("Animal:", x)
# #
# # txt = "\n\nHello"
# # x = txt.lstrip()
# # print("Greeting:", x)
# #
# # txt = "Apple and Banana"
# # mytable = str.maketrans("AB", "XY")
# # print(txt.translate(mytable))
# #
# #
# # txt = "I could eat bananas all day"
# # x = txt.partition("bananas")
# # print(x)
# #
# # txt = "It is raining today"
# # x = txt.replace("raining", "sunny")
# # print(x)
# #
# # txt = "I am reading a book"
# # x = txt.replace("book", "magazine")
# # print(x)
# #
# # txt = "apple,banana,pear"
# # x = txt.split(',')
# # print(x)
# #
# # txt = "one|two|three|four"
# # x = txt.split('|')
# # print(x)
# #
# # txt = "Line 1\nLine 2\nLine 3"
# # lines = txt.splitlines()
# # print(lines)
# #
# # txt = "Hello World"
# # lines = txt.splitlines()
# # print(lines)
# #
# # mydict = {97: 111}
# # txt = "apple"
# # print(txt.translate(mydict))
# #
# #
# # mydict = {32: 45}
# # txt = "Hello World"
# # print(txt.translate(mydict))
# #
# #
# # txt = "Hello"
# # x = txt.zfill(8)
# # print(x)
# #
# # txt = "-42"
# # x = txt.zfill(5)
# # print(x)
# #
# #
# # txt = "123abcDEF"
# # x = txt.upper()
# # print(x)
# #
# # txt = "python programming"
# # x = txt.upper()
# # print(x)
#
#
# # name = "what is your name"
# # name = name.encode()
# # print(name)
#
# txt = "Hello Sam!"
#
# mytable = str.maketrans("S", "P")
# print(mytable)
# print(txt.translate(mytable))
from for_homework import musiqalar, rasmlar

# pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]
# toqri_poshta = []
# notoqri_poshta = []
# for poshta in pochtalar:
#  if "@" in poshta:
#      toqri_poshta.append(poshta)
#  else:
#      notoqri_poshta.append(poshta)
#
# print(toqri_poshta)
# print(notoqri_poshta)


# pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]
# for pochta in pochtalar:
#     if pochta.find("@") != -1:
#         print(f"{pochta} >>> to'g'ri pochta")
#     else:
#         print(f"{pochta} >>>> noto'g'ri pochta")


# parollar=["password123", "Qwerty!", "admin", "StrongPass1!"]
#
# for parol in parollar:
#
#     if len(parol)<8:
#         print(f"{parol}: Parol qisqa")
#     elif parol.isalpha():
#         print(f"{parol}: parol kuchsiz")
#     elif parol.isdecimal():
#         print(f"{parol}: kuchsiz parol")
#     else:
#         print(f"{parol}: parol kuchli!")
#

# haroratlar = [20,22, 19, 24, 25, 23, 21]
# ortacha = sum(haroratlar)/len(haroratlar)
# print(f"O'rtacha harorat: {ortacha}")
# for harorat in haroratlar:
#     if harorat>22:
#         print(f"{haroratlar.index(harorat)+1} - iliq kun")
#     else:
#         print(f"{haroratlar.index(harorat)+1} -salqin kun")


# fayllar = [ "kitob.jpg", "ko_ jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]
# musiqalar=[]
# rasmlar=[]
# for fayl in fayllar:
#     if 'jpg' in fayl:
#         rasmlar.append(fayl)
#     else:
#         musiqalar.append(fayl)
#
# print(f"Musiqalar:{musiqalar}")
# print(f"Rasmlar:{rasmlar}")
#






