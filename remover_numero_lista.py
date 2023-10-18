#        0  1  2  3  4
lista = [1, 2, 3, 4, 5]
indice_remover = 2
i = indice_remover

while i < len(lista) - 1:
    lista[1] = lista[i + 1]
    i += 1
lista.pop()
print(lista)