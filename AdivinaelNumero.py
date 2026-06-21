import random

class AdivinaNumero:
    # Constructor de la clase, inicializa los atributos del juego
    def __init__(self):
        self.numero_secreto = random.randint(1, 100) # Genera el numero aleatorio entre 1 y 100
        self.intentos = 0
        self.max_intentos = 10
        self.historial = [] # Lista que guarda cada intento del jugador

    # Funcion para validar que el numero ingresado este en el rango permitido
    def validar_numero(self, numero):
        ListaValidos = list(filter(lambda x: x == numero, range(1, 101))) # Filtra si el numero esta en rango
        return len(ListaValidos) > 0

    # Funcion para mostrar el historial de intentos
    def mostrar_historial(self):
        if len(self.historial) == 0:
            print("Aun no hay intentos registrados\n")
            return

        print("\n  Historial De Intentos :")
        # Usamos map para transformar cada intento en un texto legible
        ListaMostrar = list(map(lambda i: "Intento " + str(i[0]) + " : ingresaste " + str(i[1]), self.historial))

        for linea in ListaMostrar:
            print(linea)
        print()

    # Funcion principal del juego
    def jugar(self):
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
        print("  Bienvenido al juego Adivina el Numero")
        print("  Tengo un numero entre 1 y 100 en mente")
        print(f"  Tienes {self.max_intentos} intentos para adivinarlo")
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

        adivino = False # Variable para saber si adivino o no

        while self.intentos < self.max_intentos:
            try:
                intento = int(input(f"\nIntento {self.intentos + 1}: Ingresa un numero: "))

                if not self.validar_numero(intento): # Validamos que el numero este en rango
                    print("El numero debe estar entre 1 y 100, intentalo de nuevo")
                    continue

                self.intentos += 1
                self.historial.append([self.intentos, intento]) # Guardamos el intento en el historial

                if intento == self.numero_secreto:
                    print(f"\nCorrecto! Adivinaste el numero {self.numero_secreto}")
                    print(f"Lo lograste en {self.intentos} intento(s)")
                    self.mostrar_historial()
                    adivino = True
                    break
                elif intento < self.numero_secreto:
                    print(f"{intento} es muy bajo, el numero es mayor")
                else:
                    print(f"{intento} es muy alto, el numero es menor")

                restantes = self.max_intentos - self.intentos
                if restantes == 1:
                    print(f"Cuidado! solo te queda {restantes} intento")
                else:
                    print(f"Te quedan {restantes} intentos")

            except ValueError:
                print("Eso no es un numero valido, intentalo de nuevo")

        if not adivino: # Si no adivino, revela el numero secreto
            print(f"\nSe acabaron los intentos!")
            print(f"El numero secreto era {self.numero_secreto}")
            self.mostrar_historial()

    # Funcion para mostrar el menu principal
    def mostrar_menu(self):
        print("\n_ _ _ _ _Adivina El Numero_ _ _ _ _")
        print("1. Jugar")
        print("2. Ver historial")
        print("3. Salir")


if __name__ == "__main__":
    juego = AdivinaNumero() # Creamos el objeto de la clase
    opcion = 0

    while opcion != 3:
        juego.mostrar_menu()
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            juego.jugar()
        elif opcion == 2:
            juego.mostrar_historial()
        elif opcion == 3:
            print("Saliendo del juego")
        else:
            print("Opcion invalida, intente de nuevo.\n")