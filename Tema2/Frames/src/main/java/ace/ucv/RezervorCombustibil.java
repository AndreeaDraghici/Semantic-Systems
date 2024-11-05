package ace.ucv;

import java.util.HashMap;
import java.util.Map;

// Clasa RezervorCombustibil folosind Pattern-ul Bunch
class RezervorCombustibil {
    private Map<String, Object> caracteristici;

    public RezervorCombustibil(Map<String, Object> caracteristiciInitiale) {
        this.caracteristici = new HashMap<>(caracteristiciInitiale);
    }

    public Object obtineCaracteristica(String numeCaracteristica) {
        return caracteristici.getOrDefault(numeCaracteristica, "undefined");
    }
}