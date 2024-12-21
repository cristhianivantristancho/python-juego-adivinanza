import random


def juego_adivinanza():
    # Generar un numero del 1 al 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    # Primeras lineas del juego donde se da la bienvenida
    print("¡Bienvenido al juego de adivinanza de numero")
    print("Debes adivinar un numero entre el 1 al 100")
    print("¡Intenta adivinarlo!")

    while not adivinado:
        # Solicitar un numero del 1 al 100
        adivinanza = input("Introduzca un numero del 1 al 100: ")

        # Verificar que la entrada sea un numero
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)  # Lo estamos pasando de texto a entero
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El numero secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El numero secreto es menor a {adivinanza}")
            else:
                print(
                    f"¡Felicidades has ganado! El numero {adivinanza} es el secreto y lo has logrado en {intentos} intentos"
                )
        else:
            print("Por favor introduzca un numero valido entre el 1 al 100")


juego_adivinanza()
