def calculator():
    print("Simple Calculator - Enter 'exit' to end")

    while True:
        try:
            tokens = get_input()

            if tokens[0].lower() == 'exit':
                break

            numbers = [float(token) for token in tokens if token.isnumeric() or (token[0] == '-' and token[1:].isnumeric())]

            if not numbers:
                raise ValueError("Invalid expression.")

            operation = tokens[len(numbers)]

            if operation == '+':
                result = add(numbers)
            elif operation == '-':
                result = subtract(numbers)
            elif operation == '*':
                result = multiply(numbers)
            elif operation == '/':
                result = divide(numbers)
            else:
                raise ValueError("Invalid operation.")

            print("Result:", result)

        except (ValueError, ZeroDivisionError) as e:
            print("Error:", e)
if __name__ == "_main_":
    calculator()
