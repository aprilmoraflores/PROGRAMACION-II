# Clase base
class JuegoAdivinaNumero:
    def validaNumero(self, numero):
        return 0 <= numero <= 10

    def juega(self):
        try:
            numero = int(input("Ingresa un número entre 0 y 10: "))
            if self.validaNumero(numero):
                print("¡Número válido!")
            else:
                print("Error: El número debe estar entre 0 y 10.")
        except ValueError:
            print("Error: Debes ingresar un número entero.")

# Clase derivada para números pares
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if 0 <= numero <= 10 and numero % 2 == 0:
            return True
        else:
            print("Error: El número debe ser PAR y estar entre 0 y 10.")
            return False

    def juega(self):
        try:
            numero = int(input("Adivina un número PAR entre 0 y 10: "))
            if self.validaNumero(numero):
                print("¡Correcto! Es un número par válido.")
        except ValueError:
            print("Error: Debes ingresar un número entero.")

# Clase derivada para números impares
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if 0 <= numero <= 10 and numero % 2 != 0:
            return True
        else:
            print("Error: El número debe ser IMPAR y estar entre 0 y 10.")
            return False

    def juega(self):
        try:
            numero = int(input("Adivina un número IMPAR entre 0 y 10: "))
            if self.validaNumero(numero):
                print("¡Correcto! Es un número impar válido.")
        except ValueError:
            print("Error: Debes ingresar un número entero.")

# Clase principal
class Aplicacion:
    def main(self):
        print("=== Juego de Adivinanza de Números Pares ===")
        juego_par = JuegoAdivinaPar()
        juego_par.juega()

        print("\n=== Juego de Adivinanza de Números Impares ===")
        juego_impar = JuegoAdivinaImpar()
        juego_impar.juega()

# Ejecutar la aplicación
if __name__ == "__main__":
    app = Aplicacion()
    app.main()
