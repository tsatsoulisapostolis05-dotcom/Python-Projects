"""A beginner-friendly command-line calculator."""


def calculator():
    try:
        number1 = float(input("\nGive me the first number: "))
        operator = input("Choose +, -, *, or /: ").strip()
        number2 = float(input("Give me the second number: "))

        if operator == "+":
            result = number1 + number2
        elif operator == "-":
            result = number1 - number2
        elif operator == "*":
            result = number1 * number2
        elif operator == "/":
            if number2 == 0:
                print("You cannot divide by zero.")
                return

            result = number1 / number2
        else:
            print("That operator is not available.")
            return

        print(f"{number1} {operator} {number2} = {result}")

    except ValueError:
        print("Please enter valid numbers only.")


calculator()
