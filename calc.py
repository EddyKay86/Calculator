def calculator():
    numbers = []
    while True:
        num = input("Enter a number(or 'done' to finish): ")
        if num.lower() == 'done':
            break
        numbers.append(float(num)) 
    operation = input("Enter operation (+, -, *, /): ")
    
    

