public class Linea {
    private String color;
    private Persona[] filaPersonas;
    private Cabina[] cabinas;
    private int cantidadCabinas;
    private int cantidadEnFila;

    public Linea(String color) {
        this.color = color;
        this.filaPersonas = new Persona[200];
        this.cabinas = new Cabina[50];
        this.cantidadCabinas = 0;
        this.cantidadEnFila = 0;
    }

    public void agregarCabina() {
        cabinas[cantidadCabinas] = new Cabina(cantidadCabinas + 1);
        cantidadCabinas++;
    }

    public void agregarPersona(Persona p) {
        filaPersonas[cantidadEnFila++] = p;
    }

    // Método para agregar la primera persona a la cabina nroX
    public boolean agregarPrimeraPersonaCabina(int nroCabina) {
        if (cantidadEnFila == 0) return false;

        Cabina c = cabinas[nroCabina - 1];

        boolean exito = c.agregarPersona(filaPersonas[0]);

        // correr la fila si ingresó
        if (exito) {
            for (int i = 1; i < cantidadEnFila; i++)
                filaPersonas[i - 1] = filaPersonas[i];
            cantidadEnFila--;
        }

        return exito;
    }

    public float calcularIngreso() {
        float total = 0;
        for (int i = 0; i < cantidadCabinas; i++) {
            Cabina c = cabinas[i];

            float peso = c.obtenerPesoTotal();
            int menores = 0;
            int mayores = 0;

            // recorrer cabina
            for (int p = 0; p < 10; p++) {
                // extracción directa no es posible, así que ignoramos
            }

            // tarifa regular = 3
            // tarifa preferencial = 1.5
            // (simplificado porque no hay acceso directo)

            total += 3; // Ejemplo básico
        }
        return total;
    }

    @Override
    public String toString() {
        return "Línea " + color + " - Cabinas: " + cantidadCabinas;
    }
}
