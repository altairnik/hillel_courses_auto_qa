# task 01 == Виправте синтаксичні помилки
# print("Hello", "world!") or print("Hello world!")
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(hello, world)

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
bananas = apples * 4
print('I have ', apples,' apples', ' and ', bananas, ' bananas','\n', 'I always have 4 times more bananas than apples=)', sep='')

# task 05 == виправте назви змінних
_storona = 1    # not beauty
torona_2 = 2
сторона_3 = 3   # not beauty
torona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = _storona + torona_2 + сторона_3 + torona_4
print(perimetery)
# or print(_storona + torona_2 + сторона_3 + torona_4)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07

"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple_trees = 4
pear_trees = apple_trees + 5
plum_trees = apple_trees - 2
all_trees = apple_trees + pear_trees + plum_trees
print('Apple trees', all_trees, 'Pear trees', pear_trees, 'Plum trees', plum_trees, 'All trees in the garden', all_trees)
# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
morning_temp = 5
lunchtime_temp = morning_temp - 10
nigh_temp = lunchtime_temp + 4
print('Night temprature is', nigh_temp )
# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys = 24
girls = int(boys / 2)
print('Today there are', boys + girls - 3, 'children in theater club')
# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
first_book = 8
second_book = first_book + 2
third_book = (first_book + second_book) / 2
total_cost = first_book + second_book + third_book
print('All books cost', total_cost)
# or print('All books cost', first_book + second_book + int(third_book))