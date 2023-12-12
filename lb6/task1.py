def insert_element(lst, target_element, new_element):
    
    try:
        index = lst.index(target_element)
        lst.insert(index, new_element)
        print(f"Елемент {new_element} вставлено перед {target_element}.")
    except ValueError:
        print(f"Елемент {target_element} не знайдено у списку.")

user_list = input("Введіть елементи списку через пробіл: ").split()

target_element = input("Введіть елемент, перед яким треба вставка: ")
new_element = input("Введіть новий елемент для вставки: ")

insert_element(user_list, target_element, new_element)
print("Список після вставки:", user_list)