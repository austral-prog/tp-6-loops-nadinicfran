# Replace the "ANSWER HERE" for your answer

def sum_to_n(n):
    """
    Retorna la suma de todos los enteros desde 1 hasta n (inclusive).
    Si n <= 0, retorna 0.
    """
    if n <= 0:
        return 0

    total = 0
    for i in range(1, n + 1):
        total += i

    return total


def sum_evens(n):
    """
    Retorna la suma de todos los numeros pares desde 1 hasta n (inclusive).
    Si n <= 0, retorna 0.
    """
    if n <= 0:
        return 0

    total = 0
    for i in range(2, n + 1, 2):
        total += i

    return total


def factorial(n):
    """
    Retorna el factorial de n (n!).
    Si n <= 0, retorna 1.
    """
    if n <= 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result
