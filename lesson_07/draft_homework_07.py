# task 1
print('task 1' + '-' * 20)
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= number:
        result = number * multiplier
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1
multiplication_table(5)
print('-' * 26)

# task 2
print('task 2' + '-' * 20)
def duble_sum(first, second):
    print(first + second)
duble_sum(4, 10)
print('-' * 26)

# task 3
print('task 3' + '-' * 20)
def middle(numbers_list):
    middle_list = sum(numbers_list) / len(numbers_list)
    return middle_list

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(middle(numbers_list))
print('-' * 26)

# task 4
print('task 4' + '-' * 20)
def backword_text(text):
    print(text[:: -1])

some_text = input()
backword_text(some_text)
print('-' * 26)

# task 5
print('task 5' + '-' * 20)
def sorted_by_len(list):
    sorted_list = sorted(list, key=lambda x: len(x))
    print(sorted_list[-1])

list = ['qqqqqwert', 'ee', 'rrrr']
sorted_by_len(list)
print('-' * 26)

# task 6
print('task 6' + '-' * 20)
def find_substring(first_string, second_string):
    index = first_string.find(second_string)
    return index

first_string = "The quick brown fox jumps over the lazy dog"
second_string = "cat"
print(find_substring(first_string, second_string))
print('-' * 26)

# task 7
print('task 7' + '-' * 20)
def find_symbon():
    while True:
        text = input('Enter some text\n')
        if 'h' in text or 'H' in text:
            print('True')
            break

find_symbon()
print('-' * 26)

# task 8
print('task 8' + '-' * 20)
car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),
  'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
  'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
  'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
  'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
  'Kia': ('white', 2020, 2.0, 'sedan', 28000),
  'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
  'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
  'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
  'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
  'Jeep': ('green', 2021, 3.0, 'suv', 50000),
  'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
  'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
  'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
  'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
  'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
  'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
  'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
  'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
  'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
  'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
  'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
  'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
  'Acura': ('white', 2017, 2.4, 'suv', 40000),
  'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
  'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
  'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
  'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
  'Ram': ('black', 2019, 5.7, 'pickup', 40000),
  'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
  'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
  'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
  'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}

search_criteria = (2017, 1.6, 36000)
def cars_sort(cars, search):
    sorted_car_data = []
    for key, value in cars.items():
      if value[1] >= search[0] and value[2] >= search[1] and value[4] <= search[2]:
        sorted_car_data = car_data.items()
    sorted_car_data = sorted(sorted_car_data, key=lambda car: car[1][4])
    print(sorted_car_data[0:5:])

cars_list = cars_sort(car_data, search_criteria)
print('-' * 26)

# task 9
print('task 9' + '-' * 20)
def check_type (mix_list):
    list_of_str = [k for k in mix_list if type(k) is str]
    print(list_of_str)

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
check_type(lst1)
print('-' * 26)

# task 10
print('task 9' + '-' * 19)
def num_of_even_numbers(numbers_list):
    numbers_sum = 0
    for num in numbers_list:
        if num % 2 == 0:
            numbers_sum += num
    print(numbers_sum)

numbers_list = [1, 2, 3, 4, 5, 6, 77, 88.7]
num_of_even_numbers(numbers_list)
