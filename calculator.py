#calculator

#addition
def add(n1, n2):
    return n1 + n2

#substraction
def sub(n1, n2):
    return n1 - n2

#division
def div(n1, n2):
    return n1 / n2

# multiplycation
def mul(n1, n2):
    return n1 * n2

operations = {}
operations["+"] = add
operations["-"] = sub
operations["*"] = mul
operations["/"] = div

def calculator():
    num1 = float(input("what's the first number: "))
    for opr in operations:
        print(opr)
    should_continue = True
    while should_continue:
        first_operation=input("pick an operation :")
        num2 = float(input("what's the number: "))
        function1 = operations[first_operation]
        result=function1(num1,num2)
        print(f"{num1} {first_operation} {num2} = {result}")
        another_operation =input(f"Type 'y' to continue calculation with {result}, or type 'n' to exit :")
        if another_operation == "y":
            num1=result
        else:
            should_continue = False
            new_cal=input("do you want to continue with new calculation type 'y', or type 'n' to exit. :")
            if new_cal == "y":
                calculator()
            else:
                print("Good Bye")

calculator()
