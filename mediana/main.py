def mediana(lista1, lista2, tamanho):
    if (tamanho == 1):
        return (lista1[0] + lista2[0]) // 2
    elif (tamanho == 2):
        return (lista1[1] + lista2[0]) // 2
    else:
        meio = tamanho//2
        if (lista1[meio] == lista2[meio]):
            return (lista1[meio] + lista2[meio]) // 2
        elif (lista1[meio] < lista2[meio]):
            novaLista1 = lista1[meio+1 : ]
            novaLista2 = lista2[: meio]
            return mediana(novaLista1, novaLista2, meio)
        else:
            novaLista1 = lista1[ : meio]
            novaLista2 = lista2[meio : ]
            return mediana(novaLista1, novaLista2, meio)

a = [2, 3, 6, 7, 9]
b = [1, 2, 6, 10, 11]
c = [0, 1, 2, 4, 5]
d = [7, 9, 10, 12, 13]
tam = 5
print("Mediana lista1:",mediana(a,b,tam))
print("Mediana lista2:",mediana(c,d,tam))
