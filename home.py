kinolar={}
ism_1 = input("Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali nima?\nIsmi: ")
kino_1 = input("1-kino nomini yozing: ")
kino_2 = input("2-kino nomini yozing: ")
kino_3 = input("3-kino nomini yozing: ")
# kinolar ={}
kinolar[ism_1]=[kino_1,kino_2,kino_3]

ism_2 = input("Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali nima?\nIsmi: ")
kino_4 = input("1-kino nomini yozing: ")
kino_5 = input("2-kino nomini yozing: ")
kino_6 = input("3-kino nomini yozing: ")
# kinolar_2 ={}
kinolar[ism_2]=[kino_4,kino_5,kino_6]


ism_3 = input("Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali nima?\nIsmi: ")
kino_7 = input("1-kino nomini yozing: ")
kino_8 = input("2-kino nomini yozing: ")
kino_9 = input("3-kino nomini yozing: ")
# kinolar_2 ={}
kinolar[ism_2]=[kino_4,kino_5,kino_6]
for ism_1,kinolar_royxati in kinolar.items():
    print(f"{ism_1.title()} yoqtirgan 3-ta film: {kinolar_royxati}")

for ism_2,kinolar_royxati in kinolar.items():
    print(f"{ism_2.title()} yoqtirgan 3-ta film: {kinolar_royxati}")

for ism_3, kinolar_royxati in kinolar.items():
    print(f"{ism_3.title()} yoqtirgan 3-ta film: {kinolar_royxati}")