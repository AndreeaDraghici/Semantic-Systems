package ace.ucv;

import java.util.Map;

/**
 * Created by Andreea Draghici on 11/5/2024
 * Name of project: untitled
 */
// Nivelul 2: Specializarea VehiculMotorizat
class VehiculMotorizat extends Vehicul {
    public VehiculMotorizat(Map<String, Object> proprietatiInitiale) {
        super(proprietatiInitiale);
        adaugaProprietate("putereMotor", "undefined");
        adaugaProprietate("calculVitezaMaxima", new CalculVitezaMaxima());
        adaugaProprietate("calculConsumCombustibil", new CalculConsumCombustibil());
    }

    public VehiculMotorizat() {
        super();
        adaugaProprietate("putereMotor", "undefined");
        adaugaProprietate("calculVitezaMaxima", new CalculVitezaMaxima());
        adaugaProprietate("calculConsumCombustibil", new CalculConsumCombustibil());
    }

    private static class CalculVitezaMaxima implements CalculatorProprietate {
        public Object calcul() {
            int putereMotor = 150; // Exemplu simplu
            return putereMotor * 1.5;
        }
    }

    private static class CalculConsumCombustibil implements CalculatorProprietate {
        public Object calcul() {
            int putereMotor = 150; // Exemplu simplu
            return putereMotor / 10.0;
        }
    }
}