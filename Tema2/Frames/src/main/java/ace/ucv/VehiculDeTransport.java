package ace.ucv;


import java.util.Map;

class VehiculDeTransport extends VehiculMotorizat {
    public VehiculDeTransport(Map<String, Object> proprietatiInitiale) {
        super(proprietatiInitiale);
        adaugaProprietate("utilizare", "transport");
    }
}