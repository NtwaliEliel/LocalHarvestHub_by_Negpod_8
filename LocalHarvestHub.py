#!/usr/bin/python3

def starting_menu():
    print("Welcome to LocalHarvestHub!")
    print("1. I am a farmer")
    print("2. I am a buyer")
    print("0. Exit")

def Farmer_menu():
    print("Welcome to LocalHarvestHub!")
    print("FARMER!")
    print("1. View available stock")
    print("2. Enter available stock")
    print("3. Enter your location")
    print("4. Sell product")
    print("5. Delete product")
    print("0. Exit")

def Inserting_Available_stock():
    Available_Products = input("Enter available products separated by space: ")
    product = Available_Products.split()
    print("Your Stock contains:", product)

def Delete_Product():
    product_name = input("Enter the product name to delete: ")
    print(product_name + " has been deleted from your stock")

def Set_Location_Farmer():
    address = input("Enter your working address: ")
    print("Your working address is:", address)
    print("Location successfully set!")
    return address

def buyer_menu():
    print("Welcome to LocalHarvestHub!")
    print("BUYER!")
    print("1. View available products")
    print("2. Enter your location")
    print("3. Buy products")
    print("0. Exit")

def view_products():
    print("Available Products:")
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

def Set_Location_Buyer():
    address = input("Enter your working address: ")
    print("Your working address is:", address)
    print("Location successfully set!")
    return address

def buy_products():
    products = {
        "Apples": 2.50,
        "Oranges": 1.75,
        "Tomatoes": 3.00,
        "Carrots": 1.50
    }

    print("Product\t\tPrice")
    print("---------------------")
    for product, price in products.items():
        print(product + "\t\t$" + str(price))

    choice = input("Enter the product you want to buy: ")
    if choice in products:
        print("You have purchased " + choice + " for $" + str(products[choice]))
    else:
        print("Invalid choice. Please try again.")

def sell_products():
    print("Selling Products:")
    product_name = input("Enter the product name: ")
    try:
        product_price = float(input("Enter the product price: "))
        print("Your product '" + product_name + "' has been listed for sale at $" + str(product_price) + ".")
    except ValueError:
        print("Invalid price. Please enter a valid number.")
        return

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
                address = Set_Location_Farmer()
            elif choice == "4":
                sell_products()
            elif choice == "5":
                Delete_Product()
            elif choice == "0":
                print("Thank you for using LocalHarvestHub. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

        elif choice == "2":
            buyer_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                view_products()
            elif choice == "2":
                address = Set_Location_Buyer()
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
