N = int(input("Введіть розмір масиву: "))

array = []

print("Введіть елементи масиву:")
for i in range(N):
    element = float(input(f"Елемент {i + 1}: "))
    array.append(element)

max_element = max(array)

print(f"Максимальний елемент в масиві: {max_element}")