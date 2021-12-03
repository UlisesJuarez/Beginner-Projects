import os
from dibujo import logo

def suma(n1, n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

def multiplicacion(n1, n2):
  return n1 * n2

def division(n1, n2):
    return n1 / n2

operaciones = {
    "+": suma,
    "-": resta,
    "*": multiplicacion,
    "/": division
}

def calculadora():
    print(logo)

    num1 = float(input("Ingresa el primer numero: "))
    for simbolo in operaciones:
        print(simbolo)

    repetir = True
    while repetir:
        hacer = input("Escriba el simbolo de la operacion: ")
        num2 = float(input("Ingresa el segundo numero: "))
        hazFuncion = operaciones[hacer]
        resultado = hazFuncion(num1, num2)
        print(f"{num1} {hacer} {num2} = {resultado}")

        if input(f"Escribe\n\t'si' para hacer mas operaciones con {resultado}\n\t'no' para empezar de 0\n\t: ").lower() == 'si':
            num1 = resultado
        else:
            repetir = False
            os.system("cls")
            calculadora()

calculadora()




