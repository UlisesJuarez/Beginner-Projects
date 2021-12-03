abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',\
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',\
    'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(texto, recorreN, operacion):
    textoFinal = ""
    if operacion == "decode":
        recorreN *= -1
    for letra in texto:
        if letra in abecedario:
            posicion_actual = abecedario.index(letra)
            nueva_posicion = posicion_actual + recorreN
            textoFinal += abecedario[nueva_posicion]
        else:
            textoFinal += letra
    print(f"Operacion elegida: {operacion}\nResultado: {textoFinal}")

repetir = True
while  repetir:

    quiero = input("Escribe \n\t'encode' para encriptar\n\t'decode' para desencriptar\n: ")
    text = input("Escribe el mensaje: ").lower()
    mueve = int(input("Escribe el numero de posiciones a mover: "))
    
    mueve = mueve % 26

    print("****************************************************")
    caesar(texto=text, recorreN=mueve, operacion=quiero)
    print("****************************************************")
    restart = input("Desea repetir el programa?\n\t'si' para repetir\n\t'no' para finalizar\n: ")
    if restart.lower() == "no":
        repetir = False
        print("Programa terminado")