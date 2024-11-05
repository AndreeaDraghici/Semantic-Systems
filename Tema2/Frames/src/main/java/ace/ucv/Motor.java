package ace.ucv;

import java.util.HashMap;
import java.util.Map;

// Clasa Motor folosind Pattern-ul Bunch
class Motor {
    private Map<String, Object> caracteristici;

    public Motor(Map<String, Object> caracteristiciInitiale) {
        this.caracteristici = new HashMap<>(caracteristiciInitiale);
    }

    public Object obtineCaracteristica(String numeCaracteristica) {
        return caracteristici.getOrDefault(numeCaracteristica, "undefined");
    }
}