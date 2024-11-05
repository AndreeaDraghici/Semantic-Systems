package ace.ucv;

import java.util.Map;

// Nivelul 2: VehiculMotorizat
class VehiculMotorizat extends Vehicul {
    public VehiculMotorizat(Map<String, Object> proprietatiInitiale) {
        super(proprietatiInitiale);
        adaugaProprietate("putereMotor", proprietatiInitiale.getOrDefault("putereMotor", 0));
        adaugaProprietate("calculVitezaMaxima", new CalculVitezaMaxima());
        adaugaProprietate("calculConsumCombustibil", new CalculConsumCombustibil());
        adaugaProprietate("calculAutonomie", new CalculAutonomie());
    }

    private class CalculVitezaMaxima implements CalculatorProprietate {
        public Object calcul() {
            int putereMotor = (Integer) obtineValoareProprietate("putereMotor");
            return putereMotor * 1.5;
        }
    }

    private class CalculConsumCombustibil implements CalculatorProprietate {
        public Object calcul() {
            int putereMotor = (Integer) obtineValoareProprietate("putereMotor");
            return putereMotor / 10.0;
        }
    }

    private class CalculAutonomie implements CalculatorProprietate {
        public Object calcul() {
            Object consumCombustibilObj = obtineValoareProprietate("calculConsumCombustibil");
            Object capacitateRezervorObj = obtineValoareProprietate("capacitateRezervor");

            // Verificăm dacă consumCombustibil și capacitateRezervor sunt de tipul corect
            if (consumCombustibilObj instanceof Double && capacitateRezervorObj instanceof Integer) {
                double consumCombustibil = (Double) consumCombustibilObj;
                int capacitateRezervor = (Integer) capacitateRezervorObj;
                return (capacitateRezervor / consumCombustibil) * 100;
            } else {
                return "undefined"; // dacă valorile nu sunt de tipul corect
            }
        }
    }
}