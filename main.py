from datetime import datetime

GROCERIES = {
    "Rice (1kg)": 50,
    "Eggs (dozen)": 75,
    "Milk (1L)": 60,
    "Bread (loaf)": 40,
    "Chicken (1kg)": 180
}


def display_items():
    """Displays all available grocery items and their prices."""
    print("\n=== Grocery Items ===")
    for i, (item, price) in enumerate(GROCERIES.items(), start=1):
        print(f"{i}. {item:<15} ₱{price:>6.2f}")
    print(f"{len(GROCERIES)+1}. Add new product")
    print("0. Back to Main Menu")


def select_items(cart):
    """Lets the cashier order items or add custom products."""
    total = sum(subtotal for _, _, _, subtotal in cart)

    while True:
        display_items()
        choice = input("\nEnter item number to add: ").strip()

        if choice == "0":
            break

        if choice == str(len(GROCERIES) + 1):
            item = input("Enter new product name: ").strip().title()
            try:
                price = float(input(f"Enter price for {item} (₱): "))
                qty = int(input(f"Enter quantity for {item}: "))
                if price <= 0 or qty <= 0:
                    print(" Price and quantity must be greater than zero.")
                    continue
            except ValueError:
                print(" Please enter valid numbers for price and quantity.")
                continue

            subtotal = price * qty
            cart.append((item, price, qty, subtotal))
            total += subtotal
            print(f" Added {qty} x {item} = ₱{subtotal:.2f}")
            continue

        if not choice.isdigit() or not (1 <= int(choice) <= len(GROCERIES)):
            print(" Invalid input. Please enter a valid item number.")
            continue

        index = int(choice)
        item = list(GROCERIES.keys())[index - 1]
        price = GROCERIES[item]

        try:
            qty = int(input(f"Enter quantity for {item}: "))
            if qty <= 0:
                print(" Quantity must be at least 1.")
                continue
        except ValueError:
            print(" Please enter a valid number for quantity.")
            continue

        subtotal = price * qty
        cart.append((item, price, qty, subtotal))
        total += subtotal
        print(f" Added {qty} x {item} = ₱{subtotal:.2f}")

    return cart


def view_cart(cart):
    """Displays current cart contents."""
    print("\n=== Current Cart ===")
    if not cart:
        print("Your cart is empty.")
        return

    total = sum(subtotal for _, _, _, subtotal in cart)
    print(f"{'Item':<18}{'Qty':<5}{'Price':<8}{'Total':>8}")
    print("-" * 42)
    for item, price, qty, subtotal in cart:
        print(f"{item:<18}{qty:<5}₱{price:<7.2f}₱{subtotal:>7.2f}")
    print("-" * 42)
    print(f"{'TOTAL:':<30} ₱{total:>8.2f}")


def proceed_to_payment(cart):
    """Handles payment and prints the receipt."""
    if not cart:
        print("\nYour cart is empty. Please order items first.")
        return []

    total = sum(subtotal for _, _, _, subtotal in cart)

    print("\n=== Checkout Summary ===")
    print(f"{'Item':<18}{'Qty':<5}{'Price':<8}{'Total':>8}")
    print("-" * 42)
    for item, price, qty, subtotal in cart:
        print(f"{item:<18}{qty:<5}₱{price:<7.2f}₱{subtotal:>7.2f}")
    print("-" * 42)
    print(f"{'TOTAL:':<30} ₱{total:>8.2f}")

    while True:
        try:
            payment = float(input("\nEnter payment amount (₱): "))
            if payment < total:
                print(" Insufficient payment. Please enter higher than total.")
            else:
                change = payment - total
                break
        except ValueError:
            print(" Please enter a valid number.")

    print_receipt(cart, total, payment, change)

    print("\nTransaction complete. Returning to main menu...")
    return []


def print_receipt(cart, total, payment, change):
    """Prints the formatted grocery receipt after payment."""
    print("\n" + "=" * 42)
    print("           GROCERY STORE RECEIPT")
    print("=" * 42)
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 42)
    print(f"{'Item':<18}{'Qty':<5}{'Price':<8}{'Total':>8}")
    print("-" * 42)
    for item, price, qty, subtotal in cart:
        print(f"{item:<18}{qty:<5}₱{price:<7.2f}₱{subtotal:>7.2f}")
    print("-" * 42)
    print(f"{'TOTAL:':<30} ₱{total:>8.2f}")
    print(f"{'Payment:':<30} ₱{payment:>8.2f}")
    print(f"{'Change:':<30} ₱{change:>8.2f}")
    print("-" * 42)

    if total > 100:
        print(" Thank you! Your total exceeds ₱100. Enjoy your shopping!")
    else:
        print(" Thank you for shopping with us!")

    print("=" * 42)
    print("        Please Come Again Soon! ")
    print("=" * 42)


def main_menu():
    """Displays the main menu and handles navigation."""
    cart = []

    while True:
        print("\n==================================")
        print("️ Welcome to the Grocery Store!")
        print("==================================")
        print("1. Order Items")
        print("2. View Cart")
        print("3. Proceed to Payment")
        print("4. Exit")
        print("==================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            cart = select_items(cart)
        elif choice == "2":
            view_cart(cart)
        elif choice == "3":
            cart = proceed_to_payment(cart)
        elif choice == "4":
            print("Thank you! Have a nice day.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main_menu()