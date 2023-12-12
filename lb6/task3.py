def operate_set(input_set, operation_variant):
    if operation_variant == 'alphabetical_order':
        result_set = sorted(input_set)
        print("Елементи множини в алфавітному порядку:", result_set)
    else:
        result_list = list(input_set)
        print("Результат у вигляді списку:", result_list)
        
        print("Результат у вигляді множини:", set(result_list))

input_set = set('noatuvbcdejklmpqrswxyzfghi')

operation_variant = 'alphabetical_order'

operate_set(input_set, operation_variant)