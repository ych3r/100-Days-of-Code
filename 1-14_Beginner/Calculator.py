from replit import clear

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def calculate():
    end = False
    x = float(input("What's the first number?: "))
    while not end:
        operation = input("+\n-\n*\n/\nPick an operation: ")
        y = float(input("What's the next number?: "))
        if operation == '+':
            ans = add(x, y)
        if operation == '-':
            ans = sub(x, y)
        if operation == '*':
            ans = mul(x, y)
        if operation == '/':
            ans = div(x, y)
        print(f"{x} {operation} {y} = {ans}")
        next = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation: ")
        if next == 'y':
            x = ans
        elif next == 'n':
            clear()
            x = float(input("What's the first number?: "))
        elif next == "exit":
            end = True


def main():
    calculate()

main()