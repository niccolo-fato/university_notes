<p align="center">
  <h2 align="center">Esercizio 12 Ottobre 2022</h2>
  <p align="center">I miei esercizi di Python!</p>
</p>

## Sommario ➕
- [Stringhe](#Stringhe)
- [Liste](#Liste)

## Stringhe

- 1)Scrivere una funzione che ritorna una stringa di saluto formata da `Ciao `, seguito dal nome come parametro, e poi da `Buona giornata!`
```python
def make_hello(name: str) -> str:
    return 'Ciao {}, Buona giornata!'.format(name)

name = (input("Inserisci il nome:"))
print(make_hello(name))
```

- 2)Scrivere una funzione che implenta la stessa funzionalità di `str.strip()`che rimuove spazi all'inizio e alla fine della stringa. Usare solo costrutti del linguaggio e non librerie.
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

- 3)Scrivere una funzione che implementa la stessa funzionalità di `str.split()` rimuovendo uno dei caratteri presi in input. Non ritornare stringhe vuote.Usare solo costrutti del linguaggio e non librerie.
```python
def split_string(string: str, characters: str = ''):
    split_list = []
    tmp = ''
    for x in string:
        if x == ' ':
            split_list.append(tmp)
            tmp = ''
        else:
            tmp += x
    if tmp:
        split_list.append(tmp)
    return split_list
string = 'Ciao sono Niccolò'
characters = 0
print(split_string(string))
```

- 4)Scrivere una funziona che si comporta come `str.replace()`.Usare solo costrutti del linguaggio e non librerie.
```python
def replace_substring(string: str, find: str, replace: str) -> str:
    count = 0
    r = ""
    tmp = ""
    for x in string:
        if x == find[count]:
            tmp += x
            count += 1
        else:
            r += tmp +(x)
            tmp = ""
            count = 0
        if count == len(find):
            r += replace
    return r
string = "Ciao Andrea"
find= "Andrea"
replace ="Luca"
print(replace_substring(string,find,replace))
```

- 5)Scrivere una funzione che codifica un messaggio con il cifrario di Cesare, che sostituisce ad ogni carattere il carattere che si trova ad un certo offset nell'alfabeto. Quando si applica l'offset,si riparte dall'inizio se necessario (pensate a cosa fa il modulo).La funzione permette anche di decrittare un messaggio applicando l'offset in negativo. Si può assumere che il testo è minuscolo e fatto delle sole lettere dell'alfabeto inglese e spazi che non sono crittati.Suggerimento: Sono utili le funzioni `ord()` e `chr()`.
```python
def caesar_cypher(string: str, offset: int,) -> str:
    r = ""
    for x in string:
        if x != ' ':
            index = ord(x) - ord('a')
            offsetted = (index + offset) % 26
            r += chr(ord('a') + offsetted)
        else:
            r += " "
    return r
string = "ciao Cesare"
offset = 17
print(caesar_cypher(string, offset))
```

- 6)Scrivere una funzione che controlla la validita' di una password.La password deve avere:
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
## Liste

- 1)Scrivere una funzione che somma i quadrati degli elementi di una lista.
```python
def sum_squares(List) -> int:
    return sum(map(lambda x: x ** 2, List))
List = [2, 3, 4, 5]
print(sum_squares(List))
```

- 2)Scrivere una funzione che ritorna il valore massimo degli elementi di una lista.
```python
def max_element(List) -> int:
    return max(List)
List = [2, 10, 9, 5]
print("Il numero più grande della lista è {}".format(max_element(List)))
```

- 3)Scrivere una funzione che rimuove i duplicati da una lista.Commentare sul tempo di esecuzione.
```python
def max_element(List) -> int:
    return list(dict.fromkeys(List))
List = [2, 10, 2, 9, 5, 9]
print((max_element(List)))
```

- 4)Scrivere una funzione che si comporta come `reverse()`.Usare solo costrutti del linguaggio e non librerie.
```python
def reverse_list(elements: list) -> list:
    return elements[::-1]
list = [2, 10, 2, 9, 5, 9]
print((reverse_list(list)))
```

- 5)Scrivere una funzione `flatten_list()` che prende una lista che contiene elementi o altre liste, e ritorna una lista contenente tutti gli elementi. Si può assumere che le liste contenute non contengono altre liste. Usare la funzione `isinstance()` per determinare se un elemento è una lista. Usare solo costrutti del linguaggio e non librerie.
```python
def flatten_list(elements: list) -> list:
    flatten_list = []
    for x in elements:
        flatten_list.append(x)
    return flatten_list
list = [2, 10, 2, 9, 5, 9], [2, 1, 4, 0, 5, 7]
print((flatten_list(list)))
```

