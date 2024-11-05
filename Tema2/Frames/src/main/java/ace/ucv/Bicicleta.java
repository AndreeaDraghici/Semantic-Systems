package ace.ucv;

import java.util.Map;

// Nivelul 3: Clasa Bicicleta
class Bicicleta extends VehiculNemotorizat {
    public Bicicleta(Map<String, Object> proprietatiInitiale) {
        super(proprietatiInitiale);
        adaugaProprietate("tipCadru", proprietatiInitiale.getOrDefault("tipCadru", "Aluminiu"));
    }
}
