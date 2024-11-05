package ace.ucv;


import java.util.Map;

// Nivelul 3: VehiculPersonal
class VehiculPersonal extends VehiculMotorizat {
    public VehiculPersonal(Map<String, Object> proprietatiInitiale) {
        super(proprietatiInitiale);
        adaugaProprietate("utilizare", "personal");
    }
}