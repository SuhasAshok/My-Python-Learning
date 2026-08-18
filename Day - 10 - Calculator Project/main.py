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
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    should_continue = True
    num1 = float(input("Enter the first number: "))
    while should_continue:
        for symbols in operations:
            print(symbols)
        operator = input("Pick an operator: ")
        num2 = float(input("Enter a number: "))
        answer = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")
        choice = input(f"type 'y' to continue with {answer} or 'n' to start new calculation or type stop: ").lower()
        if choice == "y":
            num1 = answer
        elif choice == "n":
            should_continue = False
            print("\n" * 100)
            calculator()
        else:
            should_continue = False

calculator()
