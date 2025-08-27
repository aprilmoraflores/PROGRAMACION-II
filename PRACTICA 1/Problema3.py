import math

class Estadistica:
    def __init__(self, datos):
        self.datos = datos

    def promedio(self):
        return sum(self.datos) / len(self.datos)

    def desviacion(self):
        prom = self.promedio()
        return math.sqrt(sum((x - prom) ** 2 for x in self.datos) / (len(self.datos) - 1))


if __name__ == "__main__":
    numeros = list(map(float, input("Ingrese 10 números: ").split()))
    estadistica = Estadistica(numeros)

    print(f"El promedio es {estadistica.promedio():.2f}")
    print(f"La desviación estándar es {estadistica.desviacion():.5f}")
