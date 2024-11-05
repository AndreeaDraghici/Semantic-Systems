package ace.ucv;

import java.util.Map;

/**
 * Created by Andreea Draghici on 11/5/2024
 * Name of project: untitled
 */
// Nivelul 3: Clasa Bicicleta
class Bicicleta extends VehiculNemotorizat {
    public Bicicleta(Map<String, Object> proprietatiInitiale) {
        super(proprietatiInitiale);
        adaugaProprietate("tipCadru", proprietatiInitiale.getOrDefault("tipCadru", "Aluminiu"));
    }
}