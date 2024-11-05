package ace.ucv;


import java.util.Map;

class Camion extends VehiculDeTransport {
    public Camion(Map<String, Object> proprietatiMotor, Map<String, Object> proprietatiRezervor) {
        super(proprietatiMotor);
        adaugaProprietate("tipCombustibil", proprietatiMotor.get("tipCombustibil"));
        adaugaProprietate("putereMotor", proprietatiMotor.get("putereMotor"));
        adaugaProprietate("capacitateRezervor", proprietatiRezervor.get("capacitateRezervor"));
        adaugaProprietate("capacitateIncarcare", 10000);
    }
}