from csv import reader

open_file = open('Komodo_Miami_Food_Menu.csv', 'r')
read_file = reader(open_file)

menu = list(read_file)[1:]

menu_dict = {}

app_action = {1: "Add item to cart", 2: "Remove item from cart", 3: "Modify order", 4: "View Cart", 5: "Checkout", 6: "Exit"}

sales_tax = 0.07

cart = {}

# Compiling the menu in a nested dictionary from a nested list
for row in menu:
    sku = row[0]
    name = row[1]
    price = float(row[2])

    inner_dict = {name: price}
    
    menu_dict[sku] = inner_dict

# Display the menu to the customer
def display_menu():
    print('\n')
    print("****Menu****")

    for sku in menu_dict:
        sku_num = sku[3:]  # Assuming SKU is in the format 'sku1', 'sku2', etc.
        for name in menu_dict[sku]:
            menu_item_name = name
            price = menu_dict[sku][name]
            print(f"{sku_num} {menu_item_name}: ${price:.2f}")

display_menu()

# Adding menu items to the cart
def add_to_cart(sku, quantity):
    sku = "sku" + str(sku)  # Ensuring the format matches 'sku1', 'sku2', etc.

    if sku not in menu_dict:
        print("This is not a valid entry. Please try again!")
    
    else:
        name_container = []
        for row in menu:
            if sku == row[0]:
                name_container.append(row[1])

        if sku in cart:
            cart[sku] += quantity
        
        else:
            cart[sku] = quantity

        print('\n')
        print(f"Added {cart[sku]} of {name_container[0]} to the cart.")

add_to_cart(3, 2)

# Removing menu items from the cart
def remove_from_cart(sku):
    sku = "sku" + str(sku)
    
    if sku in cart:
        removed_item = cart.pop(sku)

        item_name = None

        for row in menu:
            if sku == row[0]:
                item_name = row[1]
                break
        print(f"Removed {removed_item} of {item_name} from the cart.")

    else:
        print("The SKU item you entered is not in the cart. Please try again.")

remove_from_cart(2)

# Modifying or changing the order in the cart
def modify_cart(sku, quantity):
    sku = "sku" + str(sku)
    quantity = int(quantity)

    if sku in cart:
        if quantity > 0:
            cart[sku] = quantity
        else:
            remove_from_cart(sku)

        item_name = None

        for row in menu:
            if sku == row[0]:
                item_name = row[1]
                break
        print(f"Modified {item_name} quantity to {quantity} in cart.")

# Viewing cart order
def view_cart():
    print('\n')
    print("****Cart Contents****")

    subtotal = 0

    for sku in cart:
        quantity = cart[sku]
        for name in menu_dict[sku]:
            price = menu_dict[sku][name]
            subtotal += price * quantity
            print(f"{quantity} x {name} = ${price * quantity:.2f}")

    tax = subtotal * sales_tax
    total = subtotal + tax

    print('\n')
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")

view_cart()

# Checking out the order in the cart
def checkout():
    print('\n')
    print("****Checkout****")
    view_cart()
    print('\n')
    print("Your order is submitted and being processed.")

checkout()

# Entering the order and quantity of menu items
def get_sku_and_quantity(sku_prompt, quantity_prompt=None):

    item_sku = input(sku_prompt)
    item_sku = "sku" + item_sku

    if quantity_prompt:
        quantity = input(quantity_prompt)
        if quantity.isdigit():
            quantity = int(quantity)
        else:
            quantity = 1
        return item_sku, quantity
    return item_sku

def order_loop():
    print("Welcome to Komodo Miami!")

    app_running = True

    while app_running:
        print("****Ordering Actions****")
        for number, action in app_action.items():
            print(f"{number}: {action}")
        number = int(input("Enter a selection: "))

        if number == 1:
            display_menu()

            sku_prompt = "Please enter the SKU # for the menu item you want to order: "
            quantity_prompt = "Please enter the quantity for the menu item: "

            sku, quantity = get_sku_and_quantity(sku_prompt, quantity_prompt)
            add_to_cart(sku, quantity)

        elif number == 2:
            display_menu()

            sku_prompt = "Please enter the SKU # for the menu item you want to remove: "

            sku = get_sku_and_quantity(sku_prompt)
            remove_from_cart(sku)

        elif number == 3:
            display_menu()

            sku_prompt = "Please enter the SKU # for the menu item you want to modify: "
            quantity_prompt = "Please enter the new quantity for the menu item: "

            sku, quantity = get_sku_and_quantity(sku_prompt, quantity_prompt)
            modify_cart(sku, quantity)

        elif number == 4:

            view_cart()

        elif number == 5:

            checkout()
            app_running = False

        elif number == 6:

            print("Goodbye!")
            app_running = False

        else:
            print("You entered an invalid entry. Please try again!")

open_file.close()