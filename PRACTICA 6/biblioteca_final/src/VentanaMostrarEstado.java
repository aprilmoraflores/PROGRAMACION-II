
import javax.swing.*;
import biblioteca.*;

public class VentanaMostrarEstado extends JFrame {
    public VentanaMostrarEstado(Biblioteca b){
        setTitle("Estado Biblioteca");
        setSize(400,300);

        JTextArea txt=new JTextArea();
        txt.setEditable(false);

        txt.append("Autores:\n");
        for(Autor a:b.autores) txt.append(" - "+a+"\n");

        txt.append("\nLibros:\n");
        for(Libro l:b.libros) txt.append(" - "+l+"\n");

        txt.append("\nEstudiantes:\n");
        for(Estudiante e:b.estudiantes) txt.append(" - "+e+"\n");

        txt.append("\nPrestamos:\n");
        for(Prestamo p:b.prestamos) txt.append(" - "+p+"\n");

        add(new JScrollPane(txt));
        setVisible(true);
    }
}
