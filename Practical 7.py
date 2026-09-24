def calculator():
    """Perform basic arithmetic operations."""
    try:
        first = float(input("Enter first number: "))
        operator = input("Enter operation (+, -, *, /): ").strip()
        second = float(input("Enter second number: "))

        if operator == "+":
            result = first + second
        elif operator == "-":
            result = first - second
        elif operator == "*":
            result = first * second
        elif operator == "/":
            if second == 0:
                print("Error: cannot divide by zero.")
                return
            result = first / second
        else:
            print("Error: invalid operation.")
            return

        print(f"Result: {result}")
    except ValueError:
        print("Error: please enter valid numbers.")


if __name__ == "__main__":
    calculator()