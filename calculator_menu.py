import math

history = []

while True:
    print("\n====================")
    print("     CALCULATOR")
    print("====================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square Root")
    print("8. View History")
    print("9. Exit")

    choice = input("\nEnter your choice (1-9): ")

    if choice == '9':
        print("\nThanks for using calculator!")
        break

    if choice == '8':
        print("\nCalculation History:")

        if len(history) == 0:
            print("No calculations yet.")
        else:
            for item in history:
                print(item)

        continue

    if choice == '7':
        try:
            number = float(input("Enter a number: "))

            if number >= 0:
                result = math.sqrt(number)
                print("Result:", result)

                history.append(
                    "√" + str(number) + " = " + str(result)
                )
            else:
                print("Error: Cannot find square root of a negative number")

        except ValueError:
            print("Error: Please enter a valid number")

        continue

    if choice not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid choice")
        continue

    try:
        a = float(input("Enter your first number: "))
        b = float(input("Enter your second number: "))

        if choice == '1':
            result = a + b
            symbol = "+"

        elif choice == '2':
            result = a - b
            symbol = "-"

        elif choice == '3':
            result = a * b
            symbol = "*"

        elif choice == '4':
            if b != 0:
                result = a / b
                symbol = "/"
            else:
                print("Error: Division by zero")
                continue

        elif choice == '5':
            if b != 0:
                result = a % b
                symbol = "%"
            else:
                print("Error: Cannot use zero for modulus")
                continue

        elif choice == '6':
            result = a ** b
            symbol = "**"

        print("Result:", result)

        calculation = (
            str(a) + " " + symbol + " " +
            str(b) + " = " + str(result)
        )

        history.append(calculation)

    except ValueError:
        print("Error: Please enter valid numbers.")

