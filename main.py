from art import logo




def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
    
}

def calculator():
    print(logo)

    
    num1 = float(input("What is the first number?: "))
    for symbols in operations:
        print(symbols)
        
    user_cont = True
    while user_cont:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What is the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    
        continue_cal = input(f"Type 'y' to continue calculating with {answer} or 'n' to start a new calculation.: ").lower()
        if continue_cal == "y":
            num1 = answer
        else:
            user_cont = False
            calculator()

calculator()
