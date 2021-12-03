from logo import *
import os
"""Subasta a ciegas"""
print(logo)
subasta={}


def borrarPantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def ganador(ofertas):
    mayorOferta=0
    nombreGanador=""

    for persona in ofertas:
        ofertaActual=ofertas[persona]
        if ofertaActual>mayorOferta:
            mayorOferta=ofertaActual
            nombreGanador=persona
    print(f"El ganador es {nombreGanador} con una oferta de ${mayorOferta}")
        

repetir=True
while repetir:
    nombre=input("Cual es tu nombre: ")
    oferta=int(input("Cual es tu oferta: "))

    subasta[nombre]=oferta
    continuar=input("Hay mas ofertadores? \n\tsi\n\tno\n:").lower()
    if continuar=="si":
        borrarPantalla()
        repetir=True
    elif continuar=="no":
        repetir=False
        ganador(subasta)

