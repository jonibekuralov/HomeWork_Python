ismlar = []
n=1
while True:
    ism = input(f"{n}-Do'stingiz ismini kiriting:(Dasturni to'xtatish uchun 'stop' deb yozing): ")
    if ism.lower() !='stop':
        ismlar.append(ism)
        n=n+1
        continue
    else:
        break

print(f"\nDo'stlaringiz ro'yxati:")
for ism in ismlar:
    print(ism)
