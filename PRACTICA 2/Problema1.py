import math

class AlgebraVectorial:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    # Representación del vector
    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

    # Norma (módulo del vector)
    def norma(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    # Suma de vectores
    def __add__(self, other):
        return AlgebraVectorial(self.x + other.x, self.y + other.y, self.z + other.z)

    # Resta de vectores
    def __sub__(self, other):
        return AlgebraVectorial(self.x - other.x, self.y - other.y, self.z - other.z)

    # Producto escalar (dot product)
    def __mul__(self, other):
        if isinstance(other, AlgebraVectorial):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, (int, float)):
            return AlgebraVectorial(self.x * other, self.y * other, self.z * other)

    # Producto cruz (cross product)
    def __xor__(self, other):
        return AlgebraVectorial(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    # Verificar perpendicularidad
    def es_perpendicular(self, other):
        return self * other == 0

    # Verificar paralelismo
    def es_paralelo(self, other):
        return (self ^ other).norma() == 0

    # Proyección de a sobre b
    def proyeccion_sobre(self, other):
        escalar = (self * other) / (other.norma() ** 2)
        return other * escalar

    # Componente de a en la dirección de b
    def componente_en(self, other):
        return (self * other) / other.norma()


# ================== PRUEBAS ==================
if __name__ == "__main__":
    a = AlgebraVectorial(2, 3, 1)
    b = AlgebraVectorial(4, 6, 2)
    c = AlgebraVectorial(-3, 2, 0)

    print("Vector a:", a)
    print("Vector b:", b)
    print("Vector c:", c)

    # Operaciones
    print("\n--- Operaciones ---")
    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a · b =", a * b)
    print("a × b =", a ^ b)

    print("\n--- Verificaciones ---")
    print("¿a ⟂ c? :", a.es_perpendicular(c))
    print("¿a ∥ b? :", a.es_paralelo(b))

    print("\n--- Proyección y componente ---")
    print("Proyección de a sobre b:", a.proyeccion_sobre(b))
    print("Componente de a en dirección de b:", a.componente_en(b))
