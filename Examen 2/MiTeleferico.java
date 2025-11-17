public class MiTeleferico {
    private Linea[] lineas;
    private int cantLineas;

    public MiTeleferico() {
        this.lineas = new Linea[5];
        this.cantLineas = 0;
    }

    public void agregarLinea(String color) {
        lineas[cantLineas++] = new Linea(color);
    }

    public Linea getLinea(String color) {
        for (int i = 0; i < cantLineas; i++) {
            if (lineas[i].toString().contains(color))
                return lineas[i];
        }
        return null;
    }

    @Override
    public String toString() {
        String s = "Mi Teleférico:\n";
        for (int i = 0; i < cantLineas; i++)
            s += " - " + lineas[i] + "\n";
        return s;
    }
}
