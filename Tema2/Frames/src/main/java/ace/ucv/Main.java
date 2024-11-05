package ace.ucv;

import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        // Definirea caracteristicilor pentru Motor și Rezervor
        Map<String, Object> proprietatiMotor = new HashMap<>();
        proprietatiMotor.put("putere", 250); // Integer
        proprietatiMotor.put("tipCombustibil", "Diesel");

        Map<String, Object> proprietatiRezervor = new HashMap<>();
        proprietatiRezervor.put("capacitate", 60); // Integer

        // Crearea unei instanțe de Automobil, care este un VehiculPersonal
        Automobil masinaFamilie = new Automobil(proprietatiMotor, proprietatiRezervor);

        // Caracteristicile pentru Camion
        Map<String, Object> proprietatiMotorCamion = new HashMap<>();
        proprietatiMotorCamion.put("putereMotor", 400); // Integer pentru camion
        proprietatiMotorCamion.put("tipCombustibil", "Motorina");

        Map<String, Object> proprietatiRezervorCamion = new HashMap<>();
        proprietatiRezervorCamion.put("capacitateRezervor", 120); // Integer mai mare pentru camion

        // Instanța de Camion
        Camion camionMarfa = new Camion(proprietatiMotorCamion, proprietatiRezervorCamion);

        // Instanța de Bicicleta
        Map<String, Object> proprietatiBicicleta = new HashMap<>();
        proprietatiBicicleta.put("tipCadru", "Carbon");
        Bicicleta bicicletaMountain = new Bicicleta(proprietatiBicicleta);

        // Instanța de Trotineta
        Map<String, Object> proprietatiTrotineta = new HashMap<>();
        proprietatiTrotineta.put("esteElectrica", true);
        Trotineta trotinetaElectrica = new Trotineta(proprietatiTrotineta);

        // Instanța de Motocicleta
        Map<String, Object> proprietatiMotocicleta = new HashMap<>();
        proprietatiMotocicleta.put("putereMotor", 10);
        proprietatiMotocicleta.put("tipCombustibil", "Benzina");
        proprietatiMotocicleta.put("casca", true);

        // Instanța de Motocicleta
        Motocicleta motocicletaSport = new Motocicleta(proprietatiMotocicleta);

        System.out.println("Detalii Automobil - Masina de Familie:");
        masinaFamilie.afiseazaProprietati();

        System.out.println("\nDetalii Bicicleta - Bicicleta Mountain:");
        bicicletaMountain.afiseazaProprietati();

        System.out.println("\nDetalii Trotineta - Trotineta Electrica:");
        trotinetaElectrica.afiseazaProprietati();


        System.out.println("\nDetalii Camion - Camion de Marfa:");
        camionMarfa.afiseazaProprietati();

        System.out.println("\nDetalii Motocicleta - Motocicleta Sport:");
        motocicletaSport.afiseazaProprietati();

    }
}
