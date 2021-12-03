import random

piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tijera = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
opciones=[piedra,papel,tijera]
sel = int(input("¿Que eliges? \n\t[0] Piedra \n\t[1] Papel \n\t[2] Tijeras\nSeleccion: "))
print(f"Tu seleccion:{opciones[sel]}")
computadora=random.randint(0,2)
print(f"Seleccion de la computadora:{opciones[computadora]}")

if sel>=3 or sel<0:
    print("No haz elegido una opcion correcta, perdiste :(")
elif sel==computadora:
    print("Es un empate!!!")
elif sel==0 and  computadora==1:
    print("Haz perdido :(")
elif sel==0 and computadora==2:
    print("Haz ganado!!!")
elif sel==1 and computadora==0:
    print("Haz ganado!!!")
elif sel==1 and computadora==2:
    print("Haz perdido :(")
elif sel==2 and computadora==0:
    print("Haz perdido :(")
else:
    print("Haz ganado!!!")