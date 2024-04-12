# Programa para imprimir o número que mais se repete em uma lista
lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
num_repetido = 0
num_freq = 0
for num in lista:
    count = lista.count(num)
    if count > num_freq:
        num_repetido = num
        num_freq = count


print(50*"-")
print(f"O número que mais se repitiu foi: {num_repetido}")
print(50*"-")