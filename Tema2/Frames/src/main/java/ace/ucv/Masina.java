package ace.ucv;

import java.util.Map;

// Nivelul 3: Clasa Masina
class Masina extends VehiculMotorizat {
    private Motor motor;
    private RezervorCombustibil rezervor;

    public Masina(Map<String, Object> proprietatiMotor, Map<String, Object> proprietatiRezervor) {
        super();
        this.motor = new Motor(proprietatiMotor);
        this.rezervor = new RezervorCombustibil(proprietatiRezervor);

        adaugaProprietate("tipCombustibil", motor.obtineCaracteristica("tipCombustibil"));
        adaugaProprietate("putereMotor", motor.obtineCaracteristica("putere"));
        adaugaProprietate("capacitateRezervor", rezervor.obtineCaracteristica("capacitate"));
    }
}