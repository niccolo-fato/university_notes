<p align="center">
  <h2 align="center">Esercizio Capitolo 3 </h2>
  <p align="center">I miei esercizi di Java!</p>
</p>

## Sommario ➕

- [Esercizio 1](#Esercizio_1)
- [Esercizio 2](#Esercizio_2)
- [Esercizio 3](#Esercizio_3)
- [Esercizio 4](#Esercizio_4)


## Esercizio 1
Creare una classe Counter che rappresenti il funzionamento di un
contatore. Al suo interno sarà presente un campo privato, di tipo
intero, che memorizzi il suo valore attuale. Dal punto di vista delle
funzionalità, la classe conterrà:

    - Un metodo getValue che ritorni il valore attuale del contatore
	- Un metodo click che permetta l’incremento del campo di un’unità
	- Un metodo reset che reimposti il valore del campo a 0
	- Un metodo undo che annulli l’ultima esecuzione di click, evitando
che il valore del campo non scenda sotto allo zero.
La classe CounterTester dovrà:

	- Creare un oggetto di tipo Counter
	- Incrementare il contatore di tre unità
	- Stampare il suo valore
	- Decrementare il contatore di un’unità
	- Stampare il suo valore, controllando che sia pari a due
	- Decrementare il contatore di tre unità
	- Stampare il suo valore, controllando che sia pari a zero
Consiglio: la classe Math offre il metodo max() che può essere
utilizzato nella definizione di undo per evitare che il decremento porti
ad avere un numero negativo.
```java
package Main;
class Counter {
    private int value;
    public int GetValue(){ return value; }
    public void Click(){ value += 1; }
    public void Reset(){ value = 0; }
    public void Undo(){ value = Math.max(value -1,0); }
}
public class Main {

    public static void main(String[] args) {
        Counter OBJECT = new Counter();
        OBJECT.Click();
        OBJECT.Click();
        OBJECT.Click();
        OBJECT.GetValue();
        OBJECT.Undo();
        System.out.println("Il numero dev'essere uguale a 2: " + OBJECT.GetValue());
        OBJECT.Undo();
        OBJECT.Undo();
        OBJECT.Undo();
        System.out.println("Il numero dev'essere uguale a 0: " + OBJECT.GetValue());
    }
}
```

## Esercizio 2
Estendere l’esercizio precedente aggiungendo un ulteriore campo
privato e di tipo intero che rappresenti il valore massimo assumibile
dal contatore. Tale valore è impostabile esclusivamente tramite il
metodo setLimit, il quale accetta un parametro di tipo intero.
L’introduzione di questo limite modificherà il comportamento del
metodo click. Infatti, non sarà possibile incrementare ulteriormente il
contatore oltre il valore massimo.
La classe CounterTester riprende il comportamento di quella vista
nell’esercizio precedente. La differenza risiede nel fatto che il primo
metodo chiamato sarà setLimit, il quale dovrà impostare il valore
massimo del contatore a tre. L’efficacia di questo limite dovrà essere
accertata chiamando quattro volte di fila il metodo click e accertarsi
che il valore attuale del contatore sia pari a tre.
```java
package Main;
class Counter {
    private int value;
    private int max_value;
    public void Set_limit(int i){max_value = i;}
    public int GetValue(){ return value; }
    public void Click(){ value = Math.max(value -+1,max_value); }
    public void Reset(){ value = 0; }
    public void Undo(){ value = Math.max(value -1,0); }
}
public class Main {

    public static void main(String[] args) {
        Counter OBJECT = new Counter();
        OBJECT.Set_limit(3);
        OBJECT.Click();
        OBJECT.Click();
        OBJECT.Click();
        OBJECT.Click();
        System.out.println("Il numero dev'essere uguale a 3: " + OBJECT.GetValue());
        OBJECT.GetValue();
        OBJECT.Undo();
        System.out.println("Il numero dev'essere uguale a 2: " + OBJECT.GetValue());
        OBJECT.Undo();
        OBJECT.Undo();
        OBJECT.Undo();
        System.out.println("Il numero dev'essere uguale a 0: " + OBJECT.GetValue());
    }
}
```

## Esercizio 3
Creare una classe chiamata RangeInput che rappresenti un intervallo
numerico tra due numeri.
Attributi:

    - Min: di tipo intero, rappresenta il valore minimo dell’intervallo
    - Max: di tipo intero, rappresenta il valore massimo dell’intervallo
    - Current: di tipo intero, rappresenta il valore attuale all’interno
dell’intervallo.
Costruttore: ridefinito in modo tale che accetti due parametri che
rappresentano i due limiti dell’intervallo.
Metodi:

    - Up: incrementa di un’unità il valore attuale dell’intervallo,
    controllando che non superi il limite massimo
    - Down: decrementa di un’unità il valore attuale dell’intervallo,
    controllando che non superi il limite minimo
La classe RangeInputTester vedrà la creazione un oggetto di tipo
RangeInput valorizzando i due estremi dell’intervallo.
Successivamente, dovranno essere controllata la consistenza dei
suoi limiti chiamando più volte i metodi Up and Down a piacimento.
```java
package Main;
import java.util.Scanner;
class RangeInput {
   //Dichiaro gli attributi
   int min;
   int max;
   int current;
   //Costruttore
    public RangeInput(int input_min, int input_max,int input_current)
    {
        min = input_min;
        max = input_max;
        current = input_current;
    }
    public int getCurrent() {return current;}
    public void Up() {current = Math.min(current +1,max);}
    public void Down() {current = Math.max(current -1,min);}
}
public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int input_min;
        int input_max;
        int cont;
        System.out.print("Inserire il valore minimo dell'intervallo: ");
        input_min = scan.nextInt();
        do {System.out.print("Inserire il valore massimo dell'intervallo: ");
            input_max = scan.nextInt(); } while (input_max <= input_min);
        RangeInput OBJECT = new RangeInput(input_min, input_max,((input_min+input_max)/2));
        do {
            System.out.println("Il valore attuale è di " + OBJECT.getCurrent());
            System.out.println("\t\t MENU' SCELTA:");
            System.out.println("-Inserisci 1 per incrementare di 1 il valore dell'intervallo,\n" +
                    "-Inserisci 2 per decrementare di 1 il valore dell'intervallo,\n" +
                    "-Inserisci 0 se vuoi uscire dal programma,\n" +
                    "Scelta:");
            cont = scan.nextInt();
            switch (cont) {
                case 0 -> System.out.println("Hai deciso di uscire dal programma");
                case 1 -> OBJECT.Up();
                case 2 -> OBJECT.Down();
            }
        }while(cont !=0);
    }
}
```

## Esercizio 4
Creare una classe Circuit che gestisca l’illuminazione di un corridoio.
Attributi: tutti e tre private

    - firstSwitch: può assumere due valori: 1 o 0, che rappresentano
    rispettivamente il selezionamento o meno della prima lampada
    - secondSwitch: come firstSwitch, ma riferita alla seconda
    lampada
    - lampState: rappresenta lo presenza o meno di corrente,
    valorizzata con i valori 0 o 1 analogamente agli attributi precedenti
Metodi:

    - getFirstSwitchState: ritorna il valore di firstSwitch
    - getSecondSwitchState: ritorna il valore di secondSwitch
    - getLampState: ritorna il valore di lampState
    - toggleFirstSwitch: cambia lo stato di firstSwitch e lampState da
     0 a 1 e viceversa
    - toggleSecondSwitch: cambia lo stato di secondSwitch e
    lampState da 0 a 1 e viceversa
La classe CircuitTester dovrà essere costruita accertandosi che
l’esecuzione consecutiva dello stesso toggleSwitch riporti lo stato
dello switch corrispondente e della lampada a zero. Per controllare il
contenuto dei diversi attributi durante i test, stampare il valore
ritornato dai metodi get.
```java
package Main;
import java.util.Scanner;
class Circuit {
    private boolean firstSwitch = false; //true=1, false=0
    private boolean secondSwitch = false; //true=1, false=0
    private boolean lampState = false; //true=1, false=0
    public boolean GetFirstSwitchState(){return firstSwitch;}
    public boolean GetSecondSwitchState(){return secondSwitch;}
    public boolean GetLampState(){return lampState;}
    public void ToggleFirstSwitch(){
        firstSwitch = !firstSwitch;
        lampState = !lampState;
    }
    public void ToggleSecondSwitch(){
        secondSwitch = !secondSwitch;
        lampState = !lampState;
    }
}
public class Main {

    public static void main(String[] args) {
        Circuit OBJECT = new Circuit();

        OBJECT.ToggleFirstSwitch();
        OBJECT.ToggleFirstSwitch();
        OBJECT.ToggleSecondSwitch();
        System.out.println("Switch 1: " + OBJECT.GetFirstSwitchState());
        System.out.println("Switch 2: " + OBJECT.GetSecondSwitchState());
        System.out.println("Lamp: " + OBJECT.GetLampState());

        OBJECT.ToggleSecondSwitch();
        System.out.println("Switch 1: " + OBJECT.GetFirstSwitchState());
        System.out.println("Switch 2: " + OBJECT.GetSecondSwitchState());
        System.out.println("Lamp: " + OBJECT.GetLampState());

    }
}
```