from art import*
import random

vidasFacil=10
vidasDificil=5

def dificultad():
        eleccion=input("""
        Elige la dificultad
                'facil'    10 vidas
                'dificil'   5 vidas
        : """)
        if eleccion=="facil":
                return vidasFacil
        else:
                return vidasDificil

def compara(real,adivinado,vidas):
        if adivinado>real:
                print("Un poco menos")
                return vidas-1
        elif adivinado<real:
                print("Un poco mas")
                return vidas-1
        else:
                print(f"Has ganado, en efecto se trata del '{adivinado}'")
                

def juego():
        
        print(logo)
        print("Bienvenido a adivinar un numero!!!")
        print("Estoy pensando en un numero entre el 1 y el 100")
        numeroSecreto=random.randint(1,100)
        turnos=dificultad()
        #print(f"upps soy {numeroSecreto}")
        juegoTerminado=False
        while juegoTerminado!=True:
                print("********************************************************")
                print(f"Tienes {turnos} oportunidades para adivinar el numero.")
                adivinando=int(input("Pienso que es el: "))
                turnos=compara(numeroSecreto,adivinando,turnos)

                if turnos==0:
                        print("********************************************************")
                        print("Has agotado tus vidas, perdiste :(")
                        juegoTerminado=True
                elif adivinando!=numeroSecreto:
                        print("********************************************************")
                        print("Intenta de nuevo :)")
                else:
                        juegoTerminado=True


juego()