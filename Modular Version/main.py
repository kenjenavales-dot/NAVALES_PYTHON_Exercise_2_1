# main.py

from menu import display_menu
from customer import get_customer
from order import create_order, display_order
from payment import process_payment


def main():
    print("================================")
    print("       RESTAURANT SYSTEM")
    print("================================")

    name, table = get_customer()

    menu = display_menu()

    orders, total = create_order(menu)

    display_order(orders, total)

    if total > 0:
        process_payment(total)

    print("\n================================")
    print("Thank you for dining with us!")
    print(f"Customer: {name}")
    print(f"Table: {table}")
    print("================================")


if __name__ == "__main__":
    main()