
package biblioteca;
import java.io.Serializable;

public class Estudiante implements Serializable {
    private String codigo;
    private String nombre;

    public Estudiante(String c, String n){
        this.codigo=c;
        this.nombre=n;
    }

    public String getCodigo(){ return codigo; }
    public String getNombre(){ return nombre; }

    public String toString(){
        return nombre+" ["+codigo+"]";
    }
}
