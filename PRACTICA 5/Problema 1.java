import java.util.*;
import java.time.LocalDate;

// Clase Autor (existe independientemente) - AGREGACIÓN con Biblioteca
class Autor {
    private String nombre;
    private String nacionalidad;

    public Autor(String nombre, String nacionalidad) {
        this.nombre = nombre;
        this.nacionalidad = nacionalidad;
    }

    public void mostrarInfo() {
        System.out.println("Autor: " + nombre + " - " + nacionalidad);
    }

    public String getNombre() {
        return nombre;
    }
}

// Clase Estudiante (existe independientemente) - Asociado por Préstamo
class Estudiante {
    private String codigo;
    private String nombre;

    public Estudiante(String codigo, String nombre) {
        this.codigo = codigo;
        this.nombre = nombre;
    }

    public void mostrarInfo() {
        System.out.println("Estudiante: " + codigo + " - " + nombre);
    }

    public String getNombre() {
        return nombre;
    }
}

// Clase Libro: tiene Páginas en COMPOSICIÓN
class Libro {
    private String titulo;
    private String isbn;
    private Autor autor;
    private List<Pagina> paginas;

    // Clase interna Pagina (COMPOSICIÓN)
    public class Pagina {
        private int numero;
        private String contenido;

        private Pagina(int numero, String contenido) {
            this.numero = numero;
            this.contenido = contenido;
        }

        public void mostrarPagina() {
            System.out.println("Página " + numero + ": " + contenido);
        }
    }

    public Libro(String titulo, String isbn, Autor autor, List<String> contenidosPaginas) {
        this.titulo = titulo;
        this.isbn = isbn;
        this.autor = autor;
        this.paginas = new ArrayList<>();
        int n = 1;
        for (String c : contenidosPaginas) {
            this.paginas.add(new Pagina(n++, c));
        }
    }

    public void leer() {
        System.out.println("Leyendo '" + titulo + "' (ISBN: " + isbn + "):");
        for (Pagina p : paginas) {
            p.mostrarPagina();
        }
    }

    public String getTitulo() {
        return titulo;
    }

    public String getIsbn() {
        return isbn;
    }

    public Autor getAutor() {
        return autor;
    }
}

// Clase Prestamo: ASOCIACIÓN entre Estudiante y Libro
class Prestamo {
    private LocalDate fechaPrestamo;
    private LocalDate fechaDevolucion;
    private Estudiante estudiante;
    private Libro libro;

    public Prestamo(Estudiante estudiante, Libro libro) {
        this.estudiante = estudiante;
        this.libro = libro;
        this.fechaPrestamo = LocalDate.now();
        this.fechaDevolucion = fechaPrestamo.plusWeeks(2);
    }

    public void mostrarInfo() {
        System.out.println("--- Préstamo ---");
        System.out.println("Estudiante: " + estudiante.getNombre());
        System.out.println("Libro: " + libro.getTitulo() + " (" + libro.getIsbn() + ")");
        System.out.println("Fecha préstamo: " + fechaPrestamo + " | Fecha devolución: " + fechaDevolucion);
    }
}

// Clase Biblioteca (COMPOSICIÓN con Horario, AGREGACIÓN con Autor y Libro)
class Biblioteca {
    private String nombre;
    private List<Libro> listaLibros;
    private List<Autor> listaAutores;
    private List<Prestamo> prestamosActivos;
    private Horario horario;

    // Clase interna Horario (COMPOSICIÓN)
    public class Horario {
        private String diasApertura;
        private String horaApertura;
        private String horaCierre;

        public Horario(String diasApertura, String horaApertura, String horaCierre) {
            this.diasApertura = diasApertura;
            this.horaApertura = horaApertura;
            this.horaCierre = horaCierre;
        }

        public void mostrarHorario() {
            System.out.println("Horario: " + diasApertura + " | " + horaApertura + " - " + horaCierre);
        }
    }

    public Biblioteca(String nombre, String dias, String hApertura, String hCierre) {
        this.nombre = nombre;
        this.listaLibros = new ArrayList<>();
        this.listaAutores = new ArrayList<>();
        this.prestamosActivos = new ArrayList<>();
        this.horario = new Horario(dias, hApertura, hCierre);
        System.out.println("Biblioteca '" + nombre + "' inaugurada.");
    }

    public void agregarLibro(Libro libro) {
        listaLibros.add(libro);
        System.out.println("Libro agregado a la biblioteca: " + libro.getTitulo());
    }

    public void agregarAutor(Autor autor) {
        listaAutores.add(autor);
        System.out.println("Autor registrado: " + autor.getNombre());
    }

    public void prestarLibro(Estudiante estudiante, Libro libro) {
        if (!listaLibros.contains(libro)) {
            System.out.println("El libro '" + libro.getTitulo() + "' no está disponible en la biblioteca.");
            return;
        }
        Prestamo p = new Prestamo(estudiante, libro);
        prestamosActivos.add(p);
        System.out.println("Préstamo creado: " + estudiante.getNombre() + " -> " + libro.getTitulo());
    }

    public void mostrarEstado() {
        System.out.println("\n=== Estado de la Biblioteca: " + nombre + " ===");
        if (horario != null) {
            horario.mostrarHorario();
        }

        System.out.println("\nAutores registrados:");
        if (listaAutores.isEmpty()) System.out.println("- Ninguno");
        else for (Autor a : listaAutores) a.mostrarInfo();

        System.out.println("\nLibros disponibles:");
        if (listaLibros.isEmpty()) System.out.println("- Ninguno");
        else for (Libro l : listaLibros)
            System.out.println("- " + l.getTitulo() + " (" + l.getIsbn() + ") - Autor: " + l.getAutor().getNombre());

        System.out.println("\nPréstamos activos:");
        if (prestamosActivos.isEmpty()) System.out.println("- Ninguno");
        else for (Prestamo pr : prestamosActivos) pr.mostrarInfo();
    }

    public void cerrarBiblioteca() {
        System.out.println("\nCerrando biblioteca '" + nombre + "'. Todos los préstamos serán cancelados.");
        prestamosActivos.clear();
        horario = null;
        System.out.println("Horario eliminado (ya no existe fuera de la biblioteca).");
    }
}

// Clase principal (demostración de las tres relaciones)
public class SistemaBibliotecaDemo {
    public static void main(String[] args) {
        Autor a1 = new Autor("Gabriel García Márquez", "Colombiano");
        Autor a2 = new Autor("Jane Austen", "Inglesa");

        List<String> paginas1 = Arrays.asList("En un lugar de La Mancha...", "Capítulo 2: ...");
        Libro libro1 = new Libro("Cien años de soledad", "ISBN-0001", a1, paginas1);

        List<String> paginas2 = Arrays.asList("It is a truth universally acknowledged...", "Capítulo 2: ...");
        Libro libro2 = new Libro("Orgullo y Prejuicio", "ISBN-0002", a2, paginas2);

        Biblioteca bib = new Biblioteca("Biblioteca UMSA", "Lun-Vie", "08:00", "18:00");
        bib.agregarAutor(a1);
        bib.agregarAutor(a2);
        bib.agregarLibro(libro1);
        bib.agregarLibro(libro2);

        bib.mostrarEstado();

        Estudiante e1 = new Estudiante("2025001", "Ana Perez");
        Estudiante e2 = new Estudiante("2025002", "Luis Gomez");

        bib.prestarLibro(e1, libro1);
        bib.prestarLibro(e2, libro2);

        bib.mostrarEstado();

        System.out.println("\nLectura del libro1 (demostrando composición):");
        libro1.leer();

        bib.cerrarBiblioteca();
        bib.mostrarEstado();

        System.out.println("\nLos objetos Autor y Libro siguen existiendo fuera de la biblioteca:");
        a1.mostrarInfo();
        libro1.leer();
    }
}
