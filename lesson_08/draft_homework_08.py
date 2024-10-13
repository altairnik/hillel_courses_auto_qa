def sum_in_list_of_string_elem(list_of_string):
    try:
        sum_of_string_elem = [int(num) for num in list_of_string.split(',')]
        return sum(sum_of_string_elem)
    except ValueError:
        print(f'Не можу це зробити, помилка у рядку {list_of_string}')
        return None

input_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

for elem in input_list:
    result = sum_in_list_of_string_elem(elem)
    if result is not None:
        print(result)

