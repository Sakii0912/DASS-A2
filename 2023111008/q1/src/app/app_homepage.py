"""
This module contains the homepage (cli) of the application.
"""

def display_homepage():
    print("Welcome to the Food Delivery App!")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

def display_login(): #TODO implement login verification pending
    print("Enter your login details:")
    username = input("Username: ")
    password = input("Password: ")
    return username, password

def display_register():
    print("Enter your details to register:")
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")
    address = input("Address: ")
    return username, password, email, address

def display_food_items(items_list): #* Items list can be hard coded mostly since its under the restaurants control
    print("Available food items:")
    for i, item in enumerate(items_list):
        print(f"{i+1}. {item['name']} - {item['price']}")
    print("0. Go back")
    choice = input("Enter your choice: ")
    return choice

def main_menu():
    while True:
        choice = display_homepage()
        if choice == '1':
            username, password = display_login()
            #TODO implement login verification
        elif choice == '2':
            username, password, email, address = display_register()
            #TODO implement registration
        elif choice == '3':
            print("Exiting the application...")
            break
        else:
            print("Invalid choice. Please try again.")
