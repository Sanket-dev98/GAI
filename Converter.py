def print_menu():
    print("\n=== Python Unit Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kilometers to Miles")
    print("4. Miles to Kilometers")
    print("5. Exit")

def convert_units():
    while True:
        print_menu()
        choice = input("\nChoose an option (1-5): ").strip()

        if choice == '5':
            print("Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Please select a number from 1 to 5.")
            continue

        try:
            value = float(input("Enter the value to convert: "))
        except ValueError:
            print("Error: Please enter a valid numerical number.")
            continue

        # Perform conversions based on selection
        if choice == '1':
            result = (value * 9/5) + 32
            print(f"👉 {value}°C is equal to {result:.2f}°F")
        elif choice == '2':
            result = (value - 32) * 5/9
            print(f"👉 {value}°F is equal to {result:.2f}°C")
        elif choice == '3':
            result = value * 0.621371
            print(f"👉 {value} km is equal to {result:.2f} miles")
        elif choice == '4':
            result = value / 0.621371
            print(f"👉 {value} miles is equal to {result:.2f} km")

if __name__ == "__main__":
    convert_units()
