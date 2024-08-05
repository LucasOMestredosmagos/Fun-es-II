numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def quadrado(x):
    return x**2
quadrados = list(map(quadrado, numeros))
print(quadrados)

def eh_par(x):
    return x % 2 == 0
pares = list(filter(eh_par, numeros))
print(pares)

from functools import reduce
soma = reduce(lambda x, y: x + y, numeros)
print(soma)
