
def adventures(x):
    stone1 = ''

    for i in range(1, x):
        for j in range(i + 1, x + 1):
            if x % (i + j)== 0:
                stone1 += str(i) + str(j)
    return f'Ваш шифр: {stone1}'

x = int(input("Число камня первого поля: "))

ciphr = adventures(x)

print(ciphr)
