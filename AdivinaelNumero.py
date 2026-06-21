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