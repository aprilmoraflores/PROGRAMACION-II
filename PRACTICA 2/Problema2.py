import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Representación en texto
    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

    # Suma de vectores
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    # Resta de vectores
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    # Multiplicación por escalar o producto escalar
    def __mul__(self, other):
        if isinstance(other, (int, float)):  # Escalar * vector
            return Vector3D(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector3D):    # Producto escalar
            return self.x * other.x + self.y * other.y + self.z * other.z

    # Producto vectorial usando ^
    def __xor__(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    # Longitud del vector
    def norma(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    # Normalización del vector
    def normalizado(self):
        n = self.norma()
        if n == 0:
            raise ValueError("No se puede normalizar un vector nulo")
        return Vector3D(self.x/n, self.y/n, self.z/n)

    # Proyección de a sobre b
    def proyeccion_sobre(self, b):
        escalar = (self * b) / (b.norma()**2)
        return b * escalar

    # Componente de a en la dirección de b
    def componente_en(self, b):
        return (self * b) / b.norma()

    # Verificar perpendicularidad (producto escalar = 0)
    def es_perpendicular(self, other):
        return self * other == 0

    # Verificar paralelismo (producto vectorial = 0)
    def es_paralelo(self, other):
        return (self ^ other).norma() == 0


# ================== PRUEBAS ==================
if __name__ == "__main__":
    a = Vector3D(2, 3, 1)
    b = Vector3D(4, 6, 2)
    c = Vector3D(-3, 2, 0)

    print("Vector a:", a)
    print("Vector b:", b)
    print("Vector c:", c)

    print("\n--- Operaciones básicas ---")
    print("a + b =", a + b)
    print("a - b =", a - b)
    print("2 * a =", a * 2)
    print("a · b =", a * b)
    print("a × c =", a ^ c)
    print("|a| =", a.norma())
    print("Normalizado a =", a.normalizado())

    print("\n--- Verificaciones ---")
    print("¿a ⟂ c?", a.es_perpendicular(c))
    print("¿a ∥ b?", a.es_paralelo(b))

    print("\n--- Proyección y componente ---")
    print("Proyección de a sobre b:", a.proyeccion_sobre(b))
    print("Componente de a en dirección de b:", a.componente_en(b))
