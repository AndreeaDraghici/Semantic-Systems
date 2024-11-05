package ace.ucv;


import java.util.Map;


class VehiculDeTransport extends VehiculMotorizat {
    // Constructor care permite initializarea cu atributele dintr-un Map
    public VehiculDeTransport(Map<String, Object> proprietatiInitiale) {
        super(proprietatiInitiale);
        // Proprietatea specifica pentru vehiculul de transport
        adaugaProprietate("utilizare", "transport");
    }
}
