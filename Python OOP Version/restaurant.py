# restaurant.py

class Restaurant:

    def __init__(self):
        self.menu = {
            1: ("Burger", 120),
            2: ("Pizza", 250),
            3: ("Fried Chicken", 150),
            4: ("Spaghetti", 130),
            5: ("Soft Drink", 50)
        }

        self.orders = []
        self.customer_name = ""
        self.table_number = ""

    def get_customer(self):
        print("\n===== CUSTOMER INFORMATION =====")

        self.customer_name = input("Enter customer name: ")
        self.table_number = input("Enter table number: ")

    def display_menu(self):
        print("\n===== RESTAURANT MENU =====")

        for number, (food, price) in self.menu.items():
            print(f"{number}. {food} - ₱{price}")

    def create_order(self):
        total = 0

        while True:
            try:
                choice = int(input("\nEnter food number (0 to finish): "))

                if choice == 0:
                    break

                if choice not in self.menu:
                    print("Invalid food number.")
                    continue

                quantity = int(input("Enter quantity: "))

                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    continue

                food, price = self.menu[choice]
                subtotal = price * quantity

                self.orders.append((food, quantity, subtotal))
                total += subtotal

                print(f"{food} x {quantity} = ₱{subtotal}")

            except ValueError:
                print("Please enter a valid number.")

        return total

    def display_order(self, total):
        print("\n===== ORDER SUMMARY =====")

        if not self.orders:
            print("No orders.")
            return

        for food, quantity, subtotal in self.orders:
            print(f"{food} x {quantity} = ₱{subtotal}")

        print(f"Total: ₱{total}")

    def process_payment(self, total):
        print("\n===== PAYMENT =====")
        print(f"Total Amount: ₱{total}")

        while True:
            try:
                payment = float(input("Enter payment: ₱"))

                if payment < total:
                    print("Insufficient payment.")
                else:
                    change = payment - total

                    print(f"Payment: ₱{payment:.2f}")
                    print(f"Change: ₱{change:.2f}")
                    print("Payment successful!")
                    break

            except ValueError:
                print("Please enter a valid amount.")

    def display_receipt(self, total):
        print("\n================================")
        print("         RESTAURANT RECEIPT")
        print("================================")
        print(f"Customer: {self.customer_name}")
        print(f"Table: {self.table_number}")

        for food, quantity, subtotal in self.orders:
            print(f"{food} x {quantity} = ₱{subtotal}")

        print(f"TOTAL: ₱{total}")
        print("================================")
        print("Thank you for dining with us!")