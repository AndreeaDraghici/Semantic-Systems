package ace.ucv;

import java.util.Map;

// Nivelul 4: Automobil și Camion
class Automobil extends VehiculPersonal {
    private Motor motor;
    private RezervorCombustibil rezervor;

    public Automobil(Map<String, Object> proprietatiMotor, Map<String, Object> proprietatiRezervor) {
        super(proprietatiMotor);
        this.motor = new Motor(proprietatiMotor);
        this.rezervor = new RezervorCombustibil(proprietatiRezervor);
        adaugaProprietate("tipCombustibil", motor.obtineCaracteristica("tipCombustibil"));
        adaugaProprietate("putereMotor", motor.obtineCaracteristica("putere"));
        adaugaProprietate("capacitateRezervor", rezervor.obtineCaracteristica("capacitate"));
    }
}