
import javax.swing.*;
import biblioteca.*;

public class VentanaRegistrarPrestamo extends JFrame {
    public VentanaRegistrarPrestamo(Biblioteca b){
        setTitle("Registrar Prestamo");
        setSize(300,200);
        setLayout(new java.awt.GridLayout(3,2));

        JComboBox<String> est=new JComboBox<>();
        JComboBox<String> lib=new JComboBox<>();

        for(Estudiante e: b.estudiantes) est.addItem(e.getNombre());
        for(Libro l: b.libros) lib.addItem(l.getTitulo());

        add(new JLabel("Estudiante:"));
        add(est);
        add(new JLabel("Libro:"));
        add(lib);

        JButton g=new JButton("Guardar");
        g.addActionListener(e->{
            b.addPrestamo(new Prestamo(
                b.estudiantes.get(est.getSelectedIndex()),
                b.libros.get(lib.getSelectedIndex())
            ));
            JOptionPane.showMessageDialog(this,"Prestamo registrado");
        });
        add(g);

        JButton c=new JButton("Cerrar");
        c.addActionListener(e->dispose());
        add(c);

        setVisible(true);
    }
}
