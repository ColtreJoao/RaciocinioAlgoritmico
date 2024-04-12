# Programa para calcular e mostrar a soma dos 50 primeiros números pares
soma_pares = 0
contador = 0
for num in range(2, 101, 2):
    soma_pares += num
    contador += 1
    if contador == 50:
        break
print(f"A soma dos 50 primeiros números pares é: {soma_pares}")
print(50*"-")