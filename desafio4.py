#1. Peça 3 notas para o usuário inserir (P1, P2 e P3)
#2. Some essas notas e imprima a média da pessoa (a média é a soma das 3 notas, dividido por 3).

P1 = float(input('Digite sua primeira nota: '))
P2 = float(input('Digite sua segunda nota: '))
P3 = float(input('Digite sua terceira nota: '))
m = P1 + P2 + P3 / 3
print(f'A média é {m}')