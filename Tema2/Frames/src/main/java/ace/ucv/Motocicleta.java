package ace.ucv;

import java.util.Map;

// Nivelul 4: Clasa Motocicleta
class Motocicleta extends VehiculMotorizat {
    public Motocicleta(Map<String, Object> proprietatiInitiale) {
        super(proprietatiInitiale);
        adaugaProprietate("casca", proprietatiInitiale.getOrDefault("casca", true));
    }
}