from auth.authentication import register, login
from orders.user_orders import menu, place_order
import maskpass

def authentication_menu():
    while True:
        print("\n--- Welcome to the Food Delivery Application. Please register or login to continue ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = maskpass.askpass("Enter your password: ")
            address = input("Enter your address: ")
            role = input("Enter your role (customer/manager): ")

            if role not in ['customer', 'manager']:
                print("Invalid role. Please try again.")
                continue

            success = register(name, password, email, address, role)
            if success:
                print("Registration successful. Please login to continue.")
            else:
                print("Registration failed. Please try again.")

        elif choice == "2":
            email = input("Enter your email: ")
            password = maskpass.askpass("Enter your password: ")

            user = login(email, password)
            if user:
                print(f"Login successful. Welcome {user['name']}! logged in as a {user['role']}")
                return user
            else:
                print("Login failed. Please try again.")

        elif choice == "3":
            print("Exiting...")
            exit()

        else:
            print("Invalid choice. Please try again.")

def display_menu():
    menu = menu()
    print("\n--- Menu ---")
    for item in menu:
        print(f"{item['id']}. {item['name']} - ${item['price']}")
    print()

def order_food(user):
    display_menu()
    while True:
        try:
            item_id = int(input("Enter the item number to order (or 0 to go back): "))
            if item_id == 0:
                return
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Invalid quantity. Please try again.")
                continue

            success = place_order(user['id'], item_id, quantity)
            if success:
                print("Order placed successfully.")
            else:
                print("Order failed. Please try again.")

            choice = input("Do you want to order more items? (y/n): ")
            if choice.lower() != 'y':
                break
        except ValueError:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    user = authentication_menu()

    if user and user['role'] == 'customer':
        while True:
            print("\n--- Welcome to the Food Delivery Application ---")
            print("1. View Menu")
            print("2. Order Food")
            print("3. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                display_menu()
            elif choice == "2":
                order_food(user)
            elif choice == "3":
                print("Logging out...")
                user = authentication_menu()
            else:
                print("Invalid choice. Please try again.")
