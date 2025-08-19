# name = "karan"
# age = 28 
# height = 5.9
# is_developer = True

# print("Name", name)
# print("Age", age)
# print("Height", height)
# print("Developer", is_developer)


# # A list of favourite foods
# favourite_food = ["Pasta", "Pizza", "Momos", "Icecream"]
# print("My favourite foods are") 
# for food in favourite_food:
#     print("-", food)


age = 80
is_student = True
if age < 13:
    print("You are a child")
elif age > 18 and is_student == True:
    print("You are a adult teenager")
elif age < 20:
    print("You are a teenager")
elif age > 60:
    print("You are a senior citizen")
else:
    print("You are an adult")

def greet_user(name):
    print("Hello", name)
    print("Welcome to python")

#input_name = input("Enter your name:")
#greet_user(input_name)

def calculate_square(number):
    print("Square of a number is:", number * number)

calculate_square(5)

#Dictionary to story person details

person = {
    "name": "Karan",
    "age": 25,
    "city": "Delhi"
}

print("Name:", person["name"])
print("Age:", person["age"])
print("Name:", person["city"])
for key, value in person.items():
    print(key + ":" , value)

letter = 'P'
print(letter)
print(len(letter))
greeting = "Hello world"
print(greeting)
print(len(greeting))

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)
print(len(multiline_string))

another_multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""

first_name = "karan"
last_name = "chadha"
space = ' '
full_name = first_name + space + last_name
print(full_name)
print(len(first_name) > len(last_name))

language = "Python"
first_letter = language[0]
print(first_letter)
last_letter = language[-1]
print(last_letter)

#slicing
first_three= language[0:3]
print(first_three)
last_three = language[3:6]
print(last_three)
last_three = language[-3:]
print(last_three)

#skipping character while splitting python strings
language = 'Python'
pto = language[0:6:2]
print(pto)

#string methods
# capitalize(): Converts the first character the string to Capital Letter

challenge = 'thirty days of python'
capital = print(challenge.capitalize())

#count(): returns occurances of substring in string count(substring, start='', end='')
challenge = 'thirty days of python'
print(challenge.count('y'))
print(challenge.count('y', 7, 14))
print(challenge.count('th'))

#endswith() : checks if the string ends with the specified ending
challenge = 'thirty days of python'
print(challenge.endswith('on'))
print(challenge.endswith('py'))

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))

#find() returns the index of the first occurance of a substring
challenge = 'thirty days of python'
print(challenge.find('y'))
print(challenge.find('th'))

#format() format string to a nicer output
first_name = 'Karan'
last_name = 'Chadha'
job = 'Teacher'
country = 'India'
sentence = 'I am {}{}. I live in {}. I am a {}'.format(first_name, last_name, country, job)
print(sentence)

#isalnum(): checks alphanumeric character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum())
challenge = '30DaysPython'
print(challenge.isalnum())
challenge = 'Thirty Days Python'
print(challenge.isalnum())

#isalpha() checks if all the characters are alphabets
challenge = 'ThirtyDaysPython'
print(challenge.isalpha())
num = '123'
print(num.isalpha())

#isDigit checks Digit character
num = '10'
print(num.isdigit())
num = 'thirty'
print(num.isdigit())

# isdecimal():Checks decimal characters
num = '10'
print(num.isdecimal()) # True
num = '10.5'
print(num.isdecimal()) # False

#islower(): checks if all the alphabets in a string are lowercase
challenge = 'thirtydaysofcoding'
print(challenge.islower())
challenge = 'Thirtydaysofcoding'
print(challenge.islower())

#islower(): checks if all the alphabets in a string are uppercase
challenge = 'THIRTYDAYSOFCODING'
print(challenge.isupper())
challenge = 'Thirtydaysofcoding'
print(challenge.isupper())

#isnumeric() checks numeric characters
num = '10'
print(num.isnumeric())
print('Ten'.isnumeric())

#join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'Javascript', 'React']
result = '#,'.join(web_tech)
print(result)

#strip(): Removes both leading and trailing characters
challenge = 'thirty days of python'
print(challenge.strip('y')) # 5

#replace(): replace substring inside
challenge = 'thirty days of code'
print(challenge.replace('code','python'))

#split(): split strings from left
challenge = 'thirty days of python'
print(challenge.split())

# title(): Returns a Title Cased String
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

# swapcase(): Checks if String Starts with the Specified String
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): Checks if String Starts with the Specified String

challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
challenge = '30 days of python'
print(challenge.startswith('thirty')) # False