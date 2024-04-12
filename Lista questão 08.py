# Programa para imprimir os divisores de um número positivo
numero = int(input("Digite um número positivo: "))
print("Divisores de", numero, ":")
for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
print(50*"-")   
