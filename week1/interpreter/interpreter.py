def main():
    expression = input("Type in your arthmetic expression: ").lower().strip()

    x, y, z = expression.split(" ")
    x = int(x)
    z = int(z)

    match y:
        case "+":
            result = add(x, z)
        case "-":
            result = subtract(x, z)
        case "*":
            result = multiply(x, z)
        case "/":
            result = divide(x, z)

    print(result)

# This function adds both numbers
def add(n1, n2):
    return float(n1 + n2)

# This function subtracts both numbers
def subtract(n1 ,n2):
    return float(n1 - n2)

# This function multiply both numbers
def multiply(n1 ,n2):
    return float(n1 * n2)

# This function divide both numbers
def divide(n1 ,n2):
    return float(n1 / n2)


main()