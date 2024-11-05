package ace.ucv;

import java.util.Map;

// Nivelul 1: Vehicul
class Vehicul extends CadruVehicul {
    public Vehicul(Map<String, Object> proprietatiInitiale) {
        super("Vehicul", proprietatiInitiale);
    }

    public Vehicul() {
        super("Vehicul");
        adaugaProprietate("capacitate", "undefined");
        adaugaProprietate("viteza", "undefined");
    }
}