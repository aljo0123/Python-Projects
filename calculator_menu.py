while True:
    print("\nCalculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1/2/3/4): ")

    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))

    if choice == '1':
        print("Result:", a + b)
    elif choice == '2':
        print("Result:", a - b)
    elif choice == '3':
        print("Result:", a * b)
    elif choice == '4':
        if b != 0:
            print("Result:", a / b)
        else:
            print("Error: Division by zero")
    else:
        print("Invalid Choice")

    cont = input("Do you want to continue? (yes/no): ")
    if cont.lower() != "yes":
        print("Thanks for using calculator")
        break
