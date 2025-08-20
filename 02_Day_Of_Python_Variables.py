#Variables in python

first_name = 'Karan'
last_name = 'Chadha'
country = 'India'
city = 'New Delhi'
age = '100'
skills = ['JS', 'C#', 'Python']
person_info = {
    'firstname': 'Karan',
    'lastname': 'Chadha',
    'country': 'India',
    'city': 'New Delhi'
}

#Printing the values stored in the variables
print('First name:', first_name)
print('First Name length', len(first_name))
print('Last Name', last_name)
print('Last Name length', len(last_name))
print('Country:', country)
print('City:', city)
print('Age:', age)
print('Skills:', skills)
print('Person information:', person_info)

#Declaring multiple variables in one line
first_name, last_name, country, city, age = 'Karan', 'Chadha', 'India', 'New Delhi', '100'

print(first_name, last_name, country, city, age)
