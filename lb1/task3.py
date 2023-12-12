N = int(input("Введіть ціле число N (1 < N < 9): "))

if 1 < N < 9:
    for i in range(N, 0, -1):
        for j in range(1, i + 1):
            print(j, end='')
        print()
else:
    print("Введене число не відповідає умовам")