# order.py

def create_order(menu):
    orders = []
    total = 0

    while True:
        try:
            choice = int(input("\nEnter food number (0 to finish): "))

            if choice == 0:
                break

            if choice not in menu:
                print("Invalid food number.")
                continue

            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

            food, price = menu[choice]
            subtotal = price * quantity

            orders.append((food, quantity, subtotal))
            total += subtotal

            print(f"{food} x {quantity} = ₱{subtotal}")

        except ValueError:
            print("Please enter a valid number.")

    return orders, total


def display_order(orders, total):
    print("\n===== ORDER SUMMARY =====")

    if not orders:
        print("No orders.")
        return

    for food, quantity, subtotal in orders:
        print(f"{food} x {quantity} = ₱{subtotal}")

    print(f"Total: ₱{total}")