<p align="center">
  <h2 align="center">Esercizio 26 Ottobre 2022</h2>
  <p align="center">I miei esercizi di Python!</p>
</p>

## Esercizi 📚

- 1)Scrivere una funzione che converte una stringa di caratteri numerici nell'intero corrispondente. Non usare la funzione `int(string)`.
```python
def string_to_int(string: str) -> int:
    result = ''
    while True:
        string, remainder = divmod(string, 10)
        print(string, remainder)
        result = chr(48 + remainder) + result
        print(result)
        if string == 0: break
    return result
string = string_to_int(100)
print(type(string), string)
```

- 2)Scrivere una funzione che converte un intero in una stringa di caratteri numerici corrispondenti all'intero. Non usare la funzione `str(integer)`.
```python
def int_to_string(integer: int) -> str:
    result = 0
    for x in integer:
        result = result * 10 + ord(x) - ord('0')
    return result
integer = int_to_string('210')
print(type(integer),integer)
```

- 3)Scrivere una funzione che data una stringa, ritorna una lista di tuple consituita da parola e frequenza, ordinata per frequenza. La frequenza è il numero di volte in cui la parole appare nel testo.Per evitare problemi nel trovare le parole, togliere tutti i caratteri non alfanumerici, a parte gli spazi, e convertire le parole in minuscolo. Usare la funzione `isalnum()` per testare i caratteri.
```python
def word_frequency(string: str):
    List = []
    lower = string.lower()
    words = lower.split()
    for word in words:
        count = words.count(word)
        List.append((word, count))
    return list(dict.fromkeys(List))

print( word_frequency('Cane gatto pesce cane pappagallo pesce '))
```
- 4)Scrivere una funzione che data una stringa di numeri interi separati da spazi,ritorna la lista ordinata dei numeri interi con frequenza massima.
```python
def number_frequency(string: str) -> int:
    seq = [int(number) for number in string.split()]
    list1 = {}
    for x in seq:
        if x in list1:
            list1[x] += 1
        else:
            list1[x] = 1
    return sorted(x for x, count in list1.items() if count == max(list1.values()))
print(number_frequency('1 3 6 9 5 1 2 2 3'))
```

- 5)Implementare una funzione `ricorsiva` che data una lista contenente valori e sottoliste, ritorna una lista contenente tutti i valori. Ad esempio: [1, [2, 3]] => [1, 2, 3] e [1, [2, [3, 4]]] => [1, 2, 3, 4]
```python
def flatten_list(elements: list) -> list:
    elements = ''.join(map(str, elements))
    result = []
    for element in elements:
        if element.isnumeric():
            result.append(int(element))
    return result
print(flatten_list([1, [2, [3, 4]]]))
```

- 6)Implementare una funzionalità equivalente a `dict.update()`, che data una lista di dizionari, ritorna un dizionario con tutte le chiavi presenti nei dizionari di input. Per valori, si usano i valori nei dizionari di input scegliendo quelli dei dizionari con indice superiore se presenti.
```python
def update_dict(dictionaries) -> dict:
    result = {}
    for x in dictionaries:
        for i, j in x.items():
            result[i] = j
    return result
print(update_dict([{"Ciao": 1, "Pippo": 2}, {"Pluto": 3, "Pippo": 4}]))
```

- 7)