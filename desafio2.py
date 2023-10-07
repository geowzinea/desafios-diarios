#1. Receba o nome do usuário como entrada
#2. Imprima o nome do usuário com todas as letras em maiúsculo
#Dado o nome do usuário, imprima uma mensagem de boas vindas acompanhado do nome capitalizado (apenas as palavras do nome em maíusculo)

nome = str(input("Qual é o seu nome? "))
print(nome.upper())
print(f'Seja bem-vindo {nome.upper()}')