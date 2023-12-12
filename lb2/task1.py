import math

def calculate_z(a):
    z = math.cos(a) + math.cos(2 * a) + math.cos(6 * a) + math.cos(7 * a)
    return z

def calculate_y(n):
    y = 1
    for i in range(1, 2 * n, 2):
        y *= i
    return y

a = float(input("Введіть число alpha: "))
n = int(input("Введіть натуральне число n: "))

result_z = calculate_z(a)
result_y = calculate_y(n)

print(f"Результат для z=cosα+cos2α+cos6α+cos7α: {result_z}")
print(f"Результат для у=1*3*5*...(2*n-1): {result_y}")
