from datos import data
from logotipo import*
import random
import os

famosoA=[]
famosoB=[]

def famosoAleatorio():
    return random.choice(data)

def datos(cuenta):
    nombre=cuenta["name"]
    descripcion=cuenta["description"]
    pais=cuenta["country"]

    return f"{nombre}, a {descripcion}, de {pais}"

def revisar(eleccion,numeroA,numeroB):
        if numeroA>numeroB:
            return eleccion=="a"
        else:
            return eleccion=="b"


def jugar():
    puntuacion=0
    juegoTerminado=False
    print(logo)
    famosoA=famosoAleatorio()
    famosoB=famosoAleatorio()
    while juegoTerminado!=True:
        famosoA=famosoB
        famosoB=famosoAleatorio()

        while famosoA==famosoB:
            famosoB=famosoAleatorio()
        
        print(f"Compara A: {datos(famosoA)}")
        print(vs)
        print(f"Contra B: {datos(famosoB)}")
        eleccion=input("Quien tiene mas seguidores?\n\t'A' o 'B'\n: ").lower()
        numeroA=famosoA["follower_count"]
        numeroB=famosoB["follower_count"]

        respuestaCorrecta=revisar(eleccion,numeroA,numeroB)
        os.system("cls")

        if respuestaCorrecta:
            puntuacion+=1
            print(f"En efecto!. Puntuación actual={puntuacion}")
        else:
            juegoTerminado=True
            print(f"Error, el juego termino. Puntuación final={puntuacion}")
        
jugar()