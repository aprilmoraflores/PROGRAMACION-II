
import biblioteca.*;
import javax.swing.*;

public class VentanaAgregarLibro extends JFrame {
    public VentanaAgregarLibro(Biblioteca b){
        setTitle("Agregar Libro");
        setSize(300,200);
        setLayout(new java.awt.GridLayout(4,2));

        JTextField titulo=new JTextField();
        JTextField isbn=new JTextField();
        JComboBox<String> combo=new JComboBox<>();

        for(Autor a:b.autores) combo.addItem(a.getNombre());

        add(new JLabel("Titulo:"));
        add(titulo);
        add(new JLabel("Autor:"));
        add(combo);

        JButton g=new JButton("Guardar");
        g.addActionListener(e->{
            Autor aut=b.autores.get(combo.getSelectedIndex());
            b.addLibro(new Libro(titulo.getText(),isbn.getText(),aut));
            JOptionPane.showMessageDialog(this,"Libro guardado");
        });
        add(g);

        JButton c=new JButton("Cerrar");
        c.addActionListener(e->dispose());
        add(c);

        setVisible(true);
    }
}
