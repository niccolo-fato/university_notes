<p align="center">
  <h2 align="center">Esercizio 5 Ottobre 2022</h2>
  <p align="center">I miei esercizi di Python!</p>
</p>

## Sommario ➕

- [Errore](#Errore)
- [Calcoli](#Calcoli)
- [Stringhe](#Stringhe)
- [Funzioni](#Funzioni)

## Errore 🚫

Iniziate a prendere familiarità con i messaggi di errore che Python vi da. Provate ad introdurre di proposito degli errori e a vedere quale messaggio di errore ottenete. Meglio fare errori ora e di proposito (e capirli), piuttosto che accidentalmente in seguito e non riuscire a capire dov'è l'errore. Ad esempio:

- 1)Cosa succede se dimenticate gli apici alla fine di una stringa?
```html
Mi da un SyntaxError che va ad indicare che c’è un errore di sintassi nel programma, in questo caso l’errore sarà la mancanza di un apice e successivamente andrà a segnare dove si trova l’errore in questo modo:
              x = "ciao
                        ^
```

- 2)Cosa succede se dividete un numero per 0?
```html
Mi darà un ZeroDivisionError che si verifica quando proviamo a dividere un numero in virgola mobile per 0.
```

- 3)Cosa succede se in una istruzione di stampa (print) dimenticate una o entrambe le parentesi?
```html
Ridarà un SyntaxError dicendo qual'è il problema che in questo caso sarà “Missing parentheses in call to 'print'” e successivamente darà anche il modo in cui possiamo correggere il nostro errore che sarà “Did you mean print("ciao")?”
```

- 4)Per esprimere un numero negativo, si antepone il segno meno (ad esempio,-2 ). Cosa succede se anteponete ilsegno +? e se fate 2++2?
```html
Se mettiamo un + prima del numero ,quindi magari scrivendo +2+2, non succederà nulla, stessa cosa se proviamo a scrivere 2++2. 
```

- 5)Nella notazione matematica, possiamo omettere il simbolo di moltiplicazione. Ad esempio x*y può essere scritto come xy . E' permesso anche in Python?
```html
 Darà un SyntaxError dicendo che gli zeri iniziali nei valori decimali non sono consentiti. 
```

- 6)In Python possiamo assegnare un numero ad una variabile, ad esempio: n=42.Cosa succede se facciamo 42=n?
```html
No, non è permesso perché verrebbe preso come se fosse il nome di una variabile dando un NameError.
```

- 7)Cosa succede con x=y=1?
```html
Assegneremo il numero 1 sia alla variabile x che alla variabile y.
```

- 8)In alcuni linguaggi, come il C, ogni istruzione termina con un punto e virgola ( ; ). Cosa succede se mettiamo un punto e virgola alla fine di un'istruzione Python? E se mettiamo un punto?
```html
Mettendo il punto e virgola non succederà nulla mentre se mettiamo il punto darà errore.
```

## Calcoli 🧮

- 1)Scrivete una espressione che calcoli il numero di secondi che ci sono in 42 minuti e 42 secondi.
```python
x = (60*42/1)+42
print(x);
```

- 2)Scrivete una espressione che calcoli il numero di miglia che ci sono in 10 chilometri. (1 miglio = 1.61 km).
```python
x = 10/1.61
print(x);
```

- 3)Il volume di una sfera di raggio r è 4/3 * PI * r^3 . Scrivere una espressione che calcoli il volume di una sfera di raggio 5.
```python
Volume = 4*3.14*pow(5,3)/3 
print("Volume:",Volume)
```

- 4)Il prezzo di copertina di un libro è 24.95, ma una libreria ottiene il 40% di sconto. I costi di spedizione sono 3 euro per la prima copia, e 75 centesimi per ogni copia aggiuntiva. Qual'è il costo totale di 60 copie?
```python
libro = 24.95
sconto = int(input("Inserisci la percentuale di sconto:"))
sconto = libro-(libro*sconto/100)
print("costo libri con sconto: ",sconto)
costo_tot = 0
for x in range(60):
   if x == 0:
       costo_tot = costo_tot + (sconto+3)
   else:
       costo_tot = costo_tot + (sconto+0.75)
print("Il costo totale dei libri è :",costo_tot)
```

- 5)Se uscite di casa alle 6:52 di mattina e correte un miglio a ritmo blando (8 minuti e 15 secondi al miglio), e poi 3 miglia a ritmo moderato (7 minuti e 12 secondi al miglio), e infine un altro miglio a ritmo blando (9 minuti e 45 secondi al miglio), a che ora sarete tornati a casa?

```python
choice = 1
ora= 6
min= 52
sec = 0
while choice != 0:
   # ""Switch""
   print("""
   \t\t~Menù:~
   0-Exit,
   1-Per aumentare l'orario:
   """)
   choice = int(input("Choice:"))
   if choice != 1:
       print("ERROR==>Inserted option not available")

   else:
       ora2 = int(input("Inserire di quante ore aumentare:"))
       min2 = int(input("Inserire di quanti minuti aumentare:"))
       sec2 = int(input("Inserire di quanti secondi aumentare:"))
       miglia = int(input("Inserire miglia percorse:"))

       sec = sec + (sec2*miglia)
       if sec >= 60:
           sec = sec - 60
           min = min + 1
       min = min+ (min2*miglia)
       if min >= 60:
           min = min - 60
           ora = ora + 1
       ora = ora + (ora2*miglia)
       print("L'orario finale sarà: ",ora, " ore,",min," minuti,",sec," secondi."
```

## Stringhe 📫

- 1)Avete una stringa di 5 caratteri. Ogni carattere è una cifra decimale. Ad esempio, s="85721" . Stampate la somma delle cifre contenute nella stringa.
```python
s = str(input("Inserire una stringa di numeri decimali:"))
somma = 0
for x in range(len(s)):
   somma += int(s[x])
print("La somma dei numeri è:", somma)
```

- 2)Scrivete una espressione che a partire da una stringa di 5 caratteri, rappresentante un numero binario, stampi la sua rappresentazione decimale. Ad esempio, s="00101" -> 5 .
```python
s = str(input("Inserire un numero binario:"))[::-1]
somma = 0
potenza = 0
for x in range(len(s)):
   potenza = (int(s[x]))
   somma += (potenza*pow(2,x))
print("Il numero binario in decimale è:", somma)
```

-3)Avete una stringa di 5 caratteri. Il carattere centrale è il punto decimale ('.'). Ad esempio, s="52.29". Stampare il numero decimale rappresentato dalla stringa (stamparlo come numero, non come stringa).
```python
s = "52.29"
print(float(s))
```

## Funzioni ⏎

- 1)Scrivere una funzione che prende un numero in virgola mobile, ne calcola la radice cubica, e la ritorna.
```python
def cube_root(num) -> float:
   r = pow(num, 1 / 3)
   return r;
num = float(input("Inserire un numero:"))
print("La radice cubica di",num,"è ", cube_root(num))
```

- 2)Scrivere una funzione che prende come input cinque numeri e ritorna la somma dei numeri pari meno quella dei numeri dispari.
```python
def sum(num):
    sum_p = 0
    sum_d = 0
    r = 0
    for x in range(5):
        r =num[x] % 2
        print(r)
        if(r == 0):
            sum_p += num[x]
        else:
            sum_d += num[x]
    print(sum)
    return(sum_p-sum_d)
num = []
for x in range(5):
    num.insert(x, float(input("Inserisci un numero:")))
print(sum(num))
```

- 3)Scrivere una funzione che implenta la stessa funzionalità di str.strip()
```python
def strip_whitespace(string: str) -> str:
    ind, ind2 = 0, 0
    for i, j in enumerate(string):
        if j != ' ':
            ind = i
            break
    for i, j in enumerate(reversed(string)):
        if j != ' ':
            ind2 = i
            break
    return string[ind:len(string) - ind2]
string = "    Ciao sono Niccolò    "
print(strip_whitespace(string))
```
- 4)Scrivere una funzione che ritorna una stringa di saluto formata da Ciao , seguito dal nome letto come input e poi da Buona giornata!
```python
def make_hello(name: str) -> str:
    return 'Ciao {}, Buona giornata!'.format(name)

name = (input("Inserisci il nome:"))
print(make_hello(name))
```

