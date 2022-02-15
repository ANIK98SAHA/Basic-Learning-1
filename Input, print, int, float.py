name = input('What is your name? ')
Favourite_colour = input('What is your favourite colour? ')
birth_year = input('What is your birth year? ')
weight_k = input('What is your weight in kilograms? ')

age = 2022 - int(birth_year)
weight_P = float(weight_k) * 2.205

print(name + ' likes ' + Favourite_colour)
print(name + ' is ' + str(age) + ' years old.')
print(name + ' has weight of ' + str(weight_P) + ' pounds')
