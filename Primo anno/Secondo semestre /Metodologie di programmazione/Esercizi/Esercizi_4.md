<p align="center">
  <h2 align="center">Esercizio Capitolo 4 </h2>
  <p align="center">I miei esercizi di Java!</p>
</p>

## Sommario ➕

- [Esercizio 1](#Esercizio_1)
- [Esercizio 2](#Esercizio_2)
- [Esercizio 3](#Esercizio_3)
- [Esercizio 4](#Esercizio_4)
- [Esercizio 5](#Esercizio_5)
- [Esercizio 6](#Esercizio_6)
- [Esercizio 7](#Esercizio_7)
- [Esercizio 8](#Esercizio_8)
- [Esercizio 9](#Esercizio_9)
- [Esercizio 10](#Esercizio_10)
- [Esercizio 11](#Esercizio_11)
- [Esercizio 12](#Esercizio_12)

## Esercizio 1
Dato un foglio largo 8.5 pollici e alto 11, convertire e stampare le caratteristiche precedenti in millimetri, insieme al suo perimetro e alla diagonale.
Consiglio: 1 pollice corrisponde a 2.54 cm. Nel calcolo della diagonale tornerà utile utilizzare il metodo sqrt() della classe Math.
```java
package Main;

public class Main {

    public static void main(String[] args)  {
        double height = 11 * 25.4f;
        double width = 8.5f * 25.4f;
        double diagonal = (Math.sqrt(height*height+width*width));
        System.out.printf("Perimeter: %5.2f \n" , ((height+width)*2));
        System.out.printf("Diagonal: %5.2f" , diagonal);
    }
}
```

## Esercizio 2
Dato un valore fornito in input dall’utente, stampare in output il risultato ottenuto dopo averlo elevato alla seconda, alla terza e alla quarta.
Consiglio: utilizzare il metodo pow() della classe Math. Il numero inserito dall’utente potrà contenere una parte decimale.
```java
package Main;
import java.util.Scanner;


public class Main {

    public static void main(String[] args)  {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a value:");
        double value = scan.nextDouble();
        for (int i = 0;i <4;i++){ value = Math.pow(value,i+1); }
        System.out.printf("Value: %5.2f", value);
    }
}
```

## Esercizio 3
Dati due valori interi forniti in input dall’utente, calcolare e stampare la loro somma, differenza, prodotto, media, distanza, valore massimo e minimo.
Consiglio: i metodi abs(), max() e min() della classe Math torneranno utili per calcolare rispettivamente la distanza, il valore massimo e quello minimo.
```java
package Main;
import java.util.Scanner;


public class Main {

    public static void main(String[] args)  {
        Scanner scan = new Scanner(System.in);
        System.out.print("Inserisci il primo valore:");
        int value1 = scan.nextInt();
        System.out.print("Inserisci il secondo valore:");
        int value2 = scan.nextInt();
        int max = Math.max(value1, value2);
        int min = Math.min(value1, value2);
        System.out.println("Sum: " +  (value1+value2));
        System.out.println("Difference: " + (max-min));
        System.out.println("Product: " + (value1*value2));
        System.out.println("Average: " + ((value1+value2)/2));
        System.out.println("Distance: " + (Math.abs(max-min)));
        System.out.println("Max value: " + max);
        System.out.println("Min value: " + min);
    }
}
```

## Esercizio 4
Modificare l’esercizio precedente in modo tale che tutte le operazioni il cui risultato è contenuto in un intero siano mostrate in al più 8 cifre. L’unica eccezione sarà quindi la media, il cui risultato sarà formattato a video in modo tale da essere mostrato in al più 11 cifre, di cui 2 dedicati alla parte decimale.
```java
package Main;
import java.util.Scanner;


public class Main {

    public static void main(String[] args)  {
        Scanner scan = new Scanner(System.in);
        System.out.print("Inserisci il primo valore:");
        int value1 = scan.nextInt();
        System.out.print("Inserisci il secondo valore:");
        int value2 = scan.nextInt();
        int max = Math.max(value1, value2);
        int min = Math.min(value1, value2);
        System.out.printf("Sum: %8d\n", (value1+value2));
        System.out.printf("Difference: %8d\n", (max-min));
        System.out.printf("Product: %8d\n", (value1*value2));
        double average = (value1 + value2) / 2.0;
        System.out.printf("Average:    %11.2f\n", average);
        System.out.printf("Distance: %8d\n", (Math.abs(max-min)));
        System.out.printf("Max value: %8d\n", max);
        System.out.printf("Min value: %8d\n", min);
    }
}
```

## Esercizio 5
Dato un valore in input fornito dall’utente che rappresenta una distanza in metri, stampare la sua conversione in miglia, piedi e pollici.
```java
package Main;
import java.util.Scanner;

public class Main {

    public static void main(String[] args)  {
        Scanner scan = new Scanner(System.in);
        System.out.print("Inserisci il primo valore:");
        double value = scan.nextDouble();
        System.out.printf("Miles: %.2f\n", (value/1609.344));
        System.out.printf("Feet: %.2f\n", (value*3.28084));
        System.out.printf("Inches: %.2f\n", (value*39.3701));
    }
}
```

## Esercizio 6
Dato un valore in input fornito dall’utente indicante il raggio di un cerchio, calcolarne l’area, la circonferenza e, successivamente, il volume e la superficie della sfera ottenuta dalla figura precedente, stampando i risultati a video.
Consiglio: non sarà necessario definire un proprio pi greco. Infatti, la classe Math contiene al suo interno la costante statica PI, utile allo scopo dell’esercizio.
```java
package Main;
import java.util.Scanner;

public class Main {

    public static void main(String[] args)  {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the radius:");
        double radius = scan.nextDouble();

        System.out.printf("Area: %.2f\n", (Math.PI*(Math.pow(radius,2))));
        System.out.printf("Circumference: %.2f\n", (2 * Math.PI * radius));
        System.out.printf("Volume: %.2f\n", ((4/3) * Math.PI * Math.pow(radius,3)));
        System.out.printf("Surface: %.2f", (4 * Math.PI * Math.pow(radius,2)));
    }
}
```

## Esercizio 7
Dati due valori forniti in input dall’utente che rappresentano la base e l’altezza di un rettangolo, calcolare e stampare a video l’area, il perimetro e la lunghezza della sua diagonale.
```java
package Main;
import java.util.Scanner;

public class Main {

    public static void main(String[] args)  {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the base:");
        double base = scan.nextDouble();
        System.out.print("Enter the height:");
        double height = scan.nextDouble();

        System.out.printf("Area: %.2f\n", (base*height));
        System.out.printf("Perimeter: %.2f\n", ((base+height)*2));
        System.out.printf("Diagonal: %.2f\n", (Math.sqrt(height*height+base*base)));
    }
}
```

## Esercizio 8
Un distributore automatico accetta solamente penny e centesimi e fornisce il resto in dollari. Come assunzione, si ha che un dollaro corrisponde a 100 penny, quindi un quarto di dollaro varrà 25 penny.
Creare un distributore automatico che abbia il seguente funzionamento:
- L’utente dovrà indicare il taglio delle banconote fornite nel resto. Per semplicità, i tagli disponibili sono di 1, 5 e 10 dollari
- L’utente dovrà indicare il taglio delle monete fornite nel resto. In questo caso, corrisponderanno sempre ad un quarto di dollaro (1 = $.25, 2 = $.50, 4 = $1)
- L’utente dovrà quindi inserire il prezzo del prodotto scelto, di tipo intero, in penny. Il distributore convertirà tale valore in dollari, stampando a video il resto fornito
```java
package Main;
import java.util.Scanner;

public class Main {

    public static void main(String[] args)  {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter bill value (1 = $1 , 5 = $5 ,10 = $10 ): ");
        int value = scan.nextInt();
        System.out.print("Enter quarter value (1 = $.25, 2 = $.50, 4 = $1): ");
        int quarterValue = scan.nextInt();
        System.out.print("Enter item price in pennies:");
        int price = scan.nextInt();
        int amount = 100 * value + 25 * quarterValue - price;
        System.out.printf("Amount due (in pennies): %d\n", amount);
        System.out.printf("Dollar: %d\n", (amount / 100));
        System.out.printf("Quarters: %d\n",((amount%100) / 25));
    }
}
```

## Esercizio 9
Creare un programma che stampi a video il costo totale del carburante per un viaggio in auto di 100 miglia e il numero di miglia massime percorribili con il serbatoio attuale. Per ottenere quanto richiesto, l’utente dovrà fornire in input:
- I litri attuali nel serbatoio
- L’efficienza dell’auto (km/litro) 
- Il prezzo del carburante per litro
```java
package Main;
import java.util.Scanner;

public class Main {

    public static void main(String[] args)  {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter current liters in the tank: ");
        double litersInTank = scan.nextDouble();
        System.out.print("Enter car's efficiency (km/liter): ");
        double carEfficiency = scan.nextDouble();
        System.out.print("Enter the price of fuel per liter: $");
        double fuelPrice = scan.nextDouble();
        double milesPerTank = litersInTank * carEfficiency;
        double fuelCost = 100/carEfficiency*fuelPrice;
        System.out.println("Maximum number of miles that can be traveled: " + (int)milesPerTank + " miles");
        System.out.printf("Total cost of fuel for a 100-mile trip: $%.2f", fuelCost);
    }
}
```

## Esercizio 10
Creare una classe Menu che rappresenti un menù utente con la seguente struttura:  Attributi:
- labels: costante stringa statica, conterrà tutte le lettere dell’alfabeto  menuText:stringa,rappresenteràlevocidelmenù
- optionCount:intero,rappresenteràilnumerodivocinelmenù
- Costruttore:dovràvalorizzaregliattributimenuTexteoptionCountrispettivamentea stringa vuota e 0
Metodi:
- display():stampailcontenutotestualedelmenù
- addOption(Stringopzione):aggiungeunavocealmenù.Lalettera
identificativa della nuova voce sarà quella in posizione optionLabel. Una volta ottenuta, l’aggiunta della voce al testo corrente, rappresentato dall’attributo menuText, dovrà essere fatta secondo il seguente schema: {menuText}
{LetteraDellaNuovaVoce}) {opzione}
Ai fini di esempio viene fornita un’esecuzione di questa chiamata:
addOption(“pippo”): LetteraDellaNuovaVoce = “C”
menuText = 
“A) Voce Uno
B) Voce Due
C) pippo”
Ai fini di test, creare una classe MenuDemo che utilizzi la classe Menu aggiungendo varie voci per poi visualizzarle.
```java
package Main;
class Menu {
    final String labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    String menuText;
    int optionCount;
    public Menu(){
        optionCount = 0;
        menuText = "";
    }
    public void Display(){System.out.println("MENÙ:\n" + menuText);}
    public void AddOption(String opzione){
        String optionLabel = labels.substring(optionCount, optionCount + 1);
        menuText = menuText + optionLabel + ") " + opzione + "\n";
        optionCount++;
    }

}
public class Main {

    public static void main(String[] args)  {
        Menu mainMenu = new Menu();
        mainMenu.AddOption("Open new account");
        mainMenu.AddOption("Log into existing account");
        mainMenu.AddOption("Help");
        mainMenu.AddOption("Quit");
        mainMenu.Display();
    }
}
```

## Esercizio 11
Scrivere un programma che componga il percorso di un file dati i diversi elementi forniti dall’utente. A tale scopo, all’utente verrà richiesto di:
- Inserire la lettera del drive in un cui salvare il file
- Inserire il percorso all’interno del driv eche porti alla cartella desiderata
- Inserire il nome del file
- Inserire l’estensione del file
Come risultato, il programma dovrà stampare il percorso completo del file, ottenuto tramite la concatenazione degli elementi precedenti.
```java
package Main;
import java.util.Scanner;

public class Main {

    public static void main(String[] args)  {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the drive letter: ");
        String letter = scan.nextLine();
        System.out.print("Enter the path: ");
        String path = scan.nextLine();
        System.out.print("Enter the file name: ");
        String fileName = scan.nextLine();
        System.out.print("Enter the file extension: ");
        String extensionFile = scan.nextLine();
        System.out.printf("%s:%s//%s.%s", letter, path, fileName, extensionFile);
    }
}
```

## Esercizio 12
Creare un programma che legga una stringa fornita in input dall’utente che rappresenti un numero tra 1000 e 999999 in cui le migliaia sono separate da una virgola (es: 1,000 ; 23,456 ; 656,759). Successivamente, stampare il prefisso ed il postfisso di tale numero, definiti rispettivamente come la parte prima e dopo la virgola.
Consiglio: guardare il metodo substring() della classe String.
Esempio: inserendo la stringa 656,759, il programma stamperà in output 656759.
```java
package Main;
import java.util.Scanner;

public class Main {

    public static void main(String[] args)  {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a number with a comma: ");
        String NumberWithComma = scan.nextLine();
        System.out.println(NumberWithComma.substring(0, NumberWithComma.indexOf(","))+ NumberWithComma.substring(NumberWithComma.indexOf(",")+1));
    }
}
```