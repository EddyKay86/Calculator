def calculator():
    numbers = []
    while True:
        num = input("Enter a number(or 'done' to finish): ")
        if num.lower() == 'done':
            break
        numbers.append(float(num)) 
    operation = input("Enter the operation (+, -, *, /): ")
    
    if operation == '+':
        result = sum(numbers)
    elif operation == '-':
        result = numbers[0] - sum(numbers[1:])
    elif operation == '*':
        result = 1
        for number in numbers:
            result *= number
    elif operation == '/':
        result = numbers[0]
        for number in numbers[1:]:
            result /= number
    else:
        result = "Invalid operation"
        print("The result is:",result)
        calculator()

    
    

