word = input("Введіть слово: ")

character_count = {}

for char in word:
    character_count[char] = character_count.get(char, 0) + 1

print("Кількість різних символів у слові:")
for char, count in character_count.items():
    print(f"{char}: {count}")