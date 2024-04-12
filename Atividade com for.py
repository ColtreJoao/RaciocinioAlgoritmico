#imprimir os números de 1 a 10
for i in range(1,11):
    print(i)
    
#imprimir elementos de um vetor qualquer
#criando um vetor
vetor = ["azul","branco","verde"]
for cor in vetor:
    print(cor)
    
#Outra forma de fazer(caso precise do indice)
for i in range(0,len(vetor)):
    print(f"Elemento {i}: Valor: {vetor[i]}")