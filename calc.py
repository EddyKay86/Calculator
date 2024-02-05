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
        print(result)
    elif operation == '-':
        result = numbers[0] - sum(numbers[1:])
        print(result)
    elif operation == '*':
        result = 1
        for number in numbers:
            result *= number
            print(result)
    elif operation == '/':
        result = numbers[0]
        for number in numbers[1:]:
            result /= number
            print(result)
    else:
        result = "Invalid operation"
        print("The result is:",result)
calculator()

    
    

