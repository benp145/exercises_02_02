import my_module as geo

# Exercise 1

def print_instructions():
    print("""
Enter 'Add' to add a new item to your cart.
Enter 'Show' to see all items in your cart.
Enter 'Delete' to delete an item from your cart.
Enter 'Quit' to end program. \n""")
    print("="*8)

def shopping_cart():
    print("\nWelcome to your shopping cart!")
    print("="*40)
    input("\nPress enter to begin: ")
    
    cart = []
    done = False

    while not done:
        print_instructions()
        print("What would you like to do?")
        prompt = input("Add | Show | Delete | Quit ")
        if prompt.lower() == 'add':
            new_item = input("\nEnter the item you wish to add to cart: ")
            cart.append(new_item.title())
            input("\nItem added to cart! press enter to continue: ")
        elif prompt.lower() == 'show':
            print("\nHere are the items in your cart:")
            for item in cart:
                print(item)
            input('\nPress enter to continue: ')
        elif prompt.lower() == 'delete':
            deleted_item = input('\nEnter the item you wish removed from your cart: ')
            cart.remove(deleted_item.title())
            input('\nItem deleted from cart! Press enter to continue: ')
        elif prompt.lower() == 'quit':
            print("\nThank you for shopping with us!")
            break
        else:
            input("\nInvalid Input. press enter to continue: ")

shopping_cart()

print("\n"*2)
# Exercise 2

geo.room_sq_footage()
geo.circumference()