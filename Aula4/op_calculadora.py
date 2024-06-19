def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

def op(operacao, num1, num2):
    match operacao:
        case 1:
            return add(num1, num2)
        case 2:
            return subtract(num1, num2)
        case 3:
            return multiply(num1, num2)
        case 4:
            return divide(num1, num2)
        case _:
            return "Operação inválida!"