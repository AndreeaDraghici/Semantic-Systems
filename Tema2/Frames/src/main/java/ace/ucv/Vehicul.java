package ace.ucv;

import java.util.Map;

// Nivelul 1: Vehicul
class Vehicul extends CadruVehicul {
    // Constructor care permite inițializarea cu atributele dintr-un Map
    public Vehicul(Map<String, Object> proprietatiInitiale) {
        super("Vehicul");
        // Adăugăm proprietățile din Map la Bunch
        if (proprietatiInitiale != null) {
            for (Map.Entry<String, Object> entry : proprietatiInitiale.entrySet()) {
                adaugaProprietate(entry.getKey(), entry.getValue());
            }
        }
    }

    // Constructor default
    public Vehicul() {
        super("Vehicul");
        // Folosim Bunch pentru a adăuga atribute implicite
        adaugaProprietate("capacitate", "undefined");
        adaugaProprietate("viteza", "undefined");
    }
}
