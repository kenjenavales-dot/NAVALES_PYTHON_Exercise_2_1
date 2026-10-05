# payment.py

def process_payment(total):
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