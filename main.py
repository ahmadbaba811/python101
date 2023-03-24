# This is a sample Python script.
import math
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import converter
from utils import *
from ecommerce.shipping import cal_shipping

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# price = 20
# print(price)
#
#
# def price_function(price_p):
#     print(price_p)
#
#
# price_function(23.4)
# my_name = input('what is your name? ')
# my_color = input("what is your favourite color? ")
# birth_year = input("what is your birth year? ")
# calc_my_age = 2023 - int(birth_year)
# print('My name is ' + my_name + ", I like " + my_color + " color")
# print("I am " + str(calc_my_age) + " years old")

# _message = """Hey, Hope you are good,
# I have started learning python with Mosh
# He's good at the course."""
# _message2 = _message[:]
# print(_message)
# print(_message[1])
# print(_message[0:3])
# print(_message2)

student_name = "Isah Musa"
print(student_name[1:-2])


# formatted strings
# first_name = 'Isah'
# last_name = "musa"
# full_name = f'{first_name} [{last_name}]'
# print(full_name)
# print(len(first_name))
# print(first_name.upper())
# print(first_name.replace("Isah", "Idris Ahmad"))
# check = "v"
# if check in first_name:
#     print(f"{check} is in {first_name}")
# else:
#     print(f"{check} is not in {first_name}")


# operators
# _val = 3
# print(_val * 3) # multiplication
# print(_val / 2) # float divisor
# print(_val // 2) # integer divisor
# print(_val ** 2) # exponent
# print(_val % 2) # modulus
# _val += 2 # augmented assignment operator
# print(_val)


# #conditional statements
# first_val = True
# second_val = False
# if first_val or second_val:
#     print("one condition satisfies")
# elif first_val and second_val:
#     print("two conditions satisfies")
# elif first_val and not second_val:
#     print("first condition satisfies but the second does not")
# else:
#     print("default")
#
# #compare operatos
# # >, <, >=, <=, ==, !=,


# weight converter program
# my_wieght = input("enter your weight ")
# print("which unit do you want to convert to")
# weight_unit = input("(L) for pounds, (K) for kilogram ")
# weight_unit = weight_unit.lower()
# if weight_unit == "l" :
#     converted_wieght = float(my_wieght) * 0.45
#     print(converted_wieght)
# else:
#     converted_wieght = float(my_wieght) / 0.45
#     print(converted_wieght)


# while loop
# print("While Loop")
# i = 1
# while i <= 5:
#     print(i)
#     i = i + 1

# Guessing game
# guess_count = 1
# guess_limit = 3
# correct_val = 9
# while guess_count <= guess_limit:
#     guessed_number = input("enter a value: ")
#     if int(guessed_number) == correct_val:
#         print("you win")
#         break
#     else:
#         print("wrong, try again")
#     guess_count = guess_count + 1
# else:
#     print("sorry you only have three trials")
#     print("GAME ENDED")


# For Loop
#items = 'Pythons'
# items = [1, 2, 3, 4, 5]
# #items = range(4, 10, 2)
# total = 0
# for item in items:
#     total = total + item
# exit(print(f"TOTAL: {total}"))


# nested loop
# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")

# nest = [5, 2, 5, 2, 2]
# for x in range(len(nest)):
#     # for y in nest:
#     #     print("x" * y)
#     star_legth = nest[x];
#     print("x" * star_legth)


# find max number
numbers = [3, 6, 2, 8, 4, 10, 20, 2, 4, 4]
# max = numbers[0]
# for i in numbers:
#     if i > max:
#         max = i
# print(f"max is {max}")


# array methods
# numbers2 = numbers.copy()
# numbers.append(8)
# numbers.insert(2, 20)
# numbers.remove(2)
# # numbers.clear()
# numbers.sort()
# numbers.reverse()
# print(numbers)
# print(numbers.index(8))
# print(3 in numbers)
# print(numbers.count(2))

# remove duplicates
# uniques = []
# for i in numbers:
#     if i not in uniques:
#         uniques.append(i);
# print(uniques)


# unpacking
# cordinates = (1, 2, 4)
# # cordinates = [1, 2, 4]
# x, y, z = cordinates
# print(z)


#Dictionaries
customers = {
    "name": "Idris",
    "age" : 20,
    "location" : "Abuja",
}
# print(customers["name"])
# print(customers.get("nokey", "Default Name"))
#
#
# number_dictionaries = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }
# number_input = input("enter a number between 1 and 4 ")
# number_in_word = ""
# no_values = ""
# for i in number_input:
#     if number_dictionaries.get(i) == None:
#         no_values = no_values + i
#
# if no_values != "":
#     for x in no_values:
#         add_to_dictionary = input(f"{x} does not exists in the dictionary, would you like to add? Y(yes) N(No) ")
#         if add_to_dictionary.lower() == "y":
#             add_number = x
#             add_text = input(f"enter the number in words for {x} ")
#             number_dictionaries[add_number] = add_text
#         else:
#             break
# for i in number_input:
#         value_in_word = number_dictionaries.get(i, "!")
#         number_in_word = number_in_word + " " + value_in_word
# print(number_in_word)


# functions
# def add_to_dictionary(key, value):
#     customers[key] = value
#     return customers
#
#
# print(add_to_dictionary("favourite color", "GREEN"))


# exceptions
# try:
#     age = int(input("enter your age "))
#     print(age)
# except ValueError:
#     print("please enter an integer")


# classes
# class PointStart:
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")
#
#
# point1 = PointStart()
# point1.move()
# point1.x = 10
# point1.y = 20
# print(point1.x, point1.y)

# constructor
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print("move")
#     def draw(self):
#         print(f"draw the figure {self.x}")
#
# point1 = Point(20, 9)
# point1.y = 79
# print(point1.x, point1.y)
# point2 = Point(20, 19)
# point2.draw()


# Inheritance
# class Male:
#     def __init__(self, x):
#         self.x = x
#
#     def draw(self):
#         print(f"{self.x} is a gender")
#
#
# class Female(Male):
#     pass
#
# female = Female("female")
# female.draw()

# weight_converter(50)

max_number = find_maximum(numbers)
print(max_number)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
