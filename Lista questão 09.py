# Programa para ler 10 números inteiros, armazená-los em uma lista e imprimir em ordem crescente
numeros = []
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
numeros.sort()
print("Números em ordem crescente:", numeros)
print(50*"-")