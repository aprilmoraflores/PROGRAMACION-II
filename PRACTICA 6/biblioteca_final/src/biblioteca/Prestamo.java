
package biblioteca;
import java.io.Serializable;

public class Prestamo implements Serializable {
    private Estudiante est;
    private Libro libro;

    public Prestamo(Estudiante e, Libro l){
        est=e; libro=l;
    }

    public String toString(){
        return "Prestamo: "+est.getNombre() +" -> "+ libro.getTitulo();
    }
}
