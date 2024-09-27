# task 01-03
alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal 
on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which 
way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do 
that," said the Cat, "if you only walk long enough."'''
alice_in_wonderland = ("Would you tell me, please, which way I ought to go from here?\n"
                         "That depends a good deal on where you want to get to, said the Cat.\n"
                         "I don't much care where —— said Alice.\n"
                         "Then it doesn't matter which way you go, said the Cat.\n"
                         "—— so long as I get somewhere, Alice added as an explanation.\n"
                         "Oh, you're sure to do that, said the Cat, if you only walk long enough.")
print(alice_in_wonderland)

# task 04
black_sea_square = 436402
azov_sea_square = 37800
print('Total square of Black Sea and Azov Sea is', black_sea_square + azov_sea_square)

# task 05
# store_1 + store_2 = 250449
# store_2 + store_3 = 222950
# store_1 = 250449 - store_2
# store_3 = 222950 - store_2
# 250449 - store_2 + store_2 + 222950 = 375291 -> store_2 = (250449 + 222950) - store_total
store_total = 375291
store_2 = 473399 - 375291
store_1 = 250449 - store_2
store_3 = 222950 - store_2
print(f'Products on first store are {store_1} \n'
     f'Products on second store are {store_2} \n'
     f'Products on third store are {store_3}')

# task 06
period = 18
month_pay = 1179
print(f'Computer cost {period * month_pay}')

# task 07
print('remainder from division 8019 and 8 is ', 8019 % 8)
print('-' * 40)
print('remainder from division 9907 and 9 is ', 9907 % 9)
print('-' * 40)
print('remainder from division 2789 and 5 is ', 2789 % 5)
print('-' * 40)
print('remainder from division 7248 and 6 is ', 7248 % 6)
print('-' * 40)
print('remainder from division 7128 and 5 is ', 7128 % 5)
print('-' * 40)
print('remainder from division 19224 and 9 is ', 19224 % 9)

# task 08
pizza_big = 274
pizza_medium = 218
juice = 35
cake = 350
woter = 21
total = pizza_big * 4 + pizza_medium * 2 + juice * 4 + cake + woter * 3
print('Total budget is ', total)

# task 09
total_photos = 232
min_pages = int(232 / 8)
print(f'Photo album should have a minimum {min_pages} pages')

# task 10

distance = 1600
volume_gas_tank = 48
consumption_per_100 = 9
total_gas = (1600 / 100) * 9
gas_refill = total_gas / volume_gas_tank
print('Total gas for trip is', total_gas)
print(f'Gas refill {round(gas_refill)} times')

