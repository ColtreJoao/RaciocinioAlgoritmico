
# Programa para contar quantos números estão no intervalo [10,20] e quantos estão fora
dentro_intervalo = 0
fora_intervalo = 0
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    if 10 <= num <= 20:
        dentro_intervalo += 1
    else:
        fora_intervalo += 1
print(f"Números dentro do intervalo [10,20]: {dentro_intervalo}")
print(f"Números fora do intervalo [10,20]: {fora_intervalo}")
print(50*"-")
