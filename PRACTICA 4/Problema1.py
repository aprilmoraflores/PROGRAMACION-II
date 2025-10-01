from abc import ABC, abstractmethod

# Clase abstracta Empleado
class Empleado(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_salario_mensual(self):
        pass

    def __str__(self):
        return f"Nombre: {self.nombre}"

# Clase EmpleadoTiempoCompleto
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_anual):
        super().__init__(nombre)
        self.salario_anual = salario_anual

    def calcular_salario_mensual(self):
        return self.salario_anual / 12

    def __str__(self):
        return f"{super().__str__()}, Tipo: Tiempo Completo, Salario Anual: {self.salario_anual:.2f}"

# Clase EmpleadoTiempoHorario
class EmpleadoTiempoHorario(Empleado):
    def __init__(self, nombre, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario_mensual(self):
        return self.horas_trabajadas * self.tarifa_por_hora

    def __str__(self):
        return (f"{super().__str__()}, Tipo: Tiempo Horario, "
                f"Horas: {self.horas_trabajadas:.2f}, Tarifa: {self.tarifa_por_hora:.2f}")

# Programa de prueba
def main():
    empleados = []

    print("Ingrese datos de 3 empleados a tiempo completo:")
    for i in range(3):
        nombre = input(f"Empleado {i+1} - Nombre: ")
        salario_anual = float(input("Salario anual: "))
        empleados.append(EmpleadoTiempoCompleto(nombre, salario_anual))

    print("\nIngrese datos de 2 empleados a tiempo horario:")
    for i in range(2):
        nombre = input(f"Empleado {i+4} - Nombre: ")
        horas = float(input("Horas trabajadas: "))
        tarifa = float(input("Tarifa por hora: "))
        empleados.append(EmpleadoTiempoHorario(nombre, horas, tarifa))

    print("\nResumen de empleados:")
    for emp in empleados:
        print(emp)
        print(f"Salario mensual: {emp.calcular_salario_mensual():.2f}")
        print("-" * 40)

if __name__ == "__main__":
    main()