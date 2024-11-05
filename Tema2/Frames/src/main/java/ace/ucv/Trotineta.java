package ace.ucv;

import java.util.Map;

class Trotineta extends VehiculNemotorizat {
    public Trotineta(Map<String, Object> proprietatiInitiale) {
        super(proprietatiInitiale);
        adaugaProprietate("esteElectrica", proprietatiInitiale.getOrDefault("esteElectrica", true));
        adaugaProprietate("calculVitezaMaxima", new CalculVitezaMaxima());
    }

    private static class CalculVitezaMaxima implements CalculatorProprietate {
        public Object calcul() {
            boolean esteElectrica = true; // valoare exemplu
            return esteElectrica ? 25 : 15;
        }
    }
}