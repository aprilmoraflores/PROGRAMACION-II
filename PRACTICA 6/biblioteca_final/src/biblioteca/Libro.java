
package biblioteca;
import java.io.Serializable;

public class Libro implements Serializable {
    private String titulo;
    private String isbn;
    private Autor autor;

    public Libro(String t,String i,Autor a){
        titulo=t; isbn=i; autor=a;
    }

    public String getTitulo(){ return titulo; }
    public Autor getAutor(){ return autor; }

    public String toString(){
        return titulo+" - "+autor.getNombre();
    }
}
