# %%
from survey import AnonymousSurvey
import unittest
from name_function import get_formatted_name
import json
import random
from random import randint
from collections import OrderedDict
import this
name = "chris wilson"
uppercase_name = name.upper()
print(name.title())
print(name.upper())
print(uppercase_name)

first_name = "chris"
last_name = "wilson"
full_name = f"{first_name} {last_name}"
message = (f"{full_name.title()}!")
print(message)

print("Languages:\nPython\nC\nJavascript")
print("Languages:\n\tPython\n\tC\n\tJavascript")

favorite_name = " python "
print(favorite_name.rstrip())
print(favorite_name.lstrip())
print(favorite_name.strip())


# %%
first_name = "Chris"
last_name = "Wilson"
full_name = f"{first_name} {last_name}"
print(f"{first_name} {last_name}")
print(f"Hello {first_name} {last_name}, how are you today? ")
print(full_name.title())
print(full_name.upper())
print(full_name.lower())
print(full_name.strip())
print(full_name.lstrip())
print(full_name.rstrip())
quote = " said: A person who never made a mistake mever tried anything"
name = "Albert Einstien"
finished_quote = name + quote
print(finished_quote)
universal_age = 14_000_000_000
print(universal_age)
# %%
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles[2].upper())
print(bicycles[3].title())
print(bicycles[-1].title())
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
# %%
friends = ["Spencer", "Eddie", "Sean", "Sasha", "Mikey", "Josh"]
print(friends[1])
print(friends[2].lower())
print(friends[3].upper())
print(friends[-1][0].lower())
# %%
friends = ["Spencer", "Eddie", "Sean", "Sasha", "Mikey", "Josh"]
print(friends)
friends[0] = "John"
print(friends)
friends.append("Chris")
print(friends)

# %%
friends = []
friends.append('Chris')
friends.append('John')
friends.append('Sean')
friends.append('Eddie')
friends.append('Spencer')
friends.append('Sasha')
friends_upper = [i.title() for i in friends]
print(friends_upper)
friends_popped = friends_upper.pop()
print(friends_popped)
# %%
friends = ["Spencer", "Eddie", "Sean", "Sasha", "Mikey", "Josh"]
popped_friends = friends.pop()
print(popped_friends)
youngest_friend = friends.pop()
print(youngest_friend)

# %%
friends = ["spencer", "eddie", "sean", "sasha", "mikey", "josh"]
youngest_friend = friends.pop(0).title()
print(f"My youngest friends is {youngest_friend}!")
# %%
friends = ["spencer", "eddie", "sean", "sasha", "mikey", "josh"]
youngest_friend = friends.pop().title()
print(f"My youngest friends is {youngest_friend}!")

# %%
friends = ["spencer", "eddie", "sean", "sasha", "mikey", "josh"]
removed_friend = friends.remove("josh")
print(friends)
# %%
friends = ["spencer", "eddie", "sean", "sasha", "mikey", "josh"]
too_whiny = "mikey"
friends.remove(too_whiny)
print(friends)
print(f"\n{too_whiny.title()} was too whiny to be a friend.")
# %%
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)
len(cars)
cars.reverse()
print(cars)
cars.reverse()
print(cars)
# %%
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see another trick by {magician.title()}.\n")
print("Thanks for the great show!")
# %%
dogs = ['chihuahua', 'akita', 'bulldog', 'dane', 'samoyed', 'yorkshire']
for dog in dogs:
    print(f"I love all {dog.title()}!\n {dog.upper()}")
print("Dogs are awesome!")
# %%
for value in range(6):
    print(value)
for value in range(1, 6):
    print(value)
for value in range(1, 13, 2):
    print(value)
# %%
numbers = list(range(1, 10))
print(numbers)
# %%
# List of squared numbers
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# optimal
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
# %%
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(digits))
print(max(digits))
print(sum(digits))
# %%
squares = [value**2 for value in range(1, 11)]
print(squares)

# %%
players = ["charlies", "martina", "micheal", "florence", "eli"]
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[-3:])
print("Here are the first three people on my team:")
for player in players[:3]:
    print(player.title())
# %%
my_foods = ["pizza", "falafel", "carrot cake"]
friends_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friends_foods)

# %%
my_foods = ["pizza", "falafel", "carrot cake"]
friends_foods = my_foods[:]
my_foods.append('cannoli')
friends_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friends_foods)
# %%
# Tuples
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
    print(dimension)
# %%
dimensions = (200, 50)
print("Original Dimensions")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified Dimensions")
for dimension in dimensions:
    print(dimension)
# %%
foods = ("pizza", "burger", "sandwhich", "macandcheese")
print("These are my favorite foods:")
for food in foods:
    print(food)
foods = ("pizza", "burger", "rice", "sushi")
print("\nThese are the new foods:")
for food in foods:
    print(food)
# %%
cars = ["audi", "bmw", 'subaru', 'toyota']
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())
# %%
car = 'Audi'
car.lower() == 'audi'
car
# %%
requested_topping = 'musrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies')
# %%
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
# %%
# and condition both must pass for true
(age_0 >= 21) and (age_1 >= 21)
# %%
# or either condition can pass for true
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21
age_0 = 18
age_0 >= 21 or age_1 >= 21
# %%
requested_toppings = ['mushroom', 'onions', 'pineapple']
'mushroom' in requested_toppings
'pepperoni' in requested_toppings
# %%
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ', you can post a response if you wish.')
# %%
car = 'subaru'
print("Is car == 'subaru'? I perdict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I perdict False.")
print(car == 'audi')
# %%
age = 19
if age >= 18:
    print("Your old enough to vote!")
    print("Have you registered to vote yet?")
# %%
age = 17
if age >= 18:
    print("Your old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote!")

# %%
age = 99
if age < 4:
    print('You admission fee is $0.')
elif age < 18:
    print('Your addmission fee is $5.')
else:
    print('Your admission fee is $10.')
# %%
age = 32
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")

# %%
requested_toppings = ['mushrooms', 'pepperoni', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print('Add mushrooms')
if 'pepperoni' in requested_toppings:
    print('Add peeperoni')
if 'extra cheese' in requested_toppings:
    print('Add extra cheese')
if 'olives' in requested_toppings:
    print('Add olives')
print('\nFinished making your pizza!')
# %%
alien_color = 'yellow'
if alien_color == 'green':
    print('Player 1 gets 5 points!')
else:
    print('Player 1 gets 0 points!')
# %%
alien_color = 'green'
if alien_color == 'green':
    print('Player 1 gets 5 points!')
if alien_color != 'green':
    print('Player 1 gets 10 points!')

# %%
alien_color = 'green'
if alien_color == 'green':
    print('Player 1 gets 5 points!')
if alien_color == 'yellow':
    print('Player 1 gets 10 points!')
if alien_color == 'red':
    print('Player 1 gets 15 points!')

# %%
person_age = 15
if person_age < 2:
    print('Person is a baby')
elif person_age == 2 or person_age < 4:
    print('Person is a toddler')
elif person_age == 4 or person_age < 13:
    print('Person is a kid')
elif person_age == 13 or person_age < 20:
    print('Person is a teenager')
elif person_age == 20 or person_age < 65:
    print('Person is an adult')
else:
    print('Person is an elder')
# %%
person_age = 4
if person_age < 2:
    print('Person is a baby')
elif person_age < 4:
    print('Person is a toddler')
elif person_age < 13:
    print('Person is a kid')
elif person_age < 20:
    print('Person is a teenager')
elif person_age < 65:
    print('Person is an adult')
else:
    print('Person is an elder')
# %%
favorite_fruit = ['banana', 'kiwi', 'apple', 'pear']
if 'banana' in favorite_fruit:
    print('I love bananas!')
if 'strawberry' in favorite_fruit:
    print('I love strawberry!')
if 'kiwi' in favorite_fruit:
    print('I love Kiwi!')
for fruits in favorite_fruit:
    print("\nMy favorite fruits are " + (fruits) + ".")

# %%
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
# %%
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
# %%
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")
# %%
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
# %%
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
# %%
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# %%
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
# %%
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")
# %%
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))
# %%
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
# %%
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() + ".")
# %%
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
for k, v in user_0.items():
    print("\nKey: " + k)
    print("Value: " + v)
# %%
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

# %%
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in favorite_languages.keys():
    print(name.title())
# %%
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in favorite_languages:
    print(name.title())
# %%
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi  " + name.title() +
              ",I see you favorite language is " +
              favorite_languages[name].title() + "!")
# %%
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
# %%
# loop through keys
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
# %%
# Loop through all values
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# %%
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
# %%
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# %%
aliens = []
# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Make three aliens green 10 medium
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = '10'
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = '15'
        alien['speed'] = 'fast'

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))
# %%
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
# %%
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
# %%
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
# %%
message = input("Tell me something, and I will repeat it back to you:")
print(message)

# %%
name = input("Please enter your name: ")
print("Hello, " + name.title() + "!")

# %%
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name.title() + "!")

# %%
age = input("How old are you? ")
print(age)

# %%
age = input('How old are you?')
age = int(age)
age >= 18
# %%
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
# %%
4 % 3  # 1
# %%
5 % 3  # 2

# %%
6 % 3  # 0
# %%
7 % 3  # 1
# %%
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
# %%
prompt = ("What type of car do you like?")
prompt += "\nLet's see if we can find you a: "
car = input(prompt)
print("\nHere is your " + car.title() + "!")

# %%
number = input("How many people are in your party?")
number = int(number)
if number > 9:
    print("Sorry, but your group of " + str(number) +
          " will have to wait for a table.")
else:
    print("Your table for " + str(number) + " is now ready!")

# %%
number = input("Enter a number, and I'll tell you if its divisible by 10: ")
number = int(number)
if number % 10 == 0:
    print("\nThe number " + str(number) + " is divisible by 10.")
else:
    print("\nThe number " + str(number) + " is not divisible by 10.")
# %%
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
# %% User enter quit value
prompt = "Tell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# %% Flag = active = True
prompt = "Tell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
# %%
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
# %% # Prints odd numbers with continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
# %% # Infinite Loops
x = 1
while x <= 5:
    print(x)
# %% # Enter pizza toppings
prompt = "\nPlease enter a topping to add to your pizza: "
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print("Please add " + topping.title() + " to my pizza!")

# %%
prompt = ("How old are you?")
prompt += ("\nEnter 'quit' when you are finished.")
while True:
    age = input(prompt)
    if prompt == 'quit' or ' ':
        break
    elif int(age) < 2:
        print("You are " + str(age) + " years old and your ticket is Free!")
    elif int(age) <= 11:
        print("You are " + str(age) + " years old and your ticket is $10!")
    elif int(age) > 12:
        print("You are " + str(age) + " years old and your ticket is $15!")


# %%
prompt = ('How old are you?')
prompt += ("\nEnter 'quit' when you are finished.")
while active:
    message = int(input(prompt))
    if message == str('quit'):
        active = False
    elif message < 2:
        print(f"You are {message} years old and your ticket is Free!")
    elif message <= 12:
        print(f"You are {message} years old and your ticket is $10!")
    elif message >= 13:
        print(f"You are {message} years old and your ticket is $15!")

# %%
keepGoing = True

try:
    age = int(input("what is your age: "))
except:
    age == "quit" or " "
    print("you entered invalid stuff")
    keepGoing = False
while keepGoing:
    if age < 2:
        print(f"your ticket is free infant {age} years old")
    elif age < 11:
        print(f"your ticket is $10, you're {age} years old")
    elif age > 12:
        print(f"your ticket is $15, since you're {age} years old")


# %%
prompt = ("\nHow old are you?")
prompt += ("\nEnter 'quit' when you are finished.")
while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(input(prompt))
        if age < 2:
            print(f"You are {age} years old and your ticket is Free!")
        elif age <= 12:
            print(f"You are {age} years old and your ticket is $10!")
        elif age >= 13:
            print(f"You are {age} years old and your ticket is $15!")


# %%
# I am the one!
prompt = ("\nEnter 'quit' when you are finished. ")
prompt += ("\nHow old are you?")
while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        if int(age) < 2:
            print(f"You are {age} years old and your ticket is Free!")
        elif int(age) <= 12:
            print(f"You are {age} years old and your ticket is $10!")
        elif int(age) >= 13:
            print(f"You are {age} years old and your ticket is $15!")


# %%
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
# %%
# remove() method with while loop
pets = ['dog', 'cat', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
# %%
# Filling a dictonary with user response from polling
responses = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
# Store the response in the dictionary:
    responses[name] = response
# Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

# %%


def greet_user():
    """Display a simple greeting."""
    print('Hello!')


greet_user()
# %%


def greet_user(username):
    """Display a simple greeting."""
    print('Hello, ' + username.title() + "!")


greet_user('chris')
# %%


def display_message():
    """prints message"""
    print("This is the message I wanted to display")


display_message()
# %%


def favorite_book(title):
    print('One of my favorite books is ' + title.title())


favorite_book("alice in wonderland")
# %%


def describe_pet(animal_type, pet_name):
    """Display needed information about pets"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')
# %%


def describe_pet(animal_type, pet_name):
    """Display needed information about pets"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')
describe_pet('chihuahua', 'skippy')
describe_pet('cat', 'bella')
describe_pet('goldfish', 'orange')
# %%


def describe_pet(animal_type, pet_name):
    """Display needed information about pets"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(animal_type='chihuahua', pet_name='skippy')
# %%


def describe_pet(pet_name, animal_type='dog'):
    """Display needed information about pets"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('harry')
describe_pet('skippy')
# %%


def make_shirt(size, message):
    print('Your shirt size is ' + size.title() +
          ' and the message on it is: ' + message + ".")


make_shirt("large", "I love Python!")
make_shirt("medium", "I love Programming!")
make_shirt("small", "I love Web Development!")
# %%


def make_shirt(message, size="Large"):
    print('Your shirt size is ' + size.title() +
          ' and the message on it is: ' + message + ".")


make_shirt("I love Python!")
make_shirt("I love Programming!")
make_shirt("I love Web Development!", size="small")

# %%


def get_formatted_name(first_name, last_name):
    """Return full name formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
# %%


def get_formatted_name(first_name, middle_name, last_name):
    """Return full name formatted"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
# %%


def get_formatted_name(first_name, last_name, middle_name=''):
    """Return full name formatted"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# %%


def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)
# %%


def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
soldier = build_person('john', 'smith')
print(musician)
print(soldier)
# %%
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
# # This is an infinite loop!
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")

# %%


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
# %%


def city_state(city, state):
    cc = {'city': city, 'state': state}
    return cc


current_place = city_state('Florence', 'South Carolina')
print(current_place)

# %%


def make_album(artist_name, artist_title, tracks=''):
    """Write a function called make_album() that builds a dictionary
describing a music album"""
    album = {'name': artist_name, 'title': artist_title}
    if tracks:
        album['tracks'] = tracks
    return album


iron_madien = make_album('Iron Madien', 'Life After Death', tracks=12)
black_sabbath = make_album('Black Sabbath', 'War Pigs')
print(iron_madien)
print(black_sabbath)

# %%


def get_album(artist_name, artist_title, tracks):
    """Return a full album with user input."""
    full_album = {artist_name: 'artist_name',
                  artist_title: 'artist_title', tracks: 'tracks'}
    return full_album


while True:
    print("\nPlease enter artist name:")
    print("(enter 'q' at any time to quit)")
    artist_name = input("artist name: ")
    if artist_name == 'q':
        break
    artist_title = input("artist title: ")
    if artist_title == 'q':
        break
    tracks = input("tracks: ")
    if tracks == 'q':
        break
    full_album_info = get_album(artist_name, artist_title, tracks)
    print(full_album_info)

# %%


def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['hanna', 'ty', 'margot']
greet_users(usernames)

# %%
# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)
# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
# %%


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# %%
"""Make a list of magician’s names"""


def magicians_names(names):
    for magicians in names:
        printed_names = "Hello, " + magicians.title() + "!. Happy to have you here."
        print(printed_names)


current_magicians = ['chris', 'john', 'sue', 'sarah']
magicians_names(current_magicians)

# %%
"""RIVIST PAGE 180 OF 562 Try it yourself 8-10 8-11"""

# %%


def make_pizza(*toppings):
    """
    Stores in a Tuple called toppings.
    Print the list of toppings that have been requested.
    """
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# %%


def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# %%


def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# %%


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton', field='physics')
print(user_profile)

# %%
"""pizza.py"""


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


""" 
Make file called making_pizza.py must be in same dir as pizza.py

import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
"""
# %%


class Dog():
    """Simple dog model"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " roll over!")


my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " year old.")
my_dog.sit()
my_dog.roll_over()

# %%
"""Python 2.7 class"""
# class Dog():
# --snip--
# u my_dog = Dog('willie', 6)
# v print("My dog's name is " + my_dog.name.title() + ".")
# w print("My dog is " + str(my_dog.age) + " years old.")

# %%

# %%


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.resaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.resaurant_name.title()
              + " is awesome place to eat. They make the best "
              + self.cuisine_type.title() + "!")


one_restaurant = Restaurant('chuckies', 'hamburgers')
two_restaurant = Restaurant('churches', 'fried chicken')
three_restaurant = Restaurant('zaxybys', 'chicken wings')
one_restaurant.describe_restaurant()
two_restaurant.describe_restaurant()
three_restaurant.describe_restaurant()
# %%


class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles < 0:
            print("Nice try, you have to use positive numbers!")
        else:
            self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23000
my_new_car.read_odometer()
my_second_car = Car('mustang', 'ford', 2019)
print(my_second_car.get_descriptive_name())
my_second_car.odometer_reading = 12999
my_second_car.read_odometer()
my_used_car = Car('suburu', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
my_used_car.increment_odometer(-100)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
# %%


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")

    def increment_odometer(self, miles):
        if miles < 0:
            print("Nice try, you have to use positive numbers!")
        else:
            self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
# %%
# Inheritance in Python 2.7
# In Python 2.7, inheritance is slightly different. The ElectricCar class would
# look like this:
# class Car(object):
#     def __init__(self, make, model, year):
#         --snip--
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super(ElectricCar, self).__init__(make, model, year)
#         --snip--
# %%


# class Car():
#     --snip--


class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

# %%

favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is "
          + language.title() + ".")

# %%
x = randint(1, 6)
print(x)
y = randint(1, 100)
print(y)
z = randint(1, 20)
print(z)


# %%
x = "y"

while x == "y":

    # Gnenerates a random number
    # between 1 and 6 (including
    # both 1 and 6)
    no = random.randint(1, 6)

    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  1  ]")
        print("[     ]")
        print("[-----]")
    if no == 2:
        print("[-----]")
        print("[ 2   ]")
        print("[     ]")
        print("[   2 ]")
        print("[-----]")
    if no == 3:
        print("[-----]")
        print("[     ]")
        print("[3 3 3]")
        print("[     ]")
        print("[-----]")
    if no == 4:
        print("[-----]")
        print("[4   4]")
        print("[     ]")
        print("[4   4]")
        print("[-----]")
    if no == 5:
        print("[-----]")
        print("[5   5]")
        print("[  5  ]")
        print("[5   5]")
        print("[-----]")
    if no == 6:
        print("[-----]")
        print("[6 6 6]")
        print("[     ]")
        print("[6 6 6]")
        print("[-----]")

    x = input("press y to roll again and n to exit:")
    print("\n")
# %%

question = input('Would you like to roll the dice [y/n]?\n')

while question != 'n':
    if question == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(die1, die2)
        question = input('Would you like to roll the dice [y/n]?\n')
    else:
        print('Invalid response. Please type "y" or "n".')
        question = input('Would you like to roll the dice [y/n]?\n')

print('Good-bye!')
# %%
# %%
""" Open text file pi_digits.txt and strips white space """
with open('/home/chris/Desktop/projects/morepythonpractice/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# %%
# """ How to open a text files thats in a different folder"""
# with open('text_files/filename.txt') as file_object:

# %%
""" Reading file line by line """
filename = '/home/chris/Desktop/projects/morepythonpractice/pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# %%
""" Making list of lines from a file .readlines() method """
filename = '/home/chris/Desktop/projects/morepythonpractice/pi_digits.txt'
with open(filename) as file_object:
    for line in file_object.readlines():
        print(line.rstrip())
# %%
""" Working with the file contents, build single string no white space """
filename = '/home/chris/Desktop/projects/morepythonpractice/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))

# %%
""" Open one million digits of pi """
filename = 'millionpi.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
# %%
""" Slice the first 52 numbers and return length of txt"""
filename = "millionpi.txt"
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string[:52] + "...")
print(len(pi_string))

# %%
""" Is your birthday on pi"""
filename = "millionpi.txt"
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
birthday = input("Enter your birthday, in the for of mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does NOT appear in the first million digits of pi!")

# %%
""" use the replace() method to replace any word in a
string with a different word """
message = "I really love cats!"
message.replace("cats", "dogs")

# %%
filename = 'learning_python.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())
        print(len(line))
# %%
filename = 'learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))
# %%
"""To write text to a file, you need to call open() with a second argument telling
Python that you want to write to the file."""
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming!")
# %%
"""newlines in your write() statements makes each string appear
on its own line"""
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
# %%
filename = 'programming.txt'
with open(filename, "a") as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
# %%
# asuming python3.x
# for py 2.x input should be raw_input
# input1 = input("first input:")
# input2 = input("second input:")
# file = open("somefile.txt", "w")
# file.write(input1 + "\n")
# file.write(input2 + "\n")
# file.close()

filename = "guest.txt"
input_firstname = input("Enter your first name: ")
input_lastname = input("Enter your last name: ")
file = open(filename, "w")
file.write(input_firstname.title() + ' ' + input_lastname.title() + "\n")
file.close()
# %%
""" use a while loop to create a guest book"""
filename = "guest_book.txt"
with open(filename, 'a') as f:
    while True:
        full_name = input("Enter your full name: ")
        if full_name == "exit":
            break
        f.write(full_name.title() + '\n')
        f.flush()
        print(f"You have been added to the guest book, {full_name}")

# %%
"""
ZeroDivisionError: division by zero
"""
print(5/0)

# %%
""" Using try-except Blocks"""
try:
    print(5/0)
except ZeroDivisionError:
    print("You cant divide by zero!")

# %%
"""Else Block"""
print("Give me two numbers and I will divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print(answer)
# %%
"""Handling the FileNotFoundError Exception"""
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
        print(contents)
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

# %%
"""count words in alice in wonderland"""
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
# %%


def count_words(filename):
    """Count the approximate words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
              " words.")


filename = 'alice.txt'
count_words(filename)
# %%
""" Working with Multiple Files """


def count_words(filename):
    """Count the approximate words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
              " words.")


filenames = ['alice.txt', 'siddhartha.txt',
             'moby_dick.txt', 'little_women.txt', 'unknown.txt']
for filename in filenames:
    count_words(filename)
# %%
"""pass statement, silently passes over stated error"""
# def count_words(filename):
#   """Count the approximate number of words in a file."""
#   try:
#       --snip--
#   except FileNotFoundError:
#       pass
#   else:
#       --snip--
# filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
# for filename in filenames:
# count_words(filename)

# %%
"""Create .json with numbers in list """
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
# %%
"""Read .json file an return list"""
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)
# %%
"""Store data in JSON file"""
username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
# %%
"""Read data from JSON files"""
filename = 'username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username.title() + "!")
# %%
"""Load the username, if it has been stored previously.
Otherwise, prompt for the username and store it."""

# %%
# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.


def greet_user():
    """Greet the user by name"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")


greet_user()
# %%
"""Refactor """


def get_stored_username():
    """Get stored username if avalible"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    """Greet user by name."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = input("What's your name?")
        filename = 'username.json'
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remeber you when you come back, " + username + "!")


greet_user()

# %%
# TESTING FUNCTIONS
print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')
# %%
# Table 11-1: Assert Methods Available from the unittest Module
# Method Use
# assertEqual(a, b) Verify that a == b
# assertNotEqual(a, b) Verify that a != b
# assertTrue(x) Verify that x is True
# assertFalse(x) Verify that x is False
# assertIn(item, list) Verify that item is in list
# assertNotIn(item, list) Verify that item is not in list
# %%


class AnonymousSurvey():
    # Testing a class
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in responses:
            print('- ' + response)

# %%


class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()
# %%
