public class Cabina {
    private int nroCabina;
    private Persona[] personasAbordo;
    private int cantidad;
    private final float PESO_MAX = 850;
    private final int MAX_PERSONAS = 10;

    public Cabina(int nroCabina) {
        this.nroCabina = nroCabina;
        this.personasAbordo = new Persona[10];
        this.cantidad = 0;
    }

    public boolean agregarPersona(Persona p) {
        if (cantidad >= MAX_PERSONAS)
            return false;

        float pesoTotal = 0;
        for (int i = 0; i < cantidad; i++)
            pesoTotal += personasAbordo[i].getPeso();

        if (pesoTotal + p.getPeso() > PESO_MAX)
            return false;

        personasAbordo[cantidad++] = p;
        return true;
    }

    public float obtenerPesoTotal() {
        float total = 0;
        for (int i = 0; i < cantidad; i++)
            total += personasAbordo[i].getPeso();
        return total;
    }

    public int getNroCabina() {
        return nroCabina;
    }

    @Override
    public String toString() {
        return "Cabina " + nroCabina + ": " + cantidad + " personas, Peso total = " + obtenerPesoTotal();
    }
}
