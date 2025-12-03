
package biblioteca;
import java.io.Serializable;

public class Autor implements Serializable {
    private String nombre;
    private String nacionalidad;

    public Autor(String n, String nac){
        this.nombre=n;
        this.nacionalidad=nac;
    }

    public String getNombre(){ return nombre; }
    public String getNacionalidad(){ return nacionalidad; }

    public String toString(){
        return nombre + " ("+nacionalidad+")";
    }
}
