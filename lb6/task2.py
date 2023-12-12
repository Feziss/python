def find_element(lst, value):
    
    try:
        index = lst.index(value)
        return f"Елемент {value} знайдено за індексом {index}."
    except ValueError:
        return f"Елемент {value} не знайдено у списку"

user_list_str = input("Введіть числові елементи списку через пробіл: ")
try:
    user_list = [int(element) for element in user_list_str.split()]
except ValueError:
    print("Помилка: введені значення мають бути числовими.")
    exit()

search_value_str = input("Введіть значення для пошуку: ")
try:
    search_value = int(search_value_str)
except ValueError:
    print("Помилка: введене значення для пошуку має бути числовим")
    exit()

result = find_element(user_list, search_value)
print(result)