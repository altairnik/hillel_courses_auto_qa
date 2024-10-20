def middle(numbers_list):
    middle_list = sum(numbers_list) / len(numbers_list)
    return middle_list



def sorted_by_len(list):

    sorted_list = sorted(list, key=lambda x: len(x))
    return (sorted_list[-1])

def num_of_even_numbers(numbers_list):
    numbers_sum = 0
    for num in numbers_list:
        if num % 2 == 0:
            numbers_sum += num
    return numbers_sum
numbers_list = [1, 2, 3, 4]