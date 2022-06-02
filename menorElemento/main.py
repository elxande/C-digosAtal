def menorElemento(lista, primeiroElemento, ultimoElemento):

    if ( primeiroElemento > ultimoElemento):
        return ultimoElemento + 1

    if (primeiroElemento != lista[primeiroElemento]):
        return primeiroElemento

    meio = (primeiroElemento + ultimoElemento)//2

    if (lista[meio] == meio):
        return menorElemento(lista, meio+1, ultimoElemento)

    return menorElemento(lista, primeiroElemento, meio)


lista1 = [0, 1, 2, 6, 9, 11, 15]
lista2 = [1, 2, 3, 4, 6, 9, 11, 15]
lista3 = [0, 1, 2, 3, 4, 5, 6, 8]

teste1 = menorElemento(lista1, 0, len(lista1))
teste2 = menorElemento(lista2, 0, len(lista2))
teste3 = menorElemento(lista3, 0, len(lista3))
print(teste1)
print(teste2)
print(teste3)

