# task 6.1
# я неправильно прочитал условие задачи(точнее спутал с задачай 6.2), я почему то думал что код нужно выполнять
# пока в строке не будет больше 10 уникальных символов поетому и использовал цикл
# unic_symbol = input('Enter some text\n')
# while True:
#     if len(set(unic_symbol)) < 10:
#         print('There are less than 10 unique symbols')
#         unic_symbol = input('Enter some text\n')
#     else:
#         print(f'There are {len(set(unic_symbol))} unique symbols')
#         break
unic_symbol = input('Enter some text\n')
if len(set(unic_symbol)) < 10:
    print('False')
else:
    print(f'There are {len(set(unic_symbol))} unique symbols')

# task 6.2
# тут если в инпуте будет "H" и "h" то постоянно будет выводится первый принт так как первая поверка идет на "h"
while True:
    some_text = input('Enter some text\n') # етот вариант намного проще
    if 'h' in some_text or 'H' in some_text:
        print('True')
        break
# while True:
#     checked_text = input('Enter some text\n')
#     if checked_text.find('h') != -1:
#         print('Congratulations, your find "h"')
#         break
#     elif checked_text.find('H') != -1:
#         print('Congratulations, your find "H"')
#         break

# task 6.3
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for element in lst1:
# lst2 = [k for k in lst1 if type(k) is str] # как действительно проще
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
