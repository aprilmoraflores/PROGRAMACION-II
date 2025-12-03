
import javax.swing.*;
import java.awt.*;
import biblioteca.Biblioteca;

public class Ventana extends JFrame {
    Biblioteca b = new Biblioteca();

    public Ventana(){
        setTitle("Biblioteca");
        setSize(400,300);
        setLayout(new GridLayout(3,2));

        JButton a=new JButton("Agregar Autor");
        JButton l=new JButton("Agregar Libro");
        JButton e=new JButton("Agregar Estudiante");
        JButton p=new JButton("Registrar Prestamo");
        JButton s=new JButton("Mostrar Estado");
        JButton x=new JButton("Salir");

        a.addActionListener(ev->new VentanaAgregarAutor(b));
        l.addActionListener(ev->new VentanaAgregarLibro(b));
        e.addActionListener(ev->new VentanaAgregarEstudiante(b));
        p.addActionListener(ev->new VentanaRegistrarPrestamo(b));
        s.addActionListener(ev->new VentanaMostrarEstado(b));
        x.addActionListener(ev->System.exit(0));

        add(a);add(l);add(e);add(p);add(s);add(x);

        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setVisible(true);
    }
}
