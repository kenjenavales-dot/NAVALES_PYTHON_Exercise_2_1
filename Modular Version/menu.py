# menu.py

def display_menu():
    menu = {
        1: ("Burger", 120),
        2: ("Pizza", 250),
        3: ("Fried Chicken", 150),
        4: ("Spaghetti", 130),
        5: ("Soft Drink", 50)
    }

    print("\n===== RESTAURANT MENU =====")
    for number, (food, price) in menu.items():
        print(f"{number}. {food} - ₱{price}")

    return menu