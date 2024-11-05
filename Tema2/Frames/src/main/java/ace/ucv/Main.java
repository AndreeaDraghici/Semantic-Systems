package ace.ucv;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by Andreea Draghici on 11/5/2024
 * Name of project: Default (Template) Project
 */
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

        // Interogări și afișare pentru fiecare vehicul
        System.out.println("Capacitate rezervor Masina Familie: " + masinaFamilie.obtineValoareProprietate("capacitateRezervor"));
        System.out.println("Tip combustibil Masina Familie: " + masinaFamilie.obtineValoareProprietate("tipCombustibil"));
        System.out.println("Putere motor Masina Familie: " + masinaFamilie.obtineValoareProprietate("putereMotor"));

        System.out.println("\nCasca Motocicleta Sport: " + motocicletaSport.obtineValoareProprietate("casca"));

        System.out.println("\nTip cadru Bicicleta Mountain: " + bicicletaMountain.obtineValoareProprietate("tipCadru"));

        System.out.println("\nViteza maxima Trotineta Electrica: " + trotinetaElectrica.obtineValoareProprietate("calculVitezaMaxima"));
        System.out.println("Este electrica Trotineta Electrica: " + trotinetaElectrica.obtineValoareProprietate("esteElectrica"));

    }
}