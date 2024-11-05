package ace.ucv;


import java.util.HashMap;
import java.util.Map;

// Clasa de bază CadruVehicul pentru toate vehiculele
abstract class CadruVehicul {
    protected String nume;
    protected Map<String, Object> proprietati;

    public CadruVehicul(String nume, Map<String, Object> proprietatiInitiale) {
        this.nume = nume;
        this.proprietati = new HashMap<>(proprietatiInitiale);
    }

    public CadruVehicul(String nume) {
        this.nume = nume;
        this.proprietati = new HashMap<>();
    }

    public void adaugaProprietate(String numeProprietate, Object valoare) {
        proprietati.put(numeProprietate, valoare);
    }

    public Object obtineValoareProprietate(String numeProprietate) {
        Object valoare = proprietati.getOrDefault(numeProprietate, "undefined");
        if (valoare instanceof CalculatorProprietate) {
            return ((CalculatorProprietate) valoare).calcul();
        }
        return valoare;
    }

    public void afiseazaProprietati() {
        System.out.println("Proprietăți pentru " + nume + ":");
        for (String numeProprietate : proprietati.keySet()) {
            System.out.println(numeProprietate + ": " + obtineValoareProprietate(numeProprietate));
        }
    }
}