
import biblioteca.Biblioteca;
import biblioteca.Estudiante;
import javax.swing.*;

public class VentanaAgregarEstudiante extends JFrame {
    public VentanaAgregarEstudiante(Biblioteca b){
        setTitle("Agregar Estudiante");
        setSize(300,200);
        setLayout(new java.awt.GridLayout(3,2));

        JTextField cod=new JTextField();
        JTextField nom=new JTextField();

        add(new JLabel("Nombre:"));
        add(nom);

        JButton g=new JButton("Guardar");
        g.addActionListener(e->{
            b.addEstudiante(new Estudiante(cod.getText(),nom.getText()));
            JOptionPane.showMessageDialog(this,"Estudiante guardado");
        });
        add(g);

        JButton c=new JButton("Cerrar");
        c.addActionListener(e->dispose());
        add(c);

        setVisible(true);
    }
}
