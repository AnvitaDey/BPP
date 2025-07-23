def calculator():
    print(" Welcome to Simple Calculator")

    operators = input("Enter an operator (+, -, *, /): ")

    try:
        N1 = float(input("Enter first number: "))
        N2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input.")
        return

    if operators == "+":
        result = N1 + N2
    elif operators == "-":
        result = N1 - N2
    elif operators == "*":
        result = N1 * N2
    elif operators == "/":
        if N2 == 0:
            print("Cannot divide by zero.")
            return
        result = N1 / N2
    else:
        print("Invalid operator.")
        return

    print(f"Result= {N1} {operators} {N2}")

if __name__ == "__main__":
    while True:
        calculator()
        choice = input("\nDo you want to calculate again? (y/n): ").lower()
        if choice != 'y':
            print("Thank you!")
            break

