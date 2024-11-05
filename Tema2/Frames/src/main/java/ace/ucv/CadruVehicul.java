package ace.ucv;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by Andreea Draghici on 11/5/2024
 * Name of project: untitled
 */
// Clasa de bază CadruVehicul, folosind Pattern-ul Bunch pentru flexibilitate
abstract class CadruVehicul {
    protected String nume;
    protected Map<String, Object> proprietati;

    // Constructor care permite specificarea unui număr variabil de atribute
    public CadruVehicul(String nume, Map<String, Object> proprietatiInitiale) {
        this.nume = nume;
        this.proprietati = new HashMap<>(proprietatiInitiale);
    }

    // Constructor fără proprietăți inițiale
    public CadruVehicul(String nume) {
        this.nume = nume;
        this.proprietati = new HashMap<>();
    }

    // Adaugă sau actualizează o proprietate
    public void adaugaProprietate(String numeProprietate, Object valoare) {
        proprietati.put(numeProprietate, valoare);
    }

    public Object obtineValoareProprietate(String numeProprietate) {
        Object valoare = proprietati.getOrDefault(numeProprietate, "undefined");
        if (valoare instanceof CalculatorProprietate) {
            return ((CalculatorProprietate) valoare).calcul(); // Apelează metoda calcul() pentru a obține valoarea
        }
        return valoare;
    }

}
