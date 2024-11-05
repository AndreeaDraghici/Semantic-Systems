package ace.ucv;

import java.util.Map;

/**
 * Created by Andreea Draghici on 11/5/2024
 * Name of project: untitled
 */
// Nivelul 3: Clasa Motocicleta
class Motocicleta extends VehiculMotorizat {
    public Motocicleta(Map<String, Object> proprietatiInitiale) {
        super(proprietatiInitiale);
        adaugaProprietate("casca", proprietatiInitiale.getOrDefault("casca", true));
    }
}