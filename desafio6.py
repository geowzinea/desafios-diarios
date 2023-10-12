#1. Receba 3 valores (numeros inteiros) do usuário
#2. Imprima eles em ordem crescente

n = []
for i in range(3):
    numero = int(input(f'Digite o {i + 1}º número inteiro: '))
    n.append(numero)


for numero in n:
    print(numero, end=" ")