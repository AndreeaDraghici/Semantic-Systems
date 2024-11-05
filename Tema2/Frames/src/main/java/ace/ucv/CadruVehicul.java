package ace.ucv;

import java.util.Map;

public abstract class CadruVehicul {
    protected String nume;
    protected Bunch proprietati;

    public CadruVehicul(String nume) {
        this.nume = nume;
        this.proprietati = new Bunch();
    }

    public void adaugaProprietate(String numeProprietate, Object valoare) {
        proprietati.addAttribute(numeProprietate, valoare);
    }

    public Object obtineValoareProprietate(String numeProprietate) {
        return proprietati.getAttribute(numeProprietate);
    }

    public void afiseazaProprietati() {
        System.out.println("Proprietăți pentru " + nume + ":");
        for (Map.Entry<String, Object> entry : proprietati.getAllAttributes().entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}
