import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)
terminarJuego = False
vidas = len(stages) - 1

palabraAleatoria = random.choice(word_list)
longitudAleatoria = len(palabraAleatoria)

adivinada = []
for _ in range(longitudAleatoria):
    adivinada.append("_")

while not terminarJuego:
    letra = input("Dime una letra: ").lower()


    if letra in adivinada:
        print(f"Ya habias dicho la letra '{letra}'")

    for i in range(longitudAleatoria):
        buscar = palabraAleatoria[i]
        if buscar == letra:
            adivinada[i] = buscar
    print(f"{' '.join(adivinada)}")

    if letra not in palabraAleatoria:
        print(f"Has elegido {letra}, pero no esta en la palabra, pierdes una vida.")
        vidas -= 1
        if vidas == 0:
            terminarJuego = True
            print("Tus vidas se han agotado has perdido.")
    
    if not "_" in adivinada:
        terminarJuego = True
        print("Palabra adivinada. Has ganado!!!")

    print(stages[vidas])