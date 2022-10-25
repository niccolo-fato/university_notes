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
    words = string.split()
    for word in words:
        count = words.count(word)
        List.append((word, count))
    return list(dict.fromkeys(List))

print( word_frequency('cane gatto pesce cane pappagallo pesce '))
```