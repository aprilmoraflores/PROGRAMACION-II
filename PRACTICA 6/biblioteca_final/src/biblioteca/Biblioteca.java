
package biblioteca;
import java.util.*;
import java.io.Serializable;

public class Biblioteca implements Serializable {
    public List<Autor> autores=new ArrayList<>();
    public List<Libro> libros=new ArrayList<>();
    public List<Estudiante> estudiantes=new ArrayList<>();
    public List<Prestamo> prestamos=new ArrayList<>();

    public void addAutor(Autor a){ autores.add(a); }
    public void addLibro(Libro l){ libros.add(l); }
    public void addEstudiante(Estudiante e){ estudiantes.add(e); }
    public void addPrestamo(Prestamo p){ prestamos.add(p); }
}
