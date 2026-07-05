def length_converter():
    print("\nLength Converter")
    print("1. Meter to Kilometer")
    print("2. Kilometer to Meter")
    print("3. Meter to Centimeter")

    choice = int(input("Choose: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print(f"Result: {value / 1000} km")
    elif choice == 2:
        print(f"Result: {value * 1000} m")
    elif choice == 3:
        print(f"Result: {value * 100} cm")
    else:
        print("Invalid choice")


def weight_converter():
    print("\nWeight Converter")
    print("1. Kilogram to Gram")
    print("2. Gram to Kilogram")

    choice = int(input("Choose: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print(f"Result: {value * 1000} g")
    elif choice == 2:
        print(f"Result: {value / 1000} kg")
    else:
        print("Invalid choice")


def temperature_converter():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = int(input("Choose: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print(f"Result: {(value * 9/5) + 32:.2f} °F")
    elif choice == 2:
        print(f"Result: {(value - 32) * 5/9:.2f} °C")
    else:
        print("Invalid choice")


def time_converter():
    print("\nTime Converter")
    print("1. Hours to Minutes")
    print("2. Minutes to Hours")

    choice = int(input("Choose: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print(f"Result: {value * 60} minutes")
    elif choice == 2:
        print(f"Result: {value / 60} hours")
    else:
        print("Invalid choice")


while True:
    print("\n====== UNIT CONVERTER ======")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Time")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        length_converter()
    elif choice == "2":
        weight_converter()
    elif choice == "3":
        temperature_converter()
    elif choice == "4":
        time_converter()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice")