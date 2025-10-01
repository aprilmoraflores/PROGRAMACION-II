import random
import math
from abc import ABC, abstractmethod

# Interfaz simulada
class Coloreado:
    def como_colorear(self):
        pass

# Clase abstracta Figura
class Figura(ABC):
    def __init__(self, color="Sin color"):
        self.color = color

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def __str__(self):
        return f"Color: {self.color}"

# Clase Cuadrado que implementa Coloreado
class Cuadrado(Figura, Coloreado):
    def __init__(self, lado, color="Rojo"):
        super().__init__(color)
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

    def como_colorear(self):
        return "Colorear los cuatro lados"

    def __str__(self):
        return f"Cuadrado - Lado: {self.lado:.2f}, {super().__str__()}"

# Clase Circulo
class Circulo(Figura):
    def __init__(self, radio, color="Azul"):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Circulo - Radio: {self.radio:.2f}, {super().__str__()}"

# Programa de prueba
def main():
    figuras = []

    print("Generando 5 figuras aleatorias...\n")
    for i in range(5):
        tipo = random.randint(1, 2)
        if tipo == 1:
            lado = round(random.uniform(1.0, 10.0), 2)
            figura = Cuadrado(lado)
        else:
            radio = round(random.uniform(1.0, 10.0), 2)
            figura = Circulo(radio)
        figuras.append(figura)

    print("Resumen de figuras:")
    for fig in figuras:
        print(fig)
        print(f"Área: {fig.area():.2f}")
        print(f"Perímetro: {fig.perimetro():.2f}")
        if isinstance(fig, Coloreado):
            print(f"Coloreado: {fig.como_colorear()}")
        print("-" * 40)

if __name__ == "__main__":
    main()