# Calculadora

def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b


def modulo(a, b):
    if b == 0:
        return "Error: no se puede calcular el modulo con cero"
    return a % b