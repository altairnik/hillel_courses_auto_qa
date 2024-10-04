# task 6.1
unic_symbol = input('Enter some text\n')
for _ in unic_symbol:
    if len(unic_symbol) < 10:
        print('False')
        break
    elif len(unic_symbol) - len(set(unic_symbol)) >= 9:
        print('True')
        break

# task 6.2
while True:
    checked_text = input('Enter some text\n')
    if checked_text.find('h') != -1:
        print('Congratulations, your find "h"')
        break
    elif checked_text.find('H') != -1:
        print('Congratulations, your find "H"')
        break

# task 6.3
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for element in lst1:
    if type(element) == str:
        lst2.append(element)
print(lst2)

# task 6.4
numbers_list = [1, 2, 3, 4, 5, 6, 77, 88.7]
numbers_sum = 0
for num in numbers_list:
    if num % 2 == 0:
        numbers_sum += num
print(numbers_sum)
