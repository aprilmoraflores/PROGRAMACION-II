
import javax.swing.*;
import biblioteca.Biblioteca;
import biblioteca.Autor;

public class VentanaAgregarAutor extends JFrame {
    public VentanaAgregarAutor(Biblioteca b){
        setTitle("Agregar Autor");
        setSize(300,200);
        setLayout(new java.awt.GridLayout(3,2));

        JTextField nombre=new JTextField();
        JTextField nac=new JTextField();

        add(new JLabel("Nombre:"));
        add(nombre);
        add(new JLabel("Nacionalidad:"));
        add(nac);

        JButton g=new JButton("Guardar");
        g.addActionListener(e->{
            b.addAutor(new Autor(nombre.getText(),nac.getText()));
            JOptionPane.showMessageDialog(this,"Autor guardado");
        });
        add(g);

        JButton c=new JButton("Cerrar");
        c.addActionListener(e->dispose());
        add(c);

        setVisible(true);
    }
}
