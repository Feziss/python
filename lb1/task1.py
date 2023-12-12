a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))
if a <= 0 or b <= 0:
    print("Числа a та b не додатні")
else:
    if a > b:
        X = a * b - 3
    elif a == b:
        X = 2
    else:
        X = (a**3 + 1) / b
    print("X = ", X)