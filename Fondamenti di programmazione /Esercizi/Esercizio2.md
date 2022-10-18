<p align="center">
  <h2 align="center">Esercizio 12 Ottobre 2022</h2>
  <p align="center">I miei esercizi di Python!</p>
</p>

## Sommario ➕
- [Stringhe📚](#Stringhe📚)
- [Liste✏️](#Liste✏️)

## Stringhe 📚

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

- 3)Scrivere una funzione che implenta la stessa funzionalità di `str.split()` rimuovendo uno dei caratteri presi in input. Non ritornare stringhe vuote.Usare solo costrutti del linguaggio e non librerie.
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

## Liste ✏️