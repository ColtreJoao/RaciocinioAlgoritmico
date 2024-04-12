# Programa para escrever a tabuada de 1 a 10 de um valor lido entre 1 e 10
valor = int(input("Digite um valor entre 1 e 10: "))
if 1 <= valor <= 10:
    for i in range(1, 11):
        print(f"{valor} x {i} = {valor*i}")
else:
    print("Valor inválido!")
print(50*"-")