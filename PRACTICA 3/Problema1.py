import random

class Juego:
    def __init__(self):
        self.numeroDeVidas = 0
        self.record = 0

    def reiniciaPartida(self, vidas):
        self.numeroDeVidas = vidas
        print(f"Partida reiniciada con {vidas} vidas.")

    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas
            print(f"¡Nuevo récord: {self.record} vidas restantes!")

    def quitaVida(self):
        self.numeroDeVidas -= 1
        print(f"Te queda(n) {self.numeroDeVidas} vida(s).")

class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__()
        self.numeroAAdivinar = 0
        self.reiniciaPartida(vidas)

    def iniciaPartida(self):
        self.numeroAAdivinar = random.randint(0, 10)
        print("¡La partida ha comenzado! Adivina un número entre 0 y 10.")

    def intentaAdivinar(self, intento):
        if self.numeroDeVidas <= 0:
            print("Has perdido. No tienes más vidas.")
            return

        if intento == self.numeroAAdivinar:
            print("¡Acertaste!!")
            self.actualizaRecord()
        elif intento < self.numeroAAdivinar:
            print("El número es mayor.")
            self.quitaVida()
        else:
            print("El número es menor.")
            self.quitaVida()

        if self.numeroDeVidas == 0:
            print("Has perdido.")

class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(vidas=5)
        juego.iniciaPartida()

        while juego.numeroDeVidas > 0:
            try:
                intento = int(input("Ingresa tu número (0-10): "))
                if 0 <= intento <= 10:
                    juego.intentaAdivinar(intento)
                else:
                    print("Número fuera de rango. Intenta entre 0 y 10.")
            except ValueError:
                print("Entrada inválida. Por favor ingresa un número.")

# Ejecutar la aplicación
if __name__ == "__main__":
    Aplicacion.main()
