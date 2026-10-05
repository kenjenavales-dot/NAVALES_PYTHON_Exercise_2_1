# main.py

from restaurant import Restaurant


def main():

    restaurant = Restaurant()

    print("================================")
    print("       RESTAURANT SYSTEM")
    print("================================")

    restaurant.get_customer()

    restaurant.display_menu()

    total = restaurant.create_order()

    restaurant.display_order(total)

    if total > 0:
        restaurant.process_payment(total)
        restaurant.display_receipt(total)


if __name__ == "__main__":
    main()