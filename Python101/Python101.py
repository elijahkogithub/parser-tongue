# # 01 Your First Python Program
# print('Elijah Ko')
# print('o----')
# print('||||')
# print('*' * 10)
#
# # 02 Variables
# price = 10 #integer
# rating = 4.9 #float
# name = 'Elijah' #string
# is_published = True #boolean
# is_executed = False
# print(is_executed)
# full_name = 'John Smith'
# age = 20
# is_new = True
# age = 40
# print(is_new)
# print(age)
#
# # 03 Receiving Input
# name = input('What is your name? ') #input is string
# favorite_color = input('What is your favorite color? ')
# print(name + ' likes ' + favorite_color)
#
# # 04 Type Conversion
# birth_year = input('Birth year: ') #input is always a string
# print(type(birth_year))
# age = 2019 - int(birth_year)
# float()
# bool()
# print(type(age))
# print(age)
# weight_lbs = input('Weight (lbs): ')
# weight_kg = float(weight_lbs)/2.2
# print(f'{weight_kg} kg')
#
# # 05 Strings
# course = 'Python course for "beginners"'
# print(course)
# email = '''
# Hi everyone,
#
# This is Elijah from UK,
# I am writing this email as a testing for the
# Python
# programming!
#
# best,
# Elijah
# '''
# print(email)
#
# string = 'FISM 2021'
# print(string[0])
# print(string[-3])
# print(string[0:])
# print(string[0:5])
# print(string[0:7])
# print(string[1:-1])
# print(string[:])
#
# # 06 Formatted Strings
# first = input('first name: ')
# last = input('last name: ')
# occupation = input('occupation: ')
# message = first + ' [' + last + '] ' + 'is a ' + occupation #Elijah [Ko] is a magician
# print(message)
# msg = f'{first} [{last}] is a {occupation}' #formatted string
# print(msg)
#
# # 07 String Methods
# course = 'TarBell CouRse iN mAgIc'
# print(len(course)) #length
# print(course.upper())
# print(course)
# print(course.lower())
# print(course.capitalize())
# print(course.title())
# print(course.find('A'))
# print(course.find('CouR'))
# print(course.find('xyz')) #-1 if it can't find anything
# print(course.replace('mAgIc', 'magic Vol.3'))
# print(course)
# string = 'AbAcDeFAAA'
# print(string)
# print(string.replace('A', '1'))
# print(string)
# print('AbA' in string) #in operator, return True or False
# print('Dhh' in string)
# # 08 Arithmetic Operation
# print(10.123)
# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)
# x = 10
# x += 3
# msg = f'x is equal to {x}'
# print(msg)
#
# # 09 Operator Precedence
# x = 10 + 3 * 2 ** 3
# print(x)
# x = (10 + 3) * 2 ** 3
# print(x)
#
# # 10 Math Functions #https://docs.python.org/3/library/math.html
# import math
# x = -2.9
# print(round(x))
# print(abs(x))
# print(math.ceil(x))
# print(math.floor(x))
# y = 10
# print(math.factorial(y))
#
# #11 If Statements
# temp = input('Temperature: ')
# temp = int(temp)
# if temp > 30:
#     print('It is a hot day')
# elif temp > 25:
#     print('It is a warm day')
# else:
#     print('Is is a cool day')
# print('Have a nice day')
#
# price = input('Input the price :$')
# good_credit = False
# if good_credit:
#     print('10% deposit')
#     price = int(price) * 0.1
# else:
#     print('20% deposit')
#     price = int(price) * 0.2
# print(f'Down payment: ${price}')
#
# #12 Logical Operators
# high_income = True
# good_credit = False
# criminal_record = False
# if high_income and good_credit:
#     print("Eligible for loan")
# if high_income or criminal_record:
#     print("consider case by case")
# if high_income and not criminal_record:
#     print("OK for loaning")
#
# # 13 Comparison Operators (> < >= <= == !=)
# name = input('Name: ')
# print(len(name))
# if len(name) < 3:
#     print('name must be at least 3 characters')
# elif len(name) > 50:
#     print('name has a upper limit of 50 characters')
# else:
#     print('name looks good')
#
# # 14 Weight Converter Program
# weight = input('Weight: ')
# unit = input('(L)bs or (K)g; ')
# if unit == 'k' or unit == 'K':
#     print(f'{weight} kg')
#     print(f"You are {float(weight) * 2.2} pounds")
# elif unit == 'l' or unit == 'L':
#     print(f'{weight} lbs')
#     print(f"You are {float(weight) / 2.2} kilograms")
#
# # 15 While Loops
# i = 1
# while i <= 5:
#     print('*' * i)
#     i += 1
# print('done')
#
# # 16 Guessing Game
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('guess the number between 0-9: '))
#     guess_count += 1
#     if guess == secret_number:
#         print(f"Successful! {secret_number} is the secret number")
#         break
#     else:
#         print('try again')
# else: #THIS IS THE 'else'PART OF WHILE-LOOP #if guess_count == guess_limit and guess != secret_number:
#     print('failed')
#
# #17 Building the Car Game
# command = "" #empty string
# start = 0
# stop = 0
# while True:
#     command = input('>').lower()
#     if command == "start":
#         start += 1
#         stop = 0
#         if start == 1:
#             print('Car started...Ready to go!')
#         else:
#             print('Car has already started')
#     elif command == "stop":
#         stop += 1
#         start = 0
#         if stop == 1:
#             print('Car stopped.')
#         else:
#             print('Car has already stopped')
#     elif command == "help":
#         print("""
# 'start - to start the car'
# 'stop - to stop the car'
# 'quit - to exit'
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("I don't understand that...")
# print('quit application')
#
# # 18 For-loop
# for item in ['Python', 'C++', 'Java Script']:
#     print(item)
# for item in range(10):
#     print(item)
# for item in range(10, 20):
#     print(item)
# for item in range(10, 50, 5):
#     print(item)
# prices = [10, 20, 30, 40]
# total = 0
# for p in prices:
#     total += p
#     print(f'current sum: ${total}')
# print(f'total value: ${total}')
#
# # 19 Nested Loop
# for x in range(4):
#     for y in range(3):
#         print(f"{x}, {y}")
#
# numbers = [5, 2, 5, 2, 2]
# for n in numbers:
#     output = ''
#     for i in range(n):
#         output += 'x'
#     print(output)
#
# # 20 Lists
# names = ['Tim', 'Katie', 'Sam', 'Blessing', 'Elijah']
# print(names[2:4])
# names[0] = 'Timothy'
# print(names[:])
# 20 List - Find the largest number
# numbers = [0, 3, 49, 1, 7]
# max = numbers[0]
# for i in numbers:
#     if i >= max:
#         max = i
# print(max)
#
# # 21 2D Lists
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[0][2])
# matrix[0][2] = 20
# print(matrix[0][2])
#
# for row in matrix:
#     for item in row:
#         print(item)
# #
# # 22 List Methods
# numbers = [1, 1, 2, 3, 3, 3, 4]
# numbers.append(5) #add
# print(numbers)
# print(numbers.count(3))
# numbers.insert(0, 0)
# print(numbers)
# numbers.remove(3)
# print(numbers)
# numbers.reverse()
# print(numbers)
# print(numbers.index(3, 0, 6)) #locate the 1st occurrence of 3
# numbers.pop(7) #remove
# print(numbers)
# print(3 in numbers) #get a boolean
# numbers.sort() #None is not returning any value
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers2 = numbers.copy()
#
# # 22 List Methods - Remove the duplicates
# numbers = [0, 1, 3, 4, 2, 9, 4, 6, 1, 4, 2, 8, 7, 4, 5, 3, 1, 2, 3, 5, 8, 9, 6, 6, 4, 3, 2]
# print(numbers.__len__()) #magic methods
# numbers.sort()
# print(numbers)
# unique = []
# for i in numbers:
#     if i not in unique:
#         unique.append(i)
#         print(unique)
#
# # 23 Tuple (no modification)
# numbers.tuple(1, 2, 3)
#
# # 24 Unpacking
# coordinates = (3, 500, 500)
# x = coordinates[0] #method 1
# y = coordinates[1] #method 1
# z = coordinates[2] #method 1
# x, y, z = coordinates #method 2
# print(x * y * z)
#
# # 25 Dictionaries (each key should be unique in the dictionary)
# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True
# }
# print(customer.get("age", "!")) #get doesn't yell at you
# print(customer.get("birthdate"))
# print(customer.get("birthdate", "Apr 17 1992"))
# customer["birthdate"] = "Apr 17 1992" #add key value
# print(customer["birthdate"])
# print(customer["name"])
# customer["name"] = "Elijah Ko"
# print(customer["name"])
# # 25.1 Dictionary - Phone numbers translation
# phone = input('Phone: ')
# digits_mapping = {
#     "0": "Zero",
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine"
# }
# output = ""
# for char in phone:
#     output += digits_mapping.get(char, "!") + " "
# print(output)
#
# #25.2 Dictionary - Emoji Converter
# message = input('>')
# message = message.split(' ') #get a list
# emoji = {
#     ":)": "😀",
#     ";)": "😉",
#     ":(": "😔"
# }
# output = ""
# for word in message:
#     output += emoji.get(word, word) + " "
# print(output)
#
# # 26.1 Functions
# def greet_user():
#     print('Hi there!')
#     print('Welcome onboard')
#
#
# print('Start')
# greet_user() #always define the functions first
# print('Finish')
#
# # 26.2 Parameters / Positional Arguments
# def greet_user(first_name, last_name):
#     print(f"Hi there! {first_name} {last_name}")
#     print('Welcome onboard')
#
#
# print('Start')
# greet_user(input("first name: "), input("last name: ")) #always define the functions first
# print('Finish')
#
# # 26.3 Keyword Arguments (positional argument first!!!)
# def greet_user(first_name, last_name):
#     print(f"Hi there! {first_name} {last_name}")
#     print('Welcome onboard')
#
#
# print('Start')
# greet_user(first_name=input("first name: "), last_name=input("last name: ")) #always define the functions first
# print('Finish')
#
# #26.4 Return Statement
# def square(number):
#     return number * number
#
#
# result = square(int(input('number: ')))
# print(result)
#
# # 26.5 Creating a Reusable Function
#
# def emoji_converter(message):
#     message = message.split(' ') #get a list
#     emoji = {
#         ":)": "😀",
#         ";)": "😉",
#         ":(": "😔"
#     }
#     output = ""
#     for word in message:
#         output += emoji.get(word, word) + " "
#     return output
#
#
# print(emoji_converter(input('>')))
#
# # 27 Exceptions #to handle errors
# try:
#     age = int(input('Age: '))
#     income = 20000
#     risk = income / age
#     print(age)
# except ValueError: #name of error can be found in the console
#     print('Age must be an integer')
# except ZeroDivisionError: #name of error can be found in the console
#     print('Age cannot be 0')
#
# # 28 Classes / Constructors
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print('move')
#
#     def draw(self):
#         print('draw')
#
#
# point1 = Point(1, 2)
# point1.draw()
# point1.move()
# print(point1.x)
# print(int(point1.y))
# point1.z = 30
# print(point1.z)
#
# point2 = Point(3, 4)
# print(point2.x)
#
# # 28.1 Person Class
# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def talk(self):
#         print(f"My name is: {self.first_name} {self.last_name}")
#
#
# person1 = Person('Elijah', 'Ko')
# person1.talk()
#
# person2 = Person('Colette', 'Herry')
# person2.talk()
#
# # 28.2 Inheritance
# class Mammal:
#     def walk(self):
#         print('walk')
#
#
# class HumpbackWhale(Mammal):
#     def __init__(self, full_name):
#         self.full_name = full_name
#
#     def name(self):
#         print(f"Name: {self.full_name}")
#
#
# class SiberianTiger(Mammal):
#     pass #tell python there is nothing
#
#
# whale1 = HumpbackWhale('Dory')
# whale1.name()
# whale1.walk()
#
# tiger1 = SiberianTiger()
# tiger1.walk()
#
# # 29 Modules #like modules in supermarket
# import converters #M1
# from converters import kg_to_lbs #M2
#
# print(f"{converters.lbs_to_kg(150)} kg")
# print(f"{kg_to_lbs(70)} pounds")
#
# 29.1 Modules Exercise
# from util import find_max
# print(find_max([10, 3, 6, 2]))
#
# 30 Packages #shopping mall concept
# import ecommerce.shipping
# from ecommerce.shipping import calc_shipping, calc_shipping_extra
# print(calc_shipping())
# print(calc_shipping_extra())
#
# 31 Generating Random Values
# import random
#
# for i in range(0, 10, 2):
#     print(random.random())
#     print(random.randint(10, 20))
#
# members = ['Elijah', 'Tim', 'Katie', 'Sam']
# leader = random.choice(members)
# print(leader)
#
# # 31 Roll a dice
# import random
#
#
# class Dice:
#     def __init__(self, first_number, second_number):
#         self.first_number = first_number
#         self.second_number = second_number
#
#     def roll(self):
#         self.first_number = random.randint(1, 6)
#         self.second_number = random.randint(1, 6)
#         result = (self.first_number, self.second_number)
#         return result
#
#
# dice1 = Dice(6, 6)
# print(dice1.roll())
# 32 Path and Directory
# from pathlib import Path
#
# path = Path('ecommerce')
# print(path.exists())