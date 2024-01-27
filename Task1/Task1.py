def pizza_price_calculator():
    print("BPP Pizza Price Calculator")
    print("==========================")

    # Input number of pizzas
    while True:
        try:
            pizzas_ordered = int(input("How many pizzas ordered? "))
            if pizzas_ordered >= 0:
                break
            else:
                print("Please enter a positive integer!")
        except ValueError:
            print("Please enter a number!")

    # Input delivery requirement
    while True:
        delivery_required = input("Is delivery required? (Y/N) ").upper()
        if delivery_required in ['Y', 'N']:
            break
        else:
            print('Please answer "Y" or "N".')

    # Input whether it's Tuesday
    while True:
        is_tuesday = input("Is it Tuesday? (Y/N) ").upper()
        if is_tuesday in ['Y', 'N']:
            break
        else:
            print('Please answer "Y" or "N".')

    # Input whether the customer used the app
    while True:
        used_app = input("Did the customer use the app? (Y/N) ").upper()
        if used_app in ['Y', 'N']:
            break
        else:
            print('Please answer "Y" or "N".')

    # Calculate total price
    pizza_price = pizzas_ordered * 12
    delivery_cost = 0 if delivery_required == 'N' else 2.5 if pizzas_ordered < 5 else 0
    tuesday_discount = 0.5 if is_tuesday == 'Y' else 0
    app_discount = 0.25 if used_app == 'Y' else 0

    total_price = (pizza_price + delivery_cost) * (1 - tuesday_discount) * (1 - app_discount)

    # Display the total price
    print(f"\nTotal Price: £{total_price:.2f}.")


# Run the program
pizza_price_calculator()
