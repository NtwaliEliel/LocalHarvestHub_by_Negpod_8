#!/usr/bin/python3

def display_menu():
    print("Welcome to LocalHarvestHub!")
    print("1. View available products")
    print("2. Buy products")
    print("3. Sell products")
    print("4. Exit")

def view_products():
    print("Available Products:")
    products = {
        "Apples": 2.50,
        "Oranges": 1.75,
        "Tomatoes": 3.00,
        "Carrots": 1.50,
        "Cabbage": 4.00,
        "Bananas": 3.50  
    }
    print("Product\t\tPrice")
    print("---------------------")
    for product, price in products.items():
        print(product + "\t\t" + str(price))

def buy_products():
    print("Buying Products:")
    """Assuming products and prices are stored in a dictionary"""
    products = {
        "Apples": 2.50,
        "Oranges": 1.75,
        "Tomatoes": 3.00,
        "Carrots": 1.50,
        "Cabbage": 4.00
    }

    print("Product\t\tPrice")
    print("---------------------")
    for product, price in products.items():
        print(product + "\t\t" + str(price))

def sell_products():
    print("Selling Products:")
    """Allow users to list their own products for sale"""
    product_name = input("Enter the product name: ")
    print("DEBUG: product_name =", product_name)
    try:
        product_price = float(input("Enter the product price: "))
        print("DEBUG: product_price =", product_price)
    except ValueError:
        print("Invalid price. Please enter a valid number.")
        return  
    """Return to the menu without proceeding further"""
    print("Your product '" + product_name + "' has been listed for sale at $" + str(product_price) + ".")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            view_products()
        elif choice == "2":
            buy_products()
        elif choice == "3":
            sell_products()
        elif choice == "4":
            print("Thank you for using LocalHarvestHub. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
