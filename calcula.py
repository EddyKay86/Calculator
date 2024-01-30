def add(numbers):
    return sum(numbers)

def subtract(numbers):
    if len(numbers) < 2:
        raise ValueError("Subtraction requires at least two numbers.")
    return numbers[0] - sum(numbers[1:])

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    if len(numbers) < 2:
        raise ValueError("Division requires at least two numbers.")
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            raise ValueError("Cannot divide by zero.")
        result /= num
    return result

def get_input():
    expression = input("Enter expression (e.g., '2 + 3 * 4'): ")
    return expression.split()

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