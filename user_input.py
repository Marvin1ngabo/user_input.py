# user_input.py

name = input("What is your name? ")
age = int(input("How old are you? "))
location = input("Where do you live? ")

personalized_message = f"Hello {name}, you are {age} years old and live in {location}.\n"
print(personalized_message)