from csv import reader

open_file = open('Komodo_Miami_Food_Menu.csv', 'r')
read_file = reader(open_file)

menu = list(read_file)[1:]

menu_dict = {}

app_action ={1: "Add item to cart", 2: "Remove item from cart", 3: "Modify order", 4: "View Cart", 5: "Checkout", 6: "Exit"} 

sales_tax = 0.07

cart={}

sku_num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17']

#Compiling the menu in a nested dictionary from a nested list
for row in menu:
    sku = row[0]
    name = row[1]
    price = float(row[2])

    inner_dict = {name:price}

    menu_dict[sku] = inner_dict

#print(menu_dict)


# Display the menu to the customer
def display_menu():
    print('\n')
    print("****Menu****")

    # Removing the 'sku' from the '#', and rebuilding each item in the menu dictionary with just the '#'
    for sku in menu_dict:
        sku_num = sku[3:]
        sku_num_list.append(sku)

        for name in menu_dict[sku]:
            menu_item_name = name
            price = menu_dict[sku][name]
            print(f"{sku_num} {menu_item_name}: ${price:.2f}")

display_menu()

# Adding menu items to the cart
def add_to_cart(sku, quantity):
    sku = str(sku)

    if sku not in sku_num_list:
        print("This is not a valid entry.  Please try again!")
    else:
        name_container = []             # Need to create a list with the menu item names for the print statement, because we need to get the menu item names for our print statement
        for row in menu:                # Need to loop through the menu to get the menu item name with its corresponding sku #.
            if sku == row[0][3:]:
                name_container.append(row[1])

        if sku in cart:
            cart[sku] += quantity
        else:
            cart[sku] = quantity

    print('\n')
    print(f"Added", {cart[sku]}, "of", {name_container[0]}, "to the cart.")

add_to_cart(3, 2)

# Removing menu items from the cart
def remove_from_cart(sku):
    sku = str(sku)

    if sku in cart:
        removed_item = cart.pop(sku)

        item_name = None

        for row in menu:            # Need to loop through menu items because need to extract item name with its corresponding sku # to match with the remove item for the print statement
            if sku == row[0][3:]:   # check to see if the entered sku (e.g. '4') matches the sku in the menu
                item_name = row[1]
                break
        print(f"Removed {removed_item} of {item_name} from the cart.")

    else:
        print("The sku item you entered is not in the cart.  Please try again.")

remove_from_cart(2)

# Modifying or changing the order in the cart
def modify_cart(sku, quantity):
    sku = str(sku)
    quantity = int(quantity)

    if sku in cart:
        if quantity > 0:
            cart[sku] = quantity

        item_name = None

        for row in menu:
            if sku == row[0][3:]:
                item_name = row[1]
                break

    elif sku in cart and quantity <= 0:
        remove_from_cart(sku)

    print(f"Modified, {item_name}, quantity to , {quantity}, in cart.")

# viewing cart order.
def view_cart():

    print('\n')
    print("****Cart Contents****")

    subtotal = 0

    for sku in menu_dict:
        if sku[3:] in cart:
            quantity = cart[sku[3:]]
            for name in menu_dict[sku]:
                price = menu_dict[sku][name]
                subtotal = subtotal + (price * quantity)
                print(f"Your subtotal is ${subtotal} for {name}")

    tax = subtotal * sales_tax
    total = subtotal + tax

    print('\n')
    print(f"Your total is ${round(total, 2)}.")

view_cart()

#Checking out the order in the cart.
def checkout():
    print('\n')
    print("****Checkout****")
    view_cart()
    print('\n')
    print("Your order is submitted and being process")

checkout()

# Entering the order and quantity of menu items
def get_sku_and_quantity(sku_prompt, quantity_prompt = None):
    item_sku = input(sku_prompt)
    item_sku = "sku" + item_sku

    if quantity_prompt:                       #quantity prompt is not an empty string
        quantity = input(quantity_prompt)

        if quantity.isdigit():
            quantity = int(quantity)
        else:
            quantity = 1

        return item_sku, quantity
    
    return item_sku

get_sku_and_quantity('sku1', 2)


def order_loop():
    print("Welcome to Komodo Miami!")

    app_running = True
    
    while app_running:
        print("****Ordering Actions****")

        for number, action in app_action.items():
            print(f"{number}: {action}")
        
        print(int(input("Enter a selection: ", number)))

        if number == 1:
            display_menu()
            sku_prompt = "Please enter the SKU # for the menu item you want to order "
            quantity_prompt = "Please entered the quantity for the menu item "
            get_sku_and_quantity(sku_prompt, quantity_prompt)
            add_to_cart(sku_prompt, quantity_prompt)

        elif number == 2:
            display_menu()
            get_sku_and_quantity()  # Does not requuire the 'sku_prompt' and 'quantity_prompt' because 'remove_from_cart()' function does not require any argument variables.
            remove_from_cart()    

        elif number == 3:
            display_menu()
            get_sku_and_quantity(sku_prompt, quantity_prompt)
            modify_cart(sku_prompt, quantity_prompt)

        elif number == 4:
            view_cart()

        elif number == 5:
            checkout()
            app_running = False

        elif number == 6:
            print("Goodbye!")

        else:
            print("You entered an invalid entry.  Please try again!")

open_file.close()







   




    


