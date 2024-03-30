#!/usr/bin/python3

def starting_menu():
    print("Welcome to LocalHarvestHub!")
    print("1. I am a farmer")
    print("2. I am a Market Provider")
    print("0. Exit")

def Farmer_menu():
    print("Welcome to LocalHarvestHub!")
    print("Market Provider!")
    print("1. View available stock")
    print("2. Enter available stock")
    print("3. Enter your location")
    print("4. Sell product")
    print("0. Exit")

def Inserting_Available_stock():
    Available_Products = input("Enter available products separate them with space : ")
    product = Available_Products.split()
    print("Your Stoke contains:", product)

def Market_provider_menu():
    print("Welcome to LocalHarvestHub!")
    print("Market Provider!")
    print("1. View available products")
    print("2. Enter your location")
    print("3. Buy products")
    print("0. Exit")
def view_products():
    print("Available Products:")
    """Code to display available products"""

def Location_set_up():
    print("Enter your working address:")
    """code to set up working address"""

def buy_products():
    print("Buying Products:")
    """Assuming products and prices are stored in a dictionary"""
    products = {
        "Apples": 2.50,
        "Oranges": 1.75,
        "Tomatoes": 3.00,
        "Carrots": 1.50
    }

    print("Product\t\tPrice")
    print("---------------------")
    for product, price in products.items():
        print(product + "\t\t" + str(price))


def sell_products():
    print("Selling Products:")
    # Code for selling products


def main():
    while True:
        starting_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            Farmer_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                view_products()
            elif choice == "2":
                Inserting_Available_stock()
            elif choice == "3":
                Location_set_up()
            elif choice == "4":
                sell_product()
            elif choice == "0":
                print("Thank you for using LocalHarvestHub. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

        elif choice == "2":
            Market_provider_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                view_products()
            elif choice == "2":
                Location_set_up()
            elif choice == "3":
                buy_products()
            elif choice == "0":
                print("Thank you for using LocalHarvestHub. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

        elif choice == "0":
            print("Thank you for using LocalHarvestHub. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
