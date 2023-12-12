input_string = input("Введіть рядок: ")

if len(input_string) >= 20:
    result_substring = input_string[19:]
    print(f"Зріз: {result_substring}")
else:
    print("Довжина рядка менша за 20 символів, не можливо виконати зріз")
