# # 001 - Introduction
print('Hello World')
print('This is Elijah :)')
#
# # 002-1 - Strings - Working with Textual Data
# message = 'This is a message'
# print(message)
# message1 = "This is 'Elijah'"
# print(message1)
# message2 = 'This is \'Elijah\''
# print(message2)
# message3 = '''
# This
# is
# 'Elijah Ko'
# '''
# print(message3)
#
# # 002-2 - Strings - Working with Textual Data
# message4 = 'Hello World'
# print(len(message4))
# print(message4[:])
# print(message4[:5])
# print(message4[6:])
#
# # 002-3 - Strings - Working with Textual Data
# message5 = 'aBcDeFGhijKl mNoP abcde'
# print(message5.lower())
# print(message5.upper())
# print(message5.count('Hello'))
# print(message5.count('a'))
# print(message5.find('World')) #give -1 as false
# print(message5.find('abcde'))
# message4.replace('World', 'Universe')
# print(message4)
# message4 = message4.replace('World', 'Universe')
# print(message4)
#
# # 002-4 - Strings - Working with Textual Data
# first_name = 'Elijah'
# last_name = 'Ko'
# full_name = first_name + ' ' + last_name
# print(full_name)
# full_name = 'Hi, {} {}. It\'s great to see you!'.format(first_name, last_name) #format string 1
# print(full_name)
# full_name = f'Hi, Mr. {first_name} {last_name}, it\'s great to see you!!!' #format string 2
# print(full_name)
# full_name = f'Hi, Mr. {first_name} {last_name.upper()}, it\'s great to see you!!!'
# print(full_name)
#
# 002-5 - Strings - Working with Textual Data
# print(dir(first_name)) #pass a variable, get all attributes, methods
# print(help(str)) #type of variables, gives more info
# print(help(str.lower)) #direct way to access the usage of a specific attribute
#
# # 003-1 Integers and Floats - Working with Numeric Data
# number = 1
# number1 = 1.5
# boolean = True
# string1 = 'c'
# print(type(number))
# print(type(number1))
# print(type(boolean))
# print(type(string1))
#
# # 003-2 Integers and Floats - Working with Numeric Data
# num1 = 2
# num2 = 3
# addition = num1 + num2
# subtraction = num1 - num2
# multiply = num1 * num2
# exponent = num1 ** num2
# divide = num1 / num2
# full_division = num1 // num2
# modulus = num1 % num2
# print(addition)
# print(subtraction)
# print(multiply)
# print(exponent)
# print(divide)
# print(full_division)
# print(modulus)
#
# # 003-3 Integers and Floats - Working with Numeric Data
# num3 = 3
# num3 += 3
# print(num3)
# num3 *= 3
# print(num3)
#
# # 003-4 Integers and Floats - Working with Numeric Data
# num4 = -1.7679
# print(abs(num4))
# print(round(num4))
# print(round(num4, 3))
#
# # 003-5 Integers and Floats - Working with Numeric Data
# num5 = 23
# num6 = 41
# print(num5 == num6)
# print(num5 != num6)
# print(num5 >= num6)
# print(num5 <= num6)
# print(num5 > num6)
# print(num5 < num6)
#
# # 003-6 Integers and Floats - Working with Numeric Data
# num7 = '235'
# num8 = '413'
# num9 = int(num7) + int(num8)
# print(num9)
#
# # 004-1  Lists, Tuples, and Sets
# Lists and Tuples allow us to work with sequential data
# courses = ['English', 'Chinese', 'Physics', 'Chemistry']
# print(courses)
# print(courses[0])
# print(courses[-1])
# print(courses[:])
# print(courses[:3])
#
# # 004-2  Lists, Tuples, and Sets
# courses.append('Biology')
# print(courses)
# courses.insert(1, 'German')
# print(courses)
#
# # 004-3  Lists, Tuples, and Sets
# courses2 = ['Design', 'Japanese']
# courses.insert(0, courses2)
# print(courses)
# courses.extend(courses2)
# print(courses)
# courses.remove('Japanese')
# print(courses)
# popped = courses.pop(0)
# print(popped)
# print(courses)
#
# # 004-4  Lists, Tuples, and Sets
# # Sorting the list
# people = ['Tesla', 'Einstein', 'Newton', 'Faraday', 'Watson', 'Freud']
# print(people)
# people.reverse()
# print(people)
# sorted = sorted(people) #doesn't change sort the original list
# print(sorted)
# print(people)
# people.sort() #alphabetical order
# print(people)
#
# # 004-5  Lists, Tuples, and Sets
# numbers = [1, 12, 134, 51, 15, 150, 34]
# print(numbers)
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)
# sorted_numbers = sorted(numbers) #get a sorted version without altering the original
# print(sorted_numbers)
# print(numbers)
#
# # 004-6  Lists, Tuples, and Sets
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
#
# # 004-7  Lists, Tuples, and Sets
# print(people.index('Tesla'))
# print('Newton' in people) #return boolean
# for individual in people:
#     print(individual)
#
# # 004-8  Lists, Tuples, and Sets
# magazines = ['dezeen', 'times', 'nat geo', 'nature']
# for index, magazine in enumerate(magazines): #use enumerate to access the index and values
#     print(index, magazine)
#
# print()
#
# for index, magazine in enumerate(magazines, start=1):
#         print(index, magazine)
#
# # 004-9  Lists, Tuples, and Sets
# magazines_str = ' +'.join(magazines)
# print(magazines_str)
# magazines_str = ' - '.join(magazines)
# print(magazines_str)
# new_list = magazines_str.split(' - ')
# print(new_list)
#
# 004-10  Lists, Tuples, and Sets
# Tuples
# tuple1 = (1, 2, 3, 5, 6, 3)
# tuple2 = tuple1
# print(tuple1)
# print(tuple2)
# print(min(tuple1)) #access, but not modify
#
# # 004-11  Lists, Tuples, and Sets
# # Sets
# # Sets allow us to work with unordered unique values. Don't care about order
# phones = {'apple', 'samsung', 'nokia', 'motorola'}
# computers = {'microsoft', 'IBM', 'apple', 'dell'}
# print('apple' in phones)
# print(computers.intersection(phones)) #sharing items
# print(computers.difference(phones)) #non-sharing items
# print(computers.union(phones)) #merge
#
# # 004-12  Lists, Tuples, and Sets
# empty_list = []
# empty_list = list()
#
# empty_tuple = ()
# empty_tuple = tuple()
#
# empty_set = set() #not {}
#
# # 005-1 Dictionaries - Working with Key-Value Pairs
# student = {'name': 'Elijah', 'age': 27, 'courses': ['Engineering', 'Design', 'Maths']}
# print(student)
# print(student['name'])
# print(student.get('age')) #same as above
# print(student.get('phone'))
# print(student.get('phone', 'Not Found'))
#
# # 005-2 Dictionaries - Working with Key-Value Pairs
# # add
# student1 = {'name': 'Laura', 'age': 25, 'courses': ['Film', 'Art', 'Design']}
# print(student1)
# student1['phone'] = '07523 970721'
# print(student1)
# student1['name'] = 'Dudek' #replace name
# print(student1)
# student1.update({'name': 'David', 'age': 23, 'phone': '07152 271823'})
# print(student1)
#
# # 005-3 Dictionaries - Working with Key-Value Pairs
# # remove
# del student1['age']
# print(student1)
# popped_phone = student1.pop('phone')
# print(popped_phone)
# print(student1)
#
# # 005-4 Dictionaries - Working with Key-Value Pairs
# # Loop through all the keys
# student2 = {'name': 'Maria', 'age': 26, 'courses': ['Law', 'Latvian', 'Social Science']}
# print(len(student2))
# print(student2.keys())
# print(student2.values())
# print(student2.items()) #both key and values
#
# # 005-5 Dictionaries - Working with Key-Value Pairs
# # Loop using for-loop
# for key in student2:
#     print(key)
#
# print()
#
# for key, value in student2.items():
#     print(f'{key} -> {value}')
#
# # 006-1 Conditionals and Booleans - If, Else, and Elif Statements
# # Comparisons:
# # Equal:            ==
# # Not Equal:        !=
# # Greater Than:     >
# # Less Than:        <
# # Greater or Equal: >=
# # Less or Equal:    <=
# # Object Identity:  is
# language = input('Programming language: ')
# if language == 'python':
#     print('It is Python')
# elif language == 'java':
#     print('It is Java')
# elif language == 'c++':
#     print('It is C++')
# else:
#     print('no match')
#
# 006-2 Conditionals and Booleans - If, Else, and Elif Statements
# user_name = input('username: ')
# password = input('password: ')
# logged_in = False
# if user_name == 'elijah' and password == '920417' and logged_in == True:
#     print('You are logged in')
# else:
#     print('Failed')
#
# if user_name == 'elijah' or logged_in:
#     print('admin page')
# else:
#     print('logged in page')
#
# if not logged_in:
#     print('breached')
# else:
#     print('failed again')
#
# # 006-3 Conditionals and Booleans - If, Else, and Elif Statements
# # Object Identity:  is
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b)
# print(id(a))
# print(id(b))
# print(a is b)
#
# c = [4, 5, 6]
# d = c
# print(c == d)
# print(id(c))
# print(id(d))
# print(c is d)
#
# # 006-4 Conditionals and Booleans - If, Else, and Elif Statements
# # False Values:
#     # False
#     # None
#     # Zero of any numeric type
#     # Any empty sequence. For example, '', (), [].
#     # Any empty mapping. For example, {}.
#
# condition = {} #empty dictionary
#
# if condition:
#     print('evaluated to true')
# else:
#     print('evaluated to false')
#
# # 007-1 Loops and Iterations - For/While Loops
# nums = [1, 2, 3, 4, 5]
# for num in nums:
#     if num >= 3:
#         print('Found!')
#         break
#     print(num)
# print()
#
# for num in nums:
#     if num == 3:
#         print('Found!')
#         continue
#     print(num)
#
# # 007-2 Loops and Iterations - For/While Loops
# nums2 = [11, 12, 13, 14, 15]
# for num in nums2:
#     for letter in 'abc':
#         print(num, letter)
#
# # 007-3 Loops and Iterations - For/While Loops
# # for-loop
# for i in range(11):
#     print(i)
#
# for j in range(9, 0, -1): #decrement
#     print(j)
# #
# # 007-4 Loops and Iterations - For/While Loops
# # while-loop
# x = 0
#
# while x<10:
#     print(x)
#     x += 1
#
# # 008-1 Functions
# def hello_function():
#     print('Hello function!')
#
# for i in range(4):
#     hello_function()
#
# # 008-2 Functions
# def function_intro():
#     return 'Function Intro'
#
# print(function_intro())
# print(function_intro().upper())
# print(function_intro().capitalize())
#
# # 008-3 Functions
# def greeting(name):
#     return f'Welcome, {name}!'
#
# print(greeting('Elijah'))
#
# # 008-4 Functions
# def greeting(name, age = 25):
#     return f'Welcome, {name}. Are you {age} years old?!'
#
# print(greeting('Laura'))
# print(greeting('Elijah', age = 28))
#
# # 008-5 Functions
# # Positional and keyword argument
# def student_info(*args, **kwargs): # allow us to accept arbitrary of positional and keyword arguments
#     print(args)
#     print(kwargs)
#
# courses = ['Math', 'Physics']
# info = {'age': 14, 'gender': 'male'}
#
# student_info('Physics', 'Chemistry', age=25, gender='female') #same as below
# print()
# student_info(*courses, **info) #same as above
# print()
# student_info(courses, info)
#
# # 008-6 Functions
# # Examples
# # Number of days per month. First value placeholder for indexing purposes.
# month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# def is_leap(year):
#     """Return True for leap years, False for non-leap years."""
#
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#
#
# def days_in_month(year, month):
#     """Return number of days in that month in that year."""
#
#     # year 2017
#     # month 2
#     if not 1 <= month <= 12:
#         return 'Invalid Month'
#
#     if month == 2 and is_leap(year):
#         return 29
#
#     return month_days[month]
#
# print(days_in_month(2017, 2))
#
# # 009-1 Import Modules and Exploring The Standard Library
# import my_module
#
# courses = ['Math', 'English', 'Chinese', 'Chemistry', 'Astronomy']
# index = my_module.find_index(courses, 'Chinese')
# print(index)
# #
# # 009-2 Import Modules and Exploring The Standard Library
# # just rename the import
# import my_module as mm
#
# courses = ['Math', 'English', 'Chinese', 'Chemistry', 'Astronomy']
# index = mm.find_index(courses, 'Chinese')
# print(index)
#
# # 009-3 Import Modules and Exploring The Standard Library
# # import specific function
#
# from my_module import find_index
#
# courses = ['Math', 'English', 'Chinese', 'Chemistry', 'Astronomy']
# index = find_index(courses, 'Chinese')
# print(index)
#
# # 009-4 Import Modules and Exploring The Standard Library
# from my_module import find_index, test #access the test variable
#
# courses = ['Math', 'English', 'Chinese', 'Chemistry', 'Astronomy']
# index = find_index(courses, 'Chinese')
# print(index)
# print(test)
#
# # 009-5 Import Modules and Exploring The Standard Library
# # import everything, but not recommended, because the functions are not clearly stated
# from my_module import *
#
# # 009-6 Import Modules and Exploring The Standard Library
# # find import location
# from my_module import find_index, test #access the test variable
# import sys
#
# courses = ['Math', 'English', 'Chinese', 'Chemistry', 'Astronomy']
# index = find_index(courses, 'Chinese')
# print(index)
# print(test)
# print(sys.path)
#
# # 009-7 Import Modules and Exploring The Standard Library
# # import from standard library modules - random
# import random
#
# numbers = [1, 34, 33, 14, 15, 46, 642, 24]
# random_choice = random.choice(numbers)
# print(random_choice)
#
# # 009-8 Import Modules and Exploring The Standard Library
# # import from standard library modules - math
# import math
# rads = math.radians(90)
# print(rads)
# print(math.sin(rads))
#
# # 009-9 Import Modules and Exploring The Standard Library
# # import from standard library modules - datetime, calendar
# import datetime
# import calendar
# today = datetime.date.today()
# is_leap_year = calendar.isleap(2020)
# print(today)
# print(is_leap_year)
#
# # 009-10 Import Modules and Exploring The Standard Library
# import from standard library modules - os
# import os
# # print(os.getcwd()) #get current working directory
# courses = ['History', 'Geography', 'Religion']
# print(os.__file__)
#
# import antigravity