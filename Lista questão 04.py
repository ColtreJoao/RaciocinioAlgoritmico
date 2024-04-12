# Programa para calcular a média entre várias idades
soma = 0
contador = 0
while True:
    idade = int(input("Digite uma idade (ou digite 0 para sair): "))
    if idade == 0:
        break
    soma += idade
    contador += 1
if contador != 0:
    media = soma / contador
    print(f"A média das idades é: {media}")
else:
    print("Nenhuma idade foi inserida.")
    print(50*"-")
