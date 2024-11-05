package ace.ucv;

/**
 * Created by Andreea Draghici on 11/5/2024
 * Name of project: untitled
 */
// Clasa pentru proprietățile vehiculelor
class ProprietateVehicul {
    private String nume;
    private Object valoare;

    public ProprietateVehicul(String nume, Object valoare) {
        this.nume = nume;
        this.valoare = valoare;
    }

    public String getNume() {
        return nume;
    }

    public Object getValoare() {
        return valoare;
    }
}