<p align="center">
  <h2 align="center">Esercizio 12 Ottobre 2022</h2>
  <p align="center">I miei esercizi di Python!</p>
</p>

## Esercizi 📚

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

- 4)