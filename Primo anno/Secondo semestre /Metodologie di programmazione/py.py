def fibonacci(n):
    if n < 0:
        raise ValueError("Il numero di Fibonacci deve essere maggiore o uguale a 0")
    if n <= 1:
        return n
    fib_0 = 0
    fib_1 = 1
    for i in range(2, n+1):
        fib_i = fib_0 + fib_1
        fib_0 = fib_1
        fib_1 = fib_i
    return fib_i
print(fibonacci(4))