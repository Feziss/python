def find_root():
    equation = lambda x: 4*x + 5 - 25
    x = 1

    while equation(x) != 0:
        x += 1

    return x

result = find_root()
print(f"Корінь рівняння дорівнює x = {result}")
