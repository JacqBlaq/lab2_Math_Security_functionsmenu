"""command line menu-driven python application providing users with the
ability to perform several math and security related functions"""
import sys
import string
import secrets
import datetime
import math

valid_binary_entries = ["y", "n"]


def goodbye():
    """Print out goodbye message and exit app"""
    print("\nHave a good day. Goodbye!")
    sys.exit()


def invalid_input():
    """Method to print out message to let user know only 'yes' or 'no' values are allowed"""
    print("\nPlease only enter a \'y\' for yes or a \'n\' for no: ")


def set_password_requirement(user_input, question):
    """Method to check that user entered a valid input for password requirements"""
    while not user_input or not user_input.isalpha() or user_input not in valid_binary_entries:
        invalid_input()
        user_input = input(question)

    return user_input


def secure_password():
    """Method that creates secure password for user then outputs newly generated password"""
    alphabet = string.ascii_letters
    password = ''

    length = input("Enter desired password length greater than 8 but less than 25: ")
    while not length or not length.isnumeric():
        length = input("Please enter a valid number for your desired password length: ")

    while int(length) < 8:
        length = input("Please enter a password length greater than 8: ")

    while int(length) > 25:
        length = input("Please enter a password length less than 25: ")

    print("\nEnter a \'y\' for yes or \'n\' for no for the next set of questions: ")

    has_numbers = input("Would you like to implement numbers? ")
    has_numbers = set_password_requirement(has_numbers, "Would you like to implement numbers? ")

    if has_numbers.lower() == 'y':
        alphabet += string.digits

    has_special_characters = input("Would you like to implement special characters? ")
    has_special_characters = set_password_requirement(
        has_special_characters, "Would you like to implement special characters? ")

    if has_special_characters.lower() == 'y':
        alphabet += string.punctuation

    if has_numbers.lower() == 'y':
        char = ''.join(
            secrets.choice(
                ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']) for i in range(int(1)))
        password += char

    if has_special_characters.lower() == 'y':
        char = ''.join(
            secrets.choice(
                ['!', '\"', '#', '$', '%', '&', '\'', '(', ')', '*', '+',
                 ',', '-', '.', '/', ':', ';', '<', '=', '>', '?',
                 '@', '[', '\'', ']', '^', '_', '`', '{', '|', '}', '~']) for i in range(int(1)))
        password += char

    generated_password = ''.join(
        secrets.choice(alphabet) for i in range(int(length) - len(password)))

    print('Your secure password is: ' + password + generated_password)


def calculate_percentage():
    """Method to calculate percentage based on user inputs"""
    numerator = input("Enter numerator: ")
    while not numerator or not numerator.isnumeric():
        numerator = input("Please enter a valid number for the numerator: ")

    denominator = input("Enter denominator: ")
    while not denominator or not denominator.isnumeric():
        denominator = input("Please enter a valid number for the denominator: ")

    decimal_places = input("Enter how many decimal places for formatting: ")
    while not decimal_places or not decimal_places.isnumeric():
        decimal_places = input("Please enter a valid number for the "
                               "decimal places (Nothing more than 5): ")

    while int(decimal_places) > 5:
        decimal_places = input("Please enter a number less than 6 for the decimal places: ")

    formatted_string = ("{:." + decimal_places + "f}").format((int(numerator) / int(denominator)))
    float_value = float(formatted_string)
    print('Percentage: ', float_value)


def days_util():
    """Calculate how many days left till July 6th, 2025"""
    today = datetime.date.today()
    future = datetime.date(2025, 6, 4)
    diff = future - today
    print('Days left till: ', diff.days)


def calculate_triangle_leg():
    """Method to calculate the law of cosines based on user input"""
    print("Law of Cosines \n")
    a_side = input("What is the length of \'a\': ")
    while not a_side or not a_side.isnumeric():
        a_side = input("Please enter a valid number for length of \'a\': ")

    b_side = input("What is the length of \'b\': ")
    while not b_side or not b_side.isnumeric():
        b_side = input("Please enter a valid number for length of \'b\': ")

    c_degree = input("How many degrees is angle \'C\'? ")
    while not c_degree or not c_degree.isnumeric():
        c_degree = input("Please enter a valid number. How many degrees is angle \'C\'? ")

    a_result = (int(a_side) ** 2)
    b_result = (int(b_side) ** 2)

    c_side = a_result + b_result - (2 * int(a_side) * int(b_side) * math.cos(int(c_degree)))

    print("Law of cosines: ", math.sqrt(c_side))


def calculate_cylinder_volume():
    """Method to calculate the volume of the right circular cylinder"""
    height = input("What is the height of the cylinder: ")
    while not height or not height.isnumeric():
        height = input("Please enter a valid number. What is the height of the cylinder: ")

    radius = input("What is the radius of the cylinder: ")
    while not radius or not radius.isnumeric():
        radius = input("Please enter a valid number. What is the radius of the cylinder: ")

    volume = math.pi * (int(radius) ** 2) * int(height)

    print("Volume of the right circular cylinder: ", volume)


def main():
    """Main method with menu for user to select an action from"""
    print("Welcome to Jackie\'s One Stop Utility Shop.\n"
          "Here you can do one of the following tasks: \n\n"
          "a. Generate secure password\n"
          "b. Calculate and format a percentage\n"
          "c. How many days from today until July 4, 2025?\n"
          "d. Use the law of cosines to calculate the leg of a triangle\n"
          "e. Calculate the volume of a right circular cylinder\n"
          "f. Exit program")
    option = input("\nWhat would you like to do? \n"
                   "Enter \'a\' through \'e\' or to exit program enter \'f\': ")

    valid_inputs = ['a', 'b', 'c', 'd', 'e', 'f']

    while not option or option not in valid_inputs:
        option = input("\nOops, you may have accidentally entered an invalid entry. \n"
                       "Please only enter \'a\' through \'e\' or to exit program enter \'f\': ")

    option = option.lower()

    if option == 'f':
        goodbye()

    if option == 'a':
        secure_password()

    if option == 'b':
        calculate_percentage()

    if option == 'c':
        days_util()

    if option == 'd':
        calculate_triangle_leg()

    if option == 'e':
        calculate_cylinder_volume()


main()
