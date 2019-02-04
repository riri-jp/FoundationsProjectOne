####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Mashari"
signature_flavors = ["Cherry", "classic chocolate", "strawberry"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    print ("our menu")
    for item in menu:
        print("- %s (KD %s)" % (item,menu[item]))



def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for item in original_flavors:
        print (("- %s") % item)


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for item in signature_flavors:
        print (("- %s") % item)


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!

    if order in menu:
        return  True   
    elif order in original_flavors:
        return  True
    elif order in signature_flavors:
        return  True
    else:
         return  False 
         print ("nothing there")




def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    print ("What's your order? or Exit to Exit")
    while True:
        order = input ()
        if order == "Exit":
            break
        elif is_valid_order(order):
            order_list.append(order)
        else:
            print ("we Out!!")
        order = input("what else would you like? ")
    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    if total > 5:
        return True
    else:
        return False


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    for order in order_list:
        if order in menu:
            total += menu[order]
        elif order in original_flavors:
            total += original_price
        else:
            total += signature_price
    return total



    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    for order in order_list:
        print(order)

    total = get_total_price(order_list)
    print("your total is: %s DK" % (total))

    if accept_credit_card(total):
        print("you can pay by either credit card or cash")
    else:
            print("you can pay using cash only")
    print("Thank you for using %s as your path to diabetes!"%(cupcake_shop_name))
