package ace.ucv;

import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        // Definim caracteristicile pentru motor și rezervor
        Map<String, Object> proprietatiMotor = new HashMap<>();
        proprietatiMotor.put("putere", 250);
        proprietatiMotor.put("tipCombustibil", "Diesel");

        Map<String, Object> proprietatiRezervor = new HashMap<>();
        proprietatiRezervor.put("capacitate", 60);

        // Instanțierea unei mașini cu motor și rezervor configurabile
        Masina masinaFamilie = new Masina(proprietatiMotor, proprietatiRezervor);

        // Definim și creăm o motocicletă
        Map<String, Object> proprietatiMotocicleta = new HashMap<>();
        proprietatiMotocicleta.put("casca", true);
        Motocicleta motocicletaSport = new Motocicleta(proprietatiMotocicleta);

        // Definim și creăm o bicicletă
        Map<String, Object> proprietatiBicicleta = new HashMap<>();
        proprietatiBicicleta.put("tipCadru", "Aluminiu");
        Bicicleta bicicletaMountain = new Bicicleta(proprietatiBicicleta);

        // Definim și creăm o trotinetă electrică
        Map<String, Object> proprietatiTrotineta = new HashMap<>();
        proprietatiTrotineta.put("esteElectrica", true);
        Trotineta trotinetaElectrica = new Trotineta(proprietatiTrotineta);

        // Afișăm toate proprietățile pentru fiecare vehicul
        System.out.println("Detalii Masina Familie:");
        masinaFamilie.afiseazaProprietati();

        System.out.println("\nDetalii Motocicleta Sport:");
        motocicletaSport.afiseazaProprietati();

        System.out.println("\nDetalii Bicicleta Mountain:");
        bicicletaMountain.afiseazaProprietati();

        System.out.println("\nDetalii Trotineta Electrica:");
        trotinetaElectrica.afiseazaProprietati();
    }
}
