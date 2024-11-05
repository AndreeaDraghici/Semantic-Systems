package ace.ucv;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by Andreea Draghici on 11/5/2024
 * Name of project: untitled
 */
// Clasa RezervorCombustibil folosind Pattern-ul Bunch
class RezervorCombustibil {
    private Map<String, Object> caracteristici;

    public RezervorCombustibil(Map<String, Object> caracteristiciInitiale) {
        this.caracteristici = new HashMap<>(caracteristiciInitiale);
    }

    public Object obtineCaracteristica(String numeCaracteristica) {
        return caracteristici.getOrDefault(numeCaracteristica, "undefined");
    }

    public void afiseazaCaracteristici() {
        System.out.println("Caracteristicile rezervorului:");
        for (Map.Entry<String, Object> entry : caracteristici.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}