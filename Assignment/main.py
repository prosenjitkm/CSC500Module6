from ShoppingCart import ShoppingCart
from ItemToPurchase import ItemToPurchase

def print_menu(cart):

    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        option = input("Choose an option: ")

        if option == 'a':
            name = input("Enter the item name: ")
            description = input("Enter the item description: ")
            price = int(input("Enter the item price: "))
            quantity = int(input("Enter the item quantity: "))
            item = ItemToPurchase(name, description, price, quantity)
            cart.add_item(item)

        elif option == 'r':
            item_name = input("Enter the name of the item to remove: ")
            cart.remove_item(item_name)

        elif option == 'c':
            name = input("Enter the item name to modify: ")
            description = input("Enter the new description (or 'none' to keep current): ")
            price = int(input("Enter the new price (or 0 to keep current): "))
            quantity = int(input("Enter the new quantity (or 0 to keep current): "))
            modified_item = ItemToPurchase(name, description, price, quantity)
            cart.modify_item(modified_item)

        elif option == 'i':
            cart.print_descriptions()

        elif option == 'o':
            cart.print_total()

        elif option == 'q':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

def main():

    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    cart = ShoppingCart(customer_name, current_date)

    print(f"\nCustomer Name: {customer_name}")
    print(f"Today's Date: {current_date}")

    print_menu(cart)

if __name__ == "__main__":
    main()