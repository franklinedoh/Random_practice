# Variable length arguments *args (Non keyword arguements)
def order_food(min_order, *args):
    print(f"You have ordered: {min_order}")
    # print(args)
    for item in args:
        print(f"You have ordered: {item}")
    print("Your food will be delivered in 30 minutes")
    print("Enjoy your meal")

order_food("salad", "pizza", "soup")

