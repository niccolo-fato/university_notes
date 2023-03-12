<p align="center">
  <h2 align="center">Esercizio Capitolo 3 </h2>
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
- [Esercizio 13](#Esercizio_13)
- [Esercizio 14](#Esercizio_14)
- [Esercizio 15](#Esercizio_15)
- [Esercizio 16](#Esercizio_16)
- [Esercizio 17](#Esercizio_17)
- [Esercizio 18](#Esercizio_18)
- [Esercizio 19](#Esercizio_19)
- [Esercizio 20](#Esercizio_20)

## Esercizio 1
Sostituire, all’interno della stringa Mississippi, le occorrenze di i con ii e le occorrenze di ss con
s.
Consiglio: utilizzare la funzione replace() all’interno della classe String.
```java
package Main;
public class Main {

    public static void main(String[] args) {
       String WORD = "Mississippi";
       System.out.println(WORD.replace("i","ii").replace("ss","s"));
    }
}
```

## Esercizio 2
Data una stringa contenente uno o più spazi consecutivi, rimuovere inizialmente le eventuali loro occorrenze che si trovano in testa e/o in coda. Successivamente, eliminare tutti gli spazi interni.La stringa nale dovrà essere una giustapposizione di caratteri alfanumerici, senza spazi.
Consiglio: utilizzare la funzione trim() per eliminare gli spazi in testa e in coda, replace() per sostituire i singoli spazi con una stringa vuota.
```java
package Main;
public class Main {

    public static void main(String[] args) {
        String str = "    Hello World     !    ";
        str = str.replaceAll("\\s", "");
        System.out.println(str);
    }
}
```

## Esercizio 3
Creare un oggetto di tipo Rectangle e calcolarne l’area.
Consiglio: importare la classe Rectangle ( java.awt.Rectangle) per creare un oggetto di questo tipo. Utilizzare i metodi getWidth() e getHeight() per ottenere rispettivamente la base e l’altezza ai ni del calcolo dell’area.
```java
package Main;
import java.awt.Rectangle;
public class Main {

    public static void main(String[] args) {
       Rectangle OBJECT = new Rectangle(20,10);
        System.out.println("Width: " + OBJECT.getWidth());
        System.out.println("Height: " + OBJECT.getHeight());
    }
}
```

## Esercizio 4
Creare un oggetto di tipo Rectangle e calcolarne il perimetro.
Consiglio: guardare l’esercizio precedente.
```java
package Main;
import java.awt.Rectangle;
public class Main {

    public static void main(String[] args) {
       Rectangle OBJECT = new Rectangle(20,10);
        System.out.println("Width: " + OBJECT.getWidth());
        System.out.println("Height: " + OBJECT.getHeight());
        System.out.println("Perimeter: " +(OBJECT.getWidth()+OBJECT.getHeight())*2 );
    }
}
```

## Esercizio 5
Creare due oggetti di tipo Rectangle, rispettivamente con un’area ed un perimetro pari a 42.
Per ciascuno di questi due oggetti, stampare la base e l’altezza.
Consiglio: guardare l’esercizio 3, facendo attenzione a quali valori passare al costruttore di Rectangle per ottenere quanto richiesto.
```java
package Main;
import java.awt.Rectangle;
public class Main {

    public static void main(String[] args) {
        Rectangle REC_1 = new Rectangle(2,21);
        Rectangle REC_2 = new Rectangle(7,14);
        System.out.println("Area: " +(REC_1.getWidth()*REC_1.getHeight()) );
        System.out.println("Perimeter: " +(REC_2.getWidth()+REC_2.getHeight())*2 );
    }
}
```

## Esercizio 6
Creare un oggetto di tipo Rectangle con un’origine che sia diversa dal punto (0,0). Successivamente, modicarla in (0,0) e stampare le coordinate x e y dell’origine prima della modifica, la nuova base e la nuova altezza.
Consiglio: all’interno della classe Rectangle, utilizzare il metodo add() per cambiare l’origine di un rettangolo, capendo come esso modichi base, altezza e coordinate dell’oggetto. Utilizzare inoltre i metodi getX() e getY() per conoscere rispettivamente le coordinate X e Y dell’oggetto.
```java
package Main;
import java.awt.Rectangle;
public class Main {

    public static void main(String[] args) {
        Rectangle OBJECT = new Rectangle(3,5,2,21);
        OBJECT.add(0,0);
        System.out.println("New x: " + OBJECT.getX() );
        System.out.println("New y: " + OBJECT.getY() );
        System.out.println("Width: " + OBJECT.getWidth());
        System.out.println("Height: " + OBJECT.getHeight());
    }
}
```

## Esercizio 7
Data la stringa Mississippi, sostituire le occorrenze di i con ! e le s con $. Stampare a video il risultato nale e accertarsi che esso corrisponda alla stringa "M!$$!$$!pp!" (senza le virgolette).
Consiglio: utilizzare il metodo replace() per sostituire le occorrenze di i e s.
```java
package Main;

public class Main {

    public static void main(String[] args) {
        String WORD = "Mississippi";
        System.out.println(WORD.replace("s","$").replace("i","!"));
    }
}
```

## Esercizio 8
Data la stringa Hello, World!, sostituire le occorrenze di e con % e le o con le e, le % con le o, seguendo questo ordine. Stampare a video il risultato, accertandosi che coincida con la stringa Holle, Werld!
Consiglio: utilizzare il metodo replace() per sostituire le occorrenze di e e o.
```java
package Main;

public class Main {

    public static void main(String[] args) {
        String WORD = "Hello, World!";
        System.out.println(WORD.replace("e","%").replace("o","e").replace("%","o"));
    }
}
```

## Esercizio 9
Data la stringa desserts, capovolgerla al ne di ottenere stressed.
Consiglio: utilizzare la classe StringBuilder con cui costruire la stringa come nell’esempio.
Utilizzare il metodo reverse() per capovolgerla.
```java
package Main;

public class Main {

    public static void main(String[] args) {
        StringBuilder OBJECT = new StringBuilder("desserts");
        OBJECT.reverse();
        System.out.println(OBJECT);
    }
}
```

## Esercizio 10
Dato un oggetto di tipo Color, schiarirlo e stampare i nuovi valori RGB.
Consiglio: import java.awt.Color per la classe Color. Utilizzare il metodo brighter() per modificare i valori RGB al ne di schiarire il colore. Successivamente, utilizzare getRed(), getGreen(), getBlue() per ottenere i valori aggiornati.
```java
package Main;
import java.awt.Color;

public class Main {

    public static void main(String[] args) {
        Color RGB = new Color(255,10,50);
        Color RGB_brighter = RGB.brighter();

        System.out.println(RGB_brighter.getRed());
        System.out.println(RGB_brighter.getGreen());
        System.out.println(RGB_brighter.getBlue());
    }
}
```

## Esercizio 11
Creare un oggetto di tipo Color, schiarirlo, e creare una nestra 200x200 px che abbia questo nuovo colore come sfondo.
Consiglio: in aggiunta all’esercizio precedente, utilizzare il framework Swing nella sua totalità( import javax.swing.*) al ne di poter avere accesso alla classe JFrame. Essa sarà necessaria per poter creare una nestra la cui dimensione sarà impostata tramite il metodo setSize(). I metodi getContentPane() e setBackground() saranno necessari, rispettivamente, ad ottenere il controllo del pannello di contenimento della nestra e per impostare il nuovo colore come sfondo. Per orire la possibilità all’utente di poter chiudere la nestra, sarà necessario l’utilizzo del metodo setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE). Una volta applicate tutte le modiche, il metodo setVisibile(true) farà in modo che l’oggetto di tipo JFrame sia visibile all’utente.
```java
package Main;
import java.awt.Color;
import javax.swing.*;

public class Main {

    public static void main(String[] args) {
        Color RGB = new Color(255,10,50);
        Color RGB_brighter = RGB.brighter();

        System.out.println(RGB_brighter.getRed());
        System.out.println(RGB_brighter.getGreen());
        System.out.println(RGB_brighter.getBlue());
        JFrame FRAME = new JFrame();
        FRAME.setSize(200,200);
        FRAME.getContentPane().setBackground(RGB_brighter);
        FRAME.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        FRAME.setVisible(true);
    }
}
```

## Esercizio 12
Creare un oggetto di tipo Color e rendere più scuro solo il colore Rosso. Successivamente, riapplicare la medesima operazione allo stesso oggetto, coinvolgendo tutti e tre i parametri RGB e stampando a video i loro valori nali.
Consiglio: l’attributo RED della classe Color ore la possibilità di manipolare il parametro R, che rappresenta il colore rosso. Il metodo darker() sarà necessario al ne di poter rendere più scuro il colore rosso e, successivamente, l’oggetto di tipo Color nella sua totalità. Ai fini della stampa a video, getRed(), getGreen() e getBlue() serviranno per estrapolare dall’oggetto i 3 parametri aggiornati.
```java
package Main;
import java.awt.Color;


public class Main {

    public static void main(String[] args) {
        Color RED = Color.RED.darker();
        Color RGB = RED.darker();

        System.out.println(RGB.getRed());
        System.out.println(RGB.getGreen());
        System.out.println(RGB.getBlue());
    }
}
```

## Esercizio 13
Creare un programma che simuli il lancio di un dado a 6 facce.
Consiglio: importare java.util.Random per poter utilizzare la classe Random. Essa conterrà il metodo nextInt() che dovrà essere utilizzato per simulare l’estrazione casuale di numero tra 0 e 5.
```java
package Main;
import java.util.Random;

public class Main {

    public static void main(String[] args) {
       Random DADO = new Random();
        System.out.println(DADO.nextFloat(0, 6));
    }
}
```

## Esercizio 14
Creare un programma che generi un prezzo casuale di un prodotto nella forma xx.cc.
Consiglio: le istruzioni necessarie sono le stesse dell’esercizio 13. Per far sì che il prezzo venga stampato con al massimo due decimali, nella System.out.printf() dovrà essere utilizzato il formattatore %.2f. Esso servirà per visualizzare il prezzo con due cifre decimali.
```java
package Main;
import java.util.Random;

public class Main {

    public static void main(String[] args) {
        Random DADO = new Random();
        float a = DADO.nextFloat()*99;
        System.out.printf("Prezzo: $%.2f",a);

    }
}
```

## Esercizio 15
Calcolare la distanza tra due punti.
Consiglio: package java.awt.Point per creare i due oggetti di tipo Point, gestendo correttamente il suo costruttore per fornire le coordinate x e y. Il metodo distance(), presente al suo interno, servirà a calcolare la distanza tra i due punti.
```java
package Main;
import java.awt.Point;

public class Main {

    public static void main(String[] args) {
        Point POINT_1 = new Point(5,10);
        Point POINT_2 = new Point(-5,-10);
        System.out.println("Point distance: " + POINT_1.distance(POINT_2));
    }
}
```

## Esercizio 16
Creare un oggetto appartenente alla classe Day e valorizzarlo con giorno, mese e anno tramite il suo costruttore. Successivamente, creare un secondo oggetto di tipo Day, la cui data sarà a 10 giorni di distanza dalla precedente. Una volta che i due oggetti sono stati creati, calcolare la
loro distanza in giorni e stamparla a video, accertandosi che il valore restituito sia pari a 10.
Consiglio: l’esercizio fornisce una una classe Day che ne faciliterà la risoluzione grazie alla presenza:
- di un costruttore che accetta un giorno, un mese e un anno
- dei metodi addDays() e daysFrom() per eettuare il calcolo della distanza tra date.
```java
package Main;
import java.time.LocalDate;

class Day{
    private LocalDate date;

    public Day(int day, int month, int year) { this.date = LocalDate.of(year, month, day);}
    public void AddDays(int days) { this.date = this.date.plusDays(days); }
    public LocalDate GetDate(){ return date;}
    public long Difference(Day other) { return Math.abs(this.date.toEpochDay() - other.date.toEpochDay()); }

}

public class Main {

    public static void main(String[] args) {
        Day DAY_1 = new Day(12,03,2023);
        Day DAY_2 = new Day(22,03,2023);
        System.out.println(DAY_2.Difference(DAY_1));
    }
}
```


