a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
operator=input("Enter Operator:")

def addition(a, b, c):
    return a+b+c

def subtraction(a,b,c):
    return a-b-c

def multiple(a,b,c):
    return a*b*c

def division(a,b,c):
    return a/b/c

if operator=="+":
    addition(a,b,c)
    result=addition(a,b,c)
    print(result)
elif operator=="*":
    multiple(a,b,c)
    result=multiple(a,b,c)
    print(result)
elif operator=="-":
    subtraction(a,b,c)
    result=subtraction(a,b,c)
    print(result)
elif operator=="/":
    division(a,b,c)
    result=division(a,b.c)
    print(result)
else:
    print("Invalid operator")
