package ace.ucv;

import java.util.HashMap;
import java.util.Map;

// Clasa de baza CadruVehicul, folosind Pattern-ul Bunch pentru flexibilitate
abstract class CadruVehicul {
    protected String nume;
    protected Map<String, Object> proprietati;

    // Constructor care permite specificarea unui numar variabil de atribute
    public CadruVehicul(String nume, Map<String, Object> proprietatiInitiale) {
        this.nume = nume;
        this.proprietati = new HashMap<>(proprietatiInitiale);
    }

    // Constructor fara proprietati initiale
    public CadruVehicul(String nume) {
        this.nume = nume;
        this.proprietati = new HashMap<>();
    }

    // Adaugă sau actualizează o proprietate
    public void adaugaProprietate(String numeProprietate, Object valoare) {
        proprietati.put(numeProprietate, valoare);
    }

    // Obține valoarea unei proprietăți, apelând calcul() dacă este necesar
    public Object obtineValoareProprietate(String numeProprietate) {
        Object valoare = proprietati.getOrDefault(numeProprietate, "undefined");
        if (valoare instanceof CalculatorProprietate) {
            return ((CalculatorProprietate) valoare).calcul();
        }
        return valoare;
    }

    // Afișează toate proprietățile și valorile vehiculului
    public void afiseazaProprietati() {
        System.out.println("Proprietăți pentru " + nume + ":");
        for (String numeProprietate : proprietati.keySet()) {
            System.out.println(numeProprietate + ": " + obtineValoareProprietate(numeProprietate));
        }
    }
}