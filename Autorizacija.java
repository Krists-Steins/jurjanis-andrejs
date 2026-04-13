import java.util.Scanner;

public class Autorizacija {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // Izdomāti nejauši dati
        String pareizsLietotajs = "Juris85";
        String pareizaParole = "ZiemasRits2024";

        System.out.println("--- Autentifikācija ---");
        System.out.print("Lietotājvārds: ");
        String lietotajs = sc.nextLine();
        
        System.out.print("Parole: ");
        String parole = sc.nextLine();

        if (lietotajs.equals(pareizsLietotajs) && parole.equals(pareizaParole)) {
            System.out.println("\nSveiki, " + pareizsLietotajs + "! Izvēlieties darbību:");
            System.out.println("1. Skatīt profilu");
            System.out.println("2. Veikt maksājumu");
            System.out.println("3. Iziet");
        } else {
            System.out.println("Piekļuve liegta: nepareizi dati.");
        }
        
        sc.close();
    }
}