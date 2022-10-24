<p align="center">
  <h2 align="center">Esercizio 19 Ottobre 2022</h2>
  <p align="center">I miei esercizi di Python!</p>
</p>

## Esercizi 📚

- 1)Scrivere una funzione che controlla la validita' di una password.La password deve avere:
- Almeno una lettera fra [a-z] e una lettera fra [A-Z]
- Almeno un numero fra [0-9]
- Almeno un carattere fra [$#@]
- Essere lunga almeno 6 caratteri 
- Essere lunga non piu' di 16 caratteri
- La password non è valida se contiene caratteri diversi da quelli specificati sopra o se viola una delle regole specificate.
La funzione restituisce true/false a seconda se la password sia valida o meno.
```python
import re
def check_pwd(pwd: str) -> bool:
    bool = True
    control = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$])[A-Za-z\d@#$]{6,16}$"
    r = re.search(control, pwd)
    if r:
        bool = True
    else:
        bool = False
    return bool
pwd = 'Nick90@#'
result = check_pwd(pwd)
if result == False:
    print("La password non è valida")
else:
    print("La password è valida")
```

- 2)Scrivere una funzione che data una tupla (x, y, z) restituisca la tupla (z+1, x-1, y+2)
```python
def tuple_ex(t: tuple) -> tuple:
    t2 = ()
    tmp = 0
    for x in t:
        tmp = int(input("Inserire un numero da aggiungere o sottrarre al numero {} della tupla:".format(x)))
        t2 = t2 + (tmp,)
    return tuple(map(lambda i, j: i + j, t, t2))
t = (5, 3, 4)
print(tuple_ex(t))
```

- 3)Scrivere una funzione che calcola l'intersezione fra due liste.Date due liste, deve restituire una nuova lista contenente solo gli elementi presenti in entrambe le liste.
```python
def intersect(list1: list, list2: list) -> list:
    result = []
    for x in list1:
        if x in list2:
           result += [x]
    return result
list1 = [2, 3]
list2 = [1, 2, 3]
print(intersect(list1, list2))
```

- 4)Scrivere una funzione che data una lista contenente valori >= 0,crei una nuova lista contentente soltanto gli elementi della lista originale tali che soddisfano la seguente proprietà:
-lista[i] > 2*media(lista[0:i])
-(Il primo elemento non viene quindi mai inserito)
Ad esempio, si consideri la lista [5, 3, 10, 0]
Il primo elemento è 5. Non viene inserito
Il secondo elemento è 3, e la media degli elementi nel range [0, 0] è 5. Poichè 3 < 5*2, l'elemento non viene inserito nella nuova lista;
Il terzo elemento è 10, e la media degli elementi nel range [0, 1] è 4. Poichè 10 > 4*2, l'elemento viene inserito nella nuova lista;
Il quarto elemento è 0, e la media degli elementi nel range [0, 2] è 6. Poichè 0 < 6*2, l'elemento non viene inserito nella nuova lista.
```python
def remove_avg(a: list) -> list:
    result = []
    y = 0
    for x in range(1, len(a)):
        average = a[x] >= (a[x] + a[y]) / 2
        if average == True:
            result += [a[x]]
    return result
List1 = (5, 3, 10, 0)
print(remove_avg(List1))
```

- 5)Data una lista di interi (ciascun intero è compreso fra 0 e 99), scrivere una funzione che restituisca una lista di tuple (x, y),dove x è un intero, e y è il numero di volte che questo intero appare nella lista originale. La lista di tuple deve essere ordinata in base al primo elemento.
Ad esempio, per l'input [5, 4, 1, 4], restituisce la lista [(1, 1), (4, 2), (5, 1)](ordinata in base al primo elemento perché 1 < 4 < 5)
```python
def frequency(a: list) -> list:
    a.sort()
    list1 = []
    for x in a:
        count = a.count(x)
        list1.append((x, count))
    return list(dict.fromkeys(list1))
a = [5, 4, 1, 4]
print(frequency(a))
```


