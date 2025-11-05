from datetime import date, timedelta

# Clase Autor (Agregación)
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrar_info(self):
        print(f"Autor: {self.nombre} - {self.nacionalidad}")

# Clase Estudiante (Asociación)
class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def mostrar_info(self):
        print(f"Estudiante: {self.codigo} - {self.nombre}")

# Clase Libro con Páginas (Composición)
class Libro:
    class Pagina:
        def __init__(self, numero, contenido):
            self.numero = numero
            self.contenido = contenido

        def mostrar_pagina(self):
            print(f"Página {self.numero}: {self.contenido}")

    def __init__(self, titulo, isbn, autor, contenidos_paginas):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor
        self.paginas = []
        numero = 1
        for contenido in contenidos_paginas:
            self.paginas.append(Libro.Pagina(numero, contenido))
            numero += 1

    def leer(self):
        print(f"Leyendo '{self.titulo}' (ISBN: {self.isbn}):")
        for p in self.paginas:
            p.mostrar_pagina()

# Clase Prestamo (Asociación entre Estudiante y Libro)
class Prestamo:
    def __init__(self, estudiante, libro):
        self.estudiante = estudiante
        self.libro = libro
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(weeks=2)

    def mostrar_info(self):
        print("--- Préstamo ---")
        print(f"Estudiante: {self.estudiante.nombre}")
        print(f"Libro: {self.libro.titulo} ({self.libro.isbn})")
        print(f"Fecha préstamo: {self.fecha_prestamo} | Fecha devolución: {self.fecha_devolucion}")

# Clase Biblioteca (Composición con Horario, Agregación con Autor y Libro)
class Biblioteca:
    class Horario:
        def __init__(self, dias, hora_apertura, hora_cierre):
            self.dias = dias
            self.hora_apertura = hora_apertura
            self.hora_cierre = hora_cierre

        def mostrar_horario(self):
            print(f"Horario: {self.dias} | {self.hora_apertura} - {self.hora_cierre}")

    def __init__(self, nombre, dias, hora_apertura, hora_cierre):
        self.nombre = nombre
        self.lista_libros = []
        self.lista_autores = []
        self.prestamos_activos = []
        self.horario = Biblioteca.Horario(dias, hora_apertura, hora_cierre)
        print(f"Biblioteca '{nombre}' inaugurada.")

    def agregar_autor(self, autor):
        self.lista_autores.append(autor)
        print(f"Autor registrado: {autor.nombre}")

    def agregar_libro(self, libro):
        self.lista_libros.append(libro)
        print(f"Libro agregado: {libro.titulo}")

    def prestar_libro(self, estudiante, libro):
        if libro not in self.lista_libros:
            print(f"El libro '{libro.titulo}' no está disponible en la biblioteca.")
            return
        prestamo = Prestamo(estudiante, libro)
        self.prestamos_activos.append(prestamo)
        print(f"Préstamo creado: {estudiante.nombre} -> {libro.titulo}")

    def mostrar_estado(self):
        print(f"\n=== Estado de la Biblioteca: {self.nombre} ===")
        if self.horario:
            self.horario.mostrar_horario()
        else:
            print("Horario eliminado (biblioteca cerrada).")

        print("\nAutores registrados:")
        if not self.lista_autores:
            print("- Ninguno")
        else:
            for a in self.lista_autores:
                a.mostrar_info()

        print("\nLibros disponibles:")
        if not self.lista_libros:
            print("- Ninguno")
        else:
            for l in self.lista_libros:
                print(f"- {l.titulo} ({l.isbn}) - Autor: {l.autor.nombre}")

        print("\nPréstamos activos:")
        if not self.prestamos_activos:
            print("- Ninguno")
        else:
            for p in self.prestamos_activos:
                p.mostrar_info()

    def cerrar_biblioteca(self):
        print(f"\nCerrando biblioteca '{self.nombre}'. Todos los préstamos serán cancelados.")
        self.prestamos_activos.clear()
        self.horario = None
        print("Horario eliminado (ya no existe fuera de la biblioteca).\n")

# Ejecución principal (demostración)
def main():
    a1 = Autor("Gabriel García Márquez", "Colombiano")
    a2 = Autor("Jane Austen", "Inglesa")

    contenidos1 = ["En un lugar de La Mancha...", "Capítulo 2: ..."]
    libro1 = Libro("Cien años de soledad", "ISBN-0001", a1, contenidos1)

    contenidos2 = ["It is a truth universally acknowledged...", "Capítulo 2: ..."]
    libro2 = Libro("Orgullo y Prejuicio", "ISBN-0002", a2, contenidos2)

    bib = Biblioteca("Biblioteca UMSA", "Lun-Vie", "08:00", "18:00")

    bib.agregar_autor(a1)
    bib.agregar_autor(a2)
    bib.agregar_libro(libro1)
    bib.agregar_libro(libro2)

    bib.mostrar_estado()

    e1 = Estudiante("2025001", "Ana Perez")
    e2 = Estudiante("2025002", "Luis Gomez")

    bib.prestar_libro(e1, libro1)
    bib.prestar_libro(e2, libro2)

    bib.mostrar_estado()

    print("\nLectura del libro1 (demostrando composición):")
    libro1.leer()

    bib.cerrar_biblioteca()
    bib.mostrar_estado()

    print("\nLos objetos Autor y Libro siguen existiendo fuera de la biblioteca:")
    a1.mostrar_info()
    libro1.leer()

if __name__ == "__main__":
    main()
